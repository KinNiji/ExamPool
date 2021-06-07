# -*- coding: utf-8 -*-
"""
Created on Mon May 31 00:15:28 2021

@author: Niji
"""

import dash

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from dash.dependencies import Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate

import pymysql

import random
import datetime
from base64 import b64encode
from os import urandom
import json

opt_list = ['A', 'B', 'C', 'D', 'E']

with open('mysql.json', 'r') as f:
    mysql_config = json.load(f)
 
def getQuestion(row, shuffle):
    _id = row[0]
    _chap = row[1]
    
    # 题干
    _stem = row[2]
    
    # 题型信息
    type_info = row[-1]
    # 选项数量
    _count = int(type_info[-1])
    # 题型
    _type = type_info[:-1]
    
    # 乱序映射
    _shuffled = opt_list.copy()[:_count]
    if shuffle:
        random.shuffle(_shuffled)
    
    # 选项文本、映射后选项
    options_text = row[3: 3 + _count]
    _options = [{'label': options_text[_shuffled.index(opt_list[i])], 'value': opt_list[i]} for i in range(_count)]
    
    # 答案文本、映射后选项
    answer_text = list(row[-2])
    _answer = [_shuffled[opt_list.index(ans)] for ans in answer_text]
    
    return dict(_id=_id,
                _chap=_chap,
                _stem=_stem,
                _count=_count,
                _type=_type,
                _shuffled=_shuffled,
                _options=_options,
                _answer=_answer)

def MappingChoice(question_bank, user_choices):
    mapped_choices = {}
    
    for _id, choice in user_choices.items():
        _shuffled = question_bank[int(_id) - 1]['_shuffled']
        mapped_choice = []
        for c in choice:
            mapped_choice.append(opt_list[_shuffled.index(c)])
        _id = question_bank[int(_id) - 1]['_id']
        mapped_choices[_id] = mapped_choice
    return mapped_choices

def getUser(row):
    return dict(Uid=row[0],
                stuID=row[1],
                nickname=row[2],
                invite_code=row[3],
                inviter_code=row[4],
                authority=row[5])
           
def getConnection(old):
    def new_function(*args, **kwargs):
        conn = pymysql.connect(host='localhost', port = mysql_config['port'], user = mysql_config['user'], passwd = mysql_config['password'], db = mysql_config['db'])
        cur = conn.cursor()
        res = None
        try:
            res = old(cur, *args, **kwargs)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            res = e
        finally:
            cur.close()
            conn.close()
        
        return res
    return new_function


@getConnection
def getQuestionBank(cur, database, shuffle, wrong_filter):
    question_bank = []
    
    query = 'select * from ' + database
    row_count = cur.execute(query)
    for i in range(row_count):
        row = cur.fetchone()
        question_bank.append(getQuestion(row, shuffle))
    if wrong_filter:
        question_bank_filter = []
        for i in wrong_filter:
            question_bank_filter.append(question_bank[int(i) - 1])
        question_bank = question_bank_filter
    if shuffle:
         random.shuffle(question_bank)
    return question_bank

@getConnection
def getBankList(cur):
    bank_list = []
    
    query = 'select CN, bank_name from banks'
    row_count = cur.execute(query)
    for i in range(row_count):
        row = cur.fetchone()
        # if row[1] != 'bank_test':
        bank_list.append({'label': row[0], 'value': row[1]})
    return bank_list

@getConnection
def getBankSize(cur, database):
    query = 'select count(*) from ' + database
    row_count = cur.execute(query)
    if row_count:
        row_count = cur.fetchone()[0]
    return int(row_count)
    
@getConnection
def stuIDCheck(cur, stuID):
    query = 'select count(*) from user where stuID=%s'
    row_count = cur.execute(query, (stuID))
    if row_count:
        row_count = cur.fetchone()[0]
        if row_count==0:
            return False
        else:
            return True
    else:
        return True

@getConnection
def inviterCodeCheck(cur, inviter_code):
    query = 'select count(*) from user where invite_code=%s'
    row_count = cur.execute(query, (inviter_code))
    if row_count:
        return cur.fetchone()[0]
    else:
        return False

@getConnection
def loginCheck(cur, stuID, password):
    query = 'select Uid, stuID, nickname, invite_code, inviter_code, authority from user where stuID=%s and password=%s'
    row_count = cur.execute(query, (stuID, password))
    if row_count:
        return cur.fetchone()
    else:
        return False
   
@getConnection
def storeUser(cur, stuID, password, nickname, invite_code, inviter_code, authority):
    query = 'insert into user (stuID, password, nickname, invite_code, inviter_code, authority) values (%s, %s, %s, %s, %s, %s)'
    row_count = cur.execute(query, (stuID, password, nickname, invite_code, inviter_code, authority))
    return True if row_count else False

@getConnection
def storeRecord(cur, Uid, time, bank_name, mode, record, wrong_questions):
    query = 'insert into records values (%s, %s, %s, %s, %s, %s)'
    row_count = cur.execute(query, (Uid, time, bank_name, mode, record, wrong_questions))
    return True if row_count else False
    
@getConnection
def getHistoryWrong(cur, Uid, bank_name):
    history_wrong = []
    query = 'select wrong_questions, bank_name, mode from records where Uid=%s and bank_name=%s'
    row_count = cur.execute(query, (Uid, bank_name))
    for i in range(row_count):
        row = cur.fetchone()
        record = row[0][1:-1].split(',')
        for _id in record:
            _id = int(_id)
            history_wrong.append(_id)
    return list(set(history_wrong))

def build_register_form():
    return html.Div([
        dbc.Row([
            dbc.Col(
                html.H3('注册', id='login-text'),
                className='mt-3'
            )
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Input(
                    id='register-stuID-input',
                    type='text',
                    placeholder='学号',
                ), 
                className='mt-3'
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Input(
                    id='register-password-input',
                    type='password',
                    placeholder='密码',
                ), 
                className='mt-3'
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Input(
                    id='register-password2-input',
                    type='password',
                    placeholder='确认密码',
                ), 
                className='mt-3'
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Input(
                    id='register-nickname-input',
                    type='text',
                    placeholder='昵称',
                ), 
                className='mt-3'
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Input(
                    id='register-invite-code-input',
                    type='text',
                    placeholder='邀请码',
                ), 
                className='mt-3'
            ),
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(id='register-state'), 
                className='mt-3',
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Button('注册', id='register-submit-button', n_clicks=0, block=True, outline=True, color='primary'), 
                className='mt-3'
            ),
        ]),
    ], className='login-form')

def build_login_form():
    return html.Div([
        dbc.Row([
            dbc.Col(
                html.H3('登录', id='login-text'),
                className='mt-3'
            )
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Input(
                    id='login-stuID-input',
                    type='text',
                    placeholder='学号',
                ), 
                className='mt-3'
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Input(
                    id='login-password-input',
                    type='password',
                    placeholder='密码',
                ), 
                className='mt-3'
            ),
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(id='login-state'), 
                className='mt-3',
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Button('登录', id='login-submit-button', href='/', block=True, outline=True, color='primary'), 
                className='mt-3'
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dbc.Button('注册', href='/register', n_clicks=0, block=True, outline=True, color='primary'), 
                className='mt-3'
            ),
        ]),
    ], className='login-form')

index_content = html.Div(
    [
        html.Div([
            html.H2("主页", className='mb-4'),
            html.P("模拟题库，基于Dash编写，支持四、五选项的单选和多选，有顺序、随机、错题三种模式可选。浏览器建议缩放比133%，笔记本缩放比请自行调整。限于网站机能，点击校对答案和切换题目时可能会出现卡顿或渲染失败的情况，可下载源码后部署至本地服务器以消除上述卡顿。"),
            html.P("！卡顿还是很明显的，十分建议下载源码并在本地服务器运行。", style={'color': 'red'}),
            html.P("稳定版网址：https://exampool.cn1.utools.club 开发版网址：https://exampooldevelopment.cn1.utools.club"),
            html.Hr(),
            html.H4("即将实现的功能：", className='mb-4'),
            # html.P("2.用户注册、登录系统", style={'text-decoration':'line-through'}),
            html.P("——————————已停止开发——————————"),
            html.P("4.模拟考试模式"),
            html.P("5.移动端网页适配"),
            html.P("6.快捷键实现切题和校对功能"),
            html.P("7.数据分析功能"),
            html.Hr(),
            html.P([
                "本项目开源，当前版本：Development Ver2.4 & Test Ver1.0", 
                dbc.Badge("github源码", href="https://github.com/KinNiji/ExamPool", color="primary", className='ml-3')
            ]),
            html.P("严重Bug请反馈至郑皓煜", className="mb-0"),
        ])
    ], className='app-index')

def build_user_info():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.H4(id="user-info-text"), 
                html.P(['欢迎使用ExamPool！']),
                dbc.Button("账号管理", id='user-info-management', href='/mgm', n_clicks=0, outline=True, color="primary"), 
            ]),
            color="light"
        )
    ], className="mb-5")

def build_user_management():
    return html.Div([
        
    ])

bank_list = getBankList()
    
sidebar = html.Div(
    [
        build_user_info(),
        dbc.Nav(
            [
                dbc.NavLink("主页", href="/", active="exact"),
                dbc.NavItem(html.Hr()),
                dbc.NavLink("顺序练习", href="/asc", active="exact"),
                dbc.NavLink("随机练习", href="/rdm", active="exact"),
                dbc.NavLink("错题练习", href="/mis", active="exact"),
                dbc.NavItem(html.Hr()),
                dbc.NavLink("模拟考试", href="/sim", active="exact"),
                dbc.NavItem(html.Hr()),
                dbc.NavLink("数据统计", href="/sta", active="exact"),
            ],
            vertical='lg',
            pills=True,
        ),
    ],
    className="app-sidebar"
)

sidebar_content = html.Div(
    id="sidebar-content", 
    className="app-sidebar-content"
)

asc_content = html.Div([
    html.H4('顺序练习'),
    dbc.Label("选择题库"),
    dbc.Select(options=bank_list, value=bank_list[0]['value'], id={'mode': 'asc', 'name': 'bank-name'}, className='mb-3'),
    dbc.Label("起始题号"),
    dbc.Input(value=1, id={'mode': 'asc', 'name': 'beginning-input'}, type="number", min=1, step=1, className='mb-3'),
    dbc.Label("抽取题数"),
    dbc.Input(value=50, id={'mode': 'asc', 'name': 'max-input'}, type="number", min=1, step=1, className='mb-3'),
    dbc.Button('开始', id={'mode': 'asc', 'name': 'start-button'}),
], id={'mode': 'asc', 'name': 'exercise-content'})

rdm_content = html.Div([
    html.H4('随机练习'),
    dbc.Label("选择题库"),
    dbc.Select(options=bank_list, value=bank_list[0]['value'], id={'mode': 'rdm', 'name': 'bank-name'}, className='mb-3'),
    dbc.Label("抽取题数"),
    dbc.Input(value=50, id={'mode': 'rdm', 'name': 'max-input'}, type="number", min=1, step=1, className='mb-3'),
    dbc.Button('开始', id={'mode': 'rdm', 'name': 'start-button'}),
], id={'mode': 'rdm', 'name': 'exercise-content'})

mis_content = html.Div([
    html.H4('错题练习'),
    dbc.Label("选择题库"),
    dbc.Select(options=bank_list, value=bank_list[0]['value'], id={'mode': 'mis', 'name': 'bank-name'}, className='mb-3'),
    dbc.Label("错题量（显示为0表示该题库无错题，不会进入练习）"),
    dbc.Input(value=0, id={'mode': 'mis', 'name': 'max-input'}, type="number", min=0, step=1, className='mb-3', disabled=True),
    dbc.Button('开始', id={'mode': 'mis', 'name': 'start-button'}),
], id={'mode': 'mis', 'name': 'exercise-content'})

def buildAnswerReveal():
    return html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Button("校对答案", id='answer-reveal-button', n_clicks=0, outline=True, color="primary", className='mr-3'),
                dbc.Label("正确答案："), 
                dbc.Label(id='answer'),
                dbc.Label(id='history'),
            ], width=6),
            dbc.Col(id='answer-compare', width=3),
            
            dbc.Col(),
        ])
    ], className='mb-3')

def buildQuestionButtons():
    return html.Div([
        dbc.ButtonGroup([
            dbc.Button("到开始", id='question-beginning-button', n_clicks=0, outline=True, color="primary"),
            dbc.Button("上一题", id='question-preone-button', n_clicks=0, outline=True, color="primary"),
            dbc.Button("下一题", id='question-nextone-button', n_clicks=0, outline=True, color="primary"),
            dbc.Button("到最后", id='question-endding-button', n_clicks=0, outline=True, color="primary"),
        ])
    ], className='mb-5')

def buildQuestionIdSelector(the_beginning, the_max):
    return html.Div([
        dbc.FormGroup([
            dbc.Label("选择题号"),
            dbc.RadioItems(
                options=[
                    {"label": str(i), "value": i} for i in range(the_beginning, the_beginning + the_max)
                ],
                value=the_beginning,
                id="question-id-selector",
                inline=True,
            ),
        ])
    ], className='mb-3')

def buildQuestionCombination(database, the_beginning, the_max, shuffle=False, wrong_filter=None):
    return html.Div([
        dcc.Store(data=getQuestionBank(database, shuffle, wrong_filter), id='question-bank'),
        dcc.Store(data={}, id='temp-user-choices'),
        dcc.Store(data={}, id='user-choices'),
        dcc.Store(data=[], id='wrong-questions'),
        
        dbc.Label(id='question-stem'),
        html.Div(id='question-options', className='mb-3'),
        buildAnswerReveal(),
        buildQuestionButtons(),
        buildQuestionIdSelector(the_beginning, the_max),
        dbc.Button('保存做题记录并返回', id='question-history-save', href='/'),
    ])

true_label = dbc.Alert("回答正确！", color="success", dismissable=True)
false_label = dbc.Alert("回答错误！", color="danger", dismissable=True)






























external_stylesheets = [
    dbc.themes.BOOTSTRAP,
]

app = dash.Dash(
    __name__,
    title="ExamPool!",
    update_title=None,
    external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    suppress_callback_exceptions=True
)
server = app.server

app.layout = html.Div([
    dcc.Store(data=None, id='user-info'),
    dcc.Store(id='config'),
    html.Div([
        sidebar, 
        dcc.Location(id="url"), 
        sidebar_content
    ],id='content'),
    dbc.Toast(
        html.P(id='question-hint-text'),
        id="question-toast",
        header="提示",
        dismissable=True,
        icon="primary",
        is_open=False,
        duration=5000,
        className='hint-toast',
    ),
])



















# 注册信息验证，通过验证后保存
@app.callback(
    Output('register-state', 'children'),
    [Input('register-submit-button', 'n_clicks')],
    [State('register-stuID-input', 'value'),
     State('register-password-input', 'value'),
     State('register-password2-input', 'value'),
     State('register-nickname-input', 'value'),
     State('register-invite-code-input', 'value')])
def store_user(n_clicks, stuID, password, password2, nickname, inviter_code):
    if n_clicks==0:
        raise PreventUpdate
    else:
        if not (stuID and password and password2 and nickname and inviter_code):
            return dbc.Alert('所有字段都为必填！', color='danger', dismissable=True)
        elif stuIDCheck(stuID):
            return dbc.Alert('此学号已注册！', color='danger', dismissable=True)
        elif password != password2:
            return dbc.Alert('两次输入的密码不一致！', color='danger', dismissable=True)
        elif not inviterCodeCheck(inviter_code):
            return dbc.Alert('邀请码错误！', color='danger', dismissable=True)
        else:
            storeUser(stuID, 
                      password, 
                      nickname, 
                      b64encode(urandom(3)).decode('utf-8'), 
                      inviter_code, 
                      'user')
            return dbc.Alert('注册成功', color='success', dismissable=True)
        
# 登录验证，登录成功后将用户信息写入配置 or 退出登录，清除配置
@app.callback(
    [Output('login-state', 'children'),
     Output('user-info', 'data')],
    [Input('login-submit-button', 'n_clicks')],
    [State('login-stuID-input', 'value'),
     State('login-password-input', 'value')])
def update_login_state(n1, stuID, password):
    if n1:
        res = loginCheck(stuID, password)
        if res==False:
            return dbc.Alert('登陆失败', color='danger', dismissable=True), "null"
        else:
            if res[-1] == 'denied':
                return dbc.Alert('您没有权限登录！', color='danger', dismissable=True), "null"
            else:
                return dbc.Alert('登陆成功', color='success', dismissable=True), getUser(res)
    else:
        raise PreventUpdate

# 显示用户昵称，控制按钮状态
@app.callback(
    [Output('user-info-text', 'children'),
     Output('user-info-management', 'disabled')],
    [Input('user-info', 'data')])
def update_user_info_text(user_info):
    if user_info is None:
        return dbc.Button('登录', href='/login', n_clicks=0, block=True, outline=True, color='danger'), True
    elif user_info == "null":
        raise PreventUpdate
    else:
        return '用户 ' + user_info['nickname'], False

## 顺序模式
# 监听题库名，并设置起始题号上限
@app.callback(
    Output({'mode': 'asc', 'name': 'beginning-input'}, 'max'),
    [Input({'mode': 'asc', 'name': 'bank-name'},'value')])
def ASCupdateBeginningMax(database):
    return getBankSize(database)

# 监听起始题号，并设置抽取题数上限
@app.callback(
    Output({'mode': 'asc', 'name': 'max-input'}, 'max'),
    [Input({'mode': 'asc', 'name': 'beginning-input'}, 'value'),
     Input({'mode': 'asc', 'name': 'beginning-input'}, 'max')])
def ASCupdateMaxInput(the_beginning, max_size):
    return max_size - the_beginning + 1

## 随机模式
# 监听题库名，并设置抽取题数上限
@app.callback(
    Output({'mode': 'rdm', 'name': 'max-input'}, 'max'),
    [Input({'mode': 'rdm', 'name': 'bank-name'}, 'value')])
def RDMupdateBeginningMax(database):
    return getBankSize(database)

## 错题模式
# 监听题库名，查询错题量
@app.callback(
    Output({'mode': 'mis', 'name': 'max-input'}, 'value'),
    [Input({'mode': 'mis', 'name': 'bank-name'}, 'value')],
    State('user-info', 'data'))
def MISupdateBeginningMax(database, user_info):
    return len(getHistoryWrong(user_info['Uid'], database))

##开始练习
# 点击开始按钮时，将题库名、起始题号、抽取题数写入配置
@app.callback(
    Output('config', 'data'),
    [Input({'mode': ALL, 'name': 'start-button'}, 'n_clicks')],
    [State({'mode': ALL, 'name': 'bank-name'}, 'value'),
     State({'mode': ALL, 'name': 'beginning-input'}, 'value'),
     State({'mode': ALL, 'name': 'max-input'}, 'value')])
def updateAscConfig(n_clicks, database, the_beginning, the_max):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if ('asc' in changed_id) and ('start-button' in changed_id):
        return {'database': database[0], 'the_beginning': int(the_beginning[0]), 'the_max': int(the_max[0]), 'mode': 'asc'}
    elif ('rdm' in changed_id) and ('start-button' in changed_id):
        return {'database': database[0], 'the_beginning': 1, 'the_max': int(the_max[0]), 'mode': 'rdm'}
    elif ('mis' in changed_id) and ('start-button' in changed_id):
        return {'database': database[0], 'the_beginning': 1, 'the_max': int(the_max[0]), 'mode': 'mis'}
    else:
        raise PreventUpdate

# 点击开始按钮时，更新练习界面
@app.callback(
    Output({'mode': MATCH, 'name': 'exercise-content'}, 'children'),
    [Input({'mode': MATCH, 'name': 'start-button'}, 'n_clicks'),
     Input('config', 'data')],
    State('user-info', 'data'))
def updateContent(n_clicks, config, user_info):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if ('asc' in changed_id) and ('start-button' in changed_id) and n_clicks:
        return buildQuestionCombination(config['database'], config['the_beginning'], config['the_max'])
    elif ('rdm' in changed_id) and ('start-button' in changed_id) and n_clicks:
        return buildQuestionCombination(config['database'], config['the_beginning'], config['the_max'], shuffle=True)
    elif ('mis' in changed_id) and ('start-button' in changed_id) and n_clicks:
        if config['the_max']:
            return buildQuestionCombination(config['database'], config['the_beginning'], config['the_max'], wrong_filter=getHistoryWrong(user_info['Uid'], config['database']), shuffle=True)
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate

# 根据题号切换题目（题号选择器控制题目内容）
@app.callback(
    [Output('question-stem', 'children'),
     Output('question-options', 'children')],
    [Input('question-id-selector', 'value'),
     Input('question-bank', 'data')])
def updateQuestionBySelector(_id, question_bank):
    _id = _id - 1
    question = question_bank[_id]
    options_group = None
    type_CN = ''
    if question['_type'] == 'Single':
        type_CN = '单选'
        options_group = dbc.RadioItems(
            options=question['_options'],
            id={'_id': _id, 'name': 'question-options'},
            labelCheckedStyle={"color": "#007BFF"},
        )
    elif question['_type'] == 'Multiple':
        type_CN = '多选'
        options_group = dbc.Checklist(
            options= question['_options'],
            id={'_id': _id, 'name': 'question-options'},
            labelCheckedStyle={"color": "#007BFF"},
        )
    return '{_id}、（{type_CN}）{question}（    ）'.format(_id=str(_id + 1), type_CN=type_CN, question=question['_stem']), options_group

# 根据题号切换题目（切题按钮组控制题号选择器）
@app.callback(
    Output('question-id-selector', 'value'),
    [Input('question-beginning-button', 'n_clicks'),
     Input('question-preone-button', 'n_clicks'),
     Input('question-nextone-button', 'n_clicks'),
     Input('question-endding-button', 'n_clicks')],
    [State('question-id-selector', 'value'),
     State('config', 'data')])
def updateQuestionByButtons(beginning, preone, nextone, endding, _id, config):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    the_beginning = config['the_beginning']
    the_max = config['the_max']
    if 'question-nextone-button' in changed_id:
        _id = (_id + 1) if _id < the_beginning + the_max - 1 else the_beginning
    elif 'question-preone-button' in changed_id:
        _id = (_id - 1) if _id > the_beginning else the_beginning + the_max - 1
    elif 'question-endding-button' in changed_id:
        _id = the_beginning + the_max - 1
    elif 'question-beginning-button' in changed_id:
        _id = the_beginning
    else:
        raise PreventUpdate
    return _id

# 保留临时做题记录
@app.callback(
    Output('temp-user-choices', 'data'),
    [Input({'_id': ALL, 'name': 'question-options'}, 'value')],
    [State('question-id-selector', 'value'),
     State('temp-user-choices', 'data')])
def storeTempUserChoice(temp_user_choice, _id, temp_user_choices):
    if temp_user_choice == [None]:
        raise PreventUpdate
    else:
        if len(temp_user_choice) and type(temp_user_choice[0]) is list:
            temp_user_choice = temp_user_choice[0]
            temp_user_choice.sort()
        temp_user_choices[str(_id)] = temp_user_choice
        # print('temp', temp_user_choices)
        return temp_user_choices

# 校对答案，显示正误,保留做题记录
@app.callback(
    [Output('answer', 'children'),
     Output('answer-compare', 'children'),
     Output('user-choices', 'data'),
     Output('wrong-questions', 'data')],
    [Input('answer-reveal-button', 'n_clicks'),
     Input('question-id-selector', 'value'),
     Input({'_id': ALL, 'name': 'question-options'}, 'value')],
    [State('question-bank', 'data'),
     State('temp-user-choices', 'data'),
     State('user-choices', 'data'),
     State('wrong-questions', 'data')])
def updateAnsewer(n_clicks, _id, temp_user_choice, question_bank, temp_user_choices, user_choices, wrong_questions):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    question = question_bank[_id - 1]
    answer = question['_answer']
    if 'answer-reveal-button' in changed_id:
        if temp_user_choice == [None]:
            temp_history = temp_user_choices.get(str(_id))
            if temp_history is not None:
                temp_user_choice = temp_history
        else:
            if type(temp_user_choice[0]) is list:
                temp_user_choice = temp_user_choice[0]
                temp_user_choice.sort()
            if answer != temp_user_choice:
                wrong_questions.append(question['_id'])
        user_choices[str(_id)] = temp_user_choice
        # print('    ', temp_user_choices)
        # print('wrong', wrong_questions)
        return ''.join(answer), true_label if answer==temp_user_choice else false_label, user_choices, wrong_questions
    elif 'question-id-selector' in changed_id:
        history = user_choices.get(str(_id))
        if history is None:
            return None, None, user_choices, wrong_questions
        else:
            return ''.join(answer), true_label if answer==history else false_label, user_choices, wrong_questions
    else:
        raise PreventUpdate

# 对比两份做题记录回溯用户选项
@app.callback(
    Output('history', 'children'),
    [Input('question-id-selector', 'value')],
    [State('temp-user-choices', 'data'),
     State('user-choices', 'data')])
def updateTempOptionState(_id, temp_user_choices, user_choices):
    temp_history = temp_user_choices.get(str(_id))
    history = user_choices.get(str(_id))
    if history is None or len(history)==0:
        if temp_history is None or len(temp_history)==0:
            return None
        else:
            return '上一次选择：' + str(temp_history)
    else:
        return '历史选择：' + str(history)

# 保存做题记录
@app.callback(
    [Output("question-toast", "is_open"),
     Output("question-hint-text", "children")],
    [Input('question-history-save', 'n_clicks')],
    [State("question-toast", "is_open"),
     State('user-choices', 'data'),
     State('wrong-questions', 'data'),
     State('question-bank', 'data'),
     State('user-info', 'data'),
     State('config', 'data')])
def store_record(n_clicks, is_open, user_choices, wrong_questions, question_bank, user_info, config):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'question-history-save' in changed_id and n_clicks:
        res = storeRecord(user_info['Uid'], 
                          datetime.datetime.now(), 
                          config['database'], 
                          config['mode'], 
                          str(MappingChoice(question_bank, user_choices)),
                          str(wrong_questions))
        if res == 1:
            res = '保存成功！'
        return True, res
    return False, None

# url route
@app.callback(
    Output("sidebar-content", "children"), 
    [Input("url", "pathname"),
     Input('user-info', 'data')])
def update_sidebar_content(pathname, user_info):
    if user_info is None:
        if pathname == "/":
            return index_content
        elif pathname == "/login":
            return build_login_form()
        elif pathname == "/register":
            return build_register_form()
        else:
            return build_login_form()
    elif user_info == "null":
        raise PreventUpdate
    else:
        if pathname == "/":
            return index_content
        elif pathname == "/asc":
            return asc_content
        elif pathname == "/rdm":
            return rdm_content
        elif pathname == "/mis":
            return mis_content
        elif pathname == "/sim":
            return html.Div([html.H4('模拟考试'),html.Div('开发中')])
        elif pathname == "/sta":
            return html.Div([html.H4('数据统计'),html.Div('开发中')])
        elif pathname == "/mgm":
            return html.Div([html.H4('账号管理'),html.Div('开发中')])
        return index_content

if __name__ == "__main__":
    app.run_server(debug=False)