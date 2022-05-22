import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
from dash.dependencies import Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate

import json
import pandas as pd

from question import Core
from user import User

core = Core()
user = User()

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
]

app = dash.Dash(
    __name__,
    title="ExamPool",
    update_title=None,
    external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    suppress_callback_exceptions=True
)

login = html.Div(
    id='login-div',
    children=[
        dbc.Card(
            dbc.CardBody(
                id='login-card',
                children=[
                    html.H3('登录', className='mb-4'),
                    dbc.Input(
                        id='login-stu-id-input',
                        type='text',
                        placeholder='学号',
                        className='mb-4'
                    ),
                    dbc.Input(
                        id='login-password-input',
                        type='password',
                        placeholder='密码',
                        className='mb-4'
                    ),
                    dbc.Button('登录', id='login-submit-button', outline=True, color='primary', className=''),
                ]
            ),
            className='mx-auto px-4 py-4',
            style={'width': '50%', 'max-width': '400px'}
        ),
    ],
    className='mx-5'
)

main = html.Div(
    [
        html.H2("主页", className='mb-4'),
        html.P("模拟题库，基于Dash编写。"),
        html.P("练习模式可用，功能基本已经齐全，具体请自行体验。方法：左侧侧边栏点击刷题，选择题库后，选择练习模式开始使用。"),
        html.P("剩下的部分都没写。"),
        html.P("如果发现bug，请反馈至郑皓煜。"),
        html.P("如果是题目的错误，可连接至222.193.29.67的3308端口，使用用户名为question_checker，密码为123456的用户对题目进行修改。"),
        html.P([
            "本项目开源，当前版本：2021_12_beta",
            dbc.Badge(
                html.A("github源码，开发至稳定版本时上传。", href="https://github.com/KinNiji/ExamPool", target='_blank'),
                color="white", text_color="black", className='ml-3'
            )
        ]),
    ],
    className='mx-5 my-5'
)


def build_mode_card(mode, header, description, badges):
    return dbc.Card(
        children=dbc.CardBody([
            html.H4(header),
            html.P(description),
            html.P([dbc.Badge(badge, color="primary", className="me-1") for badge in badges]),
            dbc.Button(
                id={'name': 'exercise-mode-choose-button', 'mode': mode},
                children="选择",
                className='btn-16'
            ),
        ]),
        className='mb-4'
    )


exercise = html.Div(
    id='exercise',
    children=[
        html.Div(
            id='exercise-content',
            children=[
                html.H2('选择题库', className='mb-4'),
                dbc.Select(
                    id='exercise-bank-select',
                    placeholder='——请选择题库——',
                    options=core.get_banks(),
                    className='mb-4'
                ),
                html.Div(
                    id='exercise-configs',
                    children=[
                        html.H2('选择模式', className='mb-4'),
                        build_mode_card('norm', '练习', '自定义规则抽取题目进行练习。',
                                        ['题量控制', '题型筛选', '章节筛选', '打乱功能', '收藏功能']),
                        build_mode_card('exam', '模考', '提供考试规则，进行仿真模拟。',
                                        ['指定题型和题量的组合', '乱序抽取', '打乱选项']),
                    ]
                )
            ],
            className='mx-5 my-5'
        )
    ]
)
record = html.Div(
    [
        html.H2("记录", className='mb-4'),
    ],
    className='mx-5 my-5'
)
setting = html.Div(
    [
        html.H2("设置", className='mb-4'),
        dbc.Button(
            id='change-password-button',
            children='修改密码',
            disabled=True
        ),
        dbc.Button(
            id='logout-button',
            children='登出',
            disabled=True
        ),
    ],
    className='mx-5 my-5'
)

sidebar = [
    dtc.SideBar(
        id='sidebar',
        children=[
            dtc.SideBarItem(id='sidebar-item-1', label="主页", icon="fas fa-home"),
            dtc.SideBarItem(id='sidebar-item-2', label="刷题", icon="fas fa-list-alt"),
            dtc.SideBarItem(id='sidebar-item-3', label="记录", icon="fas fa-info-circle"),
            dtc.SideBarItem(id='sidebar-item-4', label="设置", icon="fas fa-cog")
        ],
        bg_color="#0041A3"
    ),
    # dtc的sidebar，这里的id改不了，麻
    html.Div(id="page_content")
]

param_error = html.Div('参数错误')

app.layout = html.Div([
    dcc.Store(id='stu_id', storage_type='session'),
    dcc.Location(id='location', refresh=True),
    html.Div(id='content')
])


# 用户登录
@app.callback(
    [Output('stu_id', 'data'),
     Output('location', 'href')],
    [Input('login-submit-button', 'n_clicks')],
    [State('login-stu-id-input', 'value'),
     State('login-password-input', 'value')],
    prevent_initial_call=True
)
def update_login_state(n, stu_id, password):
    if n:
        stu_id = user.login_check(stu_id, password)
        if stu_id:
            return stu_id, '/main'
    else:
        raise PreventUpdate


# 侧边栏点击切换
@app.callback(
    Output("page_content", "children"),
    [Input("sidebar-item-1", "n_clicks_timestamp"),
     Input("sidebar-item-2", "n_clicks_timestamp"),
     Input("sidebar-item-3", "n_clicks_timestamp"),
     Input("sidebar-item-4", "n_clicks_timestamp"),
     State("stu_id", "data")])
def update_sidebar_content(input1, input2, input3, input4, stu_id):
    btn_df = pd.DataFrame({"input1": [input1], "input2": [input2], "input3": [input3], "input4": [input4]})
    btn_df = btn_df.fillna(0)
    if btn_df.idxmax(axis=1).values == "input1":
        return main
    else:
        if stu_id:
            if btn_df.idxmax(axis=1).values == "input2":
                return exercise
            if btn_df.idxmax(axis=1).values == "input3":
                return record
            if btn_df.idxmax(axis=1).values == "input4":
                return setting
        else:
            return login


# 添加跳转链接
@app.callback(
    [Output({'name': 'exercise-mode-choose-button', 'mode': 'norm'}, "href"),
     Output({'name': 'exercise-mode-choose-button', 'mode': 'exam'}, "href")],
    Input("exercise-bank-select", "value"),
    prevent_initial_call=True
)
def update_exercise_card_link(bank_id):
    search = '?bank_id=' + bank_id
    return '/exercise/norm' + search, '/exercise/exam' + search


# url路由
@app.callback(
    Output('content', "children"),
    [Input("location", "pathname"),
     Input("location", "search")],
    State("stu_id", "data"))
def url_route(pathname, search, stu_id):
    path_list = pathname.split('/')
    param_dict = {}

    def split_param_seg(seg):
        if '=' in seg:
            seg_split = seg.split('=')
            param_dict[seg_split[0]] = seg_split[1]
            return True
        else:
            return False

    if stu_id:
        if search:
            if '&' in search:
                for param_seg in search[1:].split('&'):
                    if not split_param_seg(param_seg):
                        return param_error
            else:
                if not split_param_seg(search[1:]):
                    return param_error

        if path_list[1] == "":
            return sidebar
        if path_list[1] == "main":
            return sidebar
        elif path_list[1] == "exercise":
            if len(path_list) > 2:
                mode = path_list[2]
                bank_id = param_dict.get('bank_id')
                if bank_id:
                    return html.Div(
                        children=[
                            dbc.NavbarSimple(
                                children=[
                                    dbc.NavItem(dbc.NavLink(
                                        id={'name': 'exercise-navbar-back', 'mode': mode},
                                        children='返回首页',
                                        href='/main'
                                    )),
                                ],
                                brand="ExamPool",
                                sticky='top',
                                color="#0041A3",
                                dark=True,
                            ),
                            html.Div(
                                build_exercise_config_content(mode, bank_id),
                                style={'width': '800px', 'margin': '5rem auto'}
                            )
                        ],
                    )
        return param_error
    else:
        return sidebar


def build_exercise_config_content(mode, bank_id):
    bank_info = core.get_bank_info(bank_id)
    children = [
        html.H3(
            '已选题库：{}'.format(bank_info['name']),
            className='mb-4'
        ),
        html.Div(
            [
                html.H4(
                    children='总题数：{}'.format(bank_info['count']),
                    className='mr-1'
                ),
                html.I(
                    id={'name': 'exercise-config-count-info', 'mode': mode},
                    className="fas fa-question-circle"
                ),
                dbc.Tooltip(
                    '此处可指定抽取题数≤100。若在筛选条件下，所抽取题量不足指定抽题数，则会返回所有满足筛选条件的题目。',
                    target={'name': 'exercise-config-count-info', 'mode': mode},
                    placement="left"
                ),
            ],
            className='d-flex align-items-center justify-content-between mb-4'
        )
    ]
    if bank_info:
        if mode == 'norm':
            count_detail_raw = bank_info['count_detail']
            type_list = []
            chap_list = []
            count_list = []
            for cd in count_detail_raw:
                type_list.append(core.parse_type(cd[0])[0])
                chap_list.append(cd[1])
                count_list.append(cd[2])
            count_detail = pd.DataFrame({'type': type_list, 'chap': chap_list, 'count': count_list})
            additional_children = [
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText('输入跳过题数'),
                        dbc.Input(
                            id={'name': 'exercise-config-skip', 'mode': mode},
                            type="number",
                            value=0,
                            min=0, max=bank_info['count'] - 1, step=1
                        ),
                        dbc.InputGroupText('输入抽取题数'),
                        dbc.Input(
                            id={'name': 'exercise-config-count', 'mode': mode},
                            type="number",
                            value=40,
                            min=1, max=bank_info['count'] if bank_info['count'] < 100 else 100, step=1
                        ),
                    ],
                    className='mb-4'
                ),
                html.Div(
                    [
                        html.H4('筛选题型（非必选）', className='mb-4'),
                        dcc.Dropdown(
                            id={'name': 'exercise-config-type', 'mode': mode},
                            options=[{'label': _type, 'value': _type} for _type in
                                     count_detail['type'].unique().tolist()],
                            placeholder='——请选择题型——',
                            multi=True,
                            className='mb-4'
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.H4('筛选章节（非必选）', className='mb-4'),
                        dcc.Dropdown(
                            id={'name': 'exercise-config-chap', 'mode': mode},
                            options=[{'label': chap, 'value': chap} for chap in count_detail['chap'].unique().tolist()],
                            placeholder='——请选择章节——',
                            multi=True,
                            className='mb-4'
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.H4("是否打乱", className='mb-4'),
                        dbc.RadioItems(
                            options=[
                                {"label": "是", "value": True},
                                {"label": "否", "value": False},
                            ],
                            value=True,
                            id={'name': 'exercise-config-shuffle', 'mode': mode},
                            inline=True,
                            className='mb-4'
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.H4("是否只显示收藏的题", className='mb-4'),
                        dbc.RadioItems(
                            options=[
                                {"label": "是", "value": True},
                                {"label": "否", "value": False},
                            ],
                            value=False,
                            id={'name': 'exercise-config-star', 'mode': mode},
                            inline=True,
                            className='mb-4'
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        dbc.Button(
                            id={'name': 'exercise-start-button', 'mode': mode},
                            children='开始',
                            className='mb-4'
                        )
                    ],
                    className='d-flex justify-content-end mb-4'
                )

            ]
            children += additional_children
        elif mode == 'exam':
            pass
        else:
            return param_error

        bank_info.update({'bank_id': bank_id})
        return html.Div(
            children=[
                dcc.Store(id={'name': 'exercise-bank-info', 'mode': mode}, data=bank_info),
                html.Div(
                    id={'name': 'exercise-content', 'mode': mode},
                    children=children
                )
            ]
        )
    else:
        return param_error


@app.callback(
    Output({'name': 'exercise-content', 'mode': 'norm'}, 'children'),
    Input({'name': 'exercise-start-button', 'mode': 'norm'}, 'n_clicks'),
    [State({'name': 'exercise-bank-info', 'mode': 'norm'}, 'data'),
     State({'name': 'exercise-config-skip', 'mode': 'norm'}, 'value'),
     State({'name': 'exercise-config-count', 'mode': 'norm'}, 'value'),
     State({'name': 'exercise-config-type', 'mode': 'norm'}, 'value'),
     State({'name': 'exercise-config-chap', 'mode': 'norm'}, 'value'),
     State({'name': 'exercise-config-shuffle', 'mode': 'norm'}, 'value'),
     State({'name': 'exercise-config-star', 'mode': 'norm'}, 'value'),
     State('stu_id', 'data')],
    prevent_initial_call=True
)
def update_exercise_content(n, bank_info, skip, count, type_filter, chap_filter, shuffle, star_filter, stu_id):
    if n:
        return build_exercise_content(stu_id, bank_info['bank_id'], 'norm', skip, count, type_filter, chap_filter, shuffle, star_filter)
    else:
        raise PreventUpdate


def build_exercise_content(stu_id, bank_id, mode, skip, count, type_filter, chap_filter, shuffle, star_filter):
    def build_question_div(display_id, question):
        _id = question['id']
        _type = question['type']
        star = question['star']
        children = [
            html.Div(
                [
                    html.P('{}、【{}】'.format(display_id + 1, _type)),
                    dbc.Button(
                        id={'name': 'star', 'id': _id},
                        children=[
                            html.I(
                                id={'name': 'star-icon', 'id': _id},
                                children='已收藏' if star else '收藏',
                                className="fas fa-star",
                                style={'color': '#0041A3' if star else 'black'}
                            )
                        ],
                        value=star,
                        outline=True,
                        color='#fff',
                        className='no-border-button'
                    )
                ],
                className='d-flex justify-content-between'
            ),

            html.P(question['stem'])
        ]
        if _type == '单选题' or _type == '判断题':
            children.append(
                dbc.RadioItems(
                    id={'name': 'user-answer', 'id': _id},
                    options=question['options'],
                    labelCheckedStyle={"color": "#007BFF"},
                    className='mb-1'
                )
            )
        elif _type == '多选题':
            children.append(
                dbc.Checklist(
                    id={'name': 'user-answer', 'id': _id},
                    options=question['options'],
                    labelCheckedStyle={"color": "#007BFF"},
                    className='mb-1'
                )
            )
        elif _type == '简答题':
            children.append(
                dbc.Textarea(
                    id={'name': 'user-answer', 'id': _id},
                    className='mb-1'
                )
            )
        children.append(
            html.P(
                children=[
                    html.Div(id={'name': 'answer-status', 'id': _id}, hidden=True),
                    html.Div(),
                    html.Span(
                        id={'name': 'answer-hint', 'id': _id},
                        children='答案提示',
                        style={"textDecoration": "underline", "cursor": "pointer"},
                    ),
                    dbc.Tooltip(
                        id={'name': 'answer', 'id': _id},
                        children=question['answer'],
                        target={'name': 'answer-hint', 'id': _id},
                        placement="top"
                    )
                ],
                className='d-flex justify-content-between'
            ),
        )
        return html.Div(
            id={'name': 'question', 'id': _id},
            children=children,
            className='mx-4 my-5'
        )

    if mode == 'norm':
        stars = core.get_stars(stu_id, bank_id)
        questions = core.get_questions(bank_id, shuffle, [], type_filter, chap_filter, stars, star_filter)
        length = len(questions)
        if length > skip + count:
            questions = questions[skip: skip + count]
        elif skip < length <= skip + count:
            questions = questions[skip:]
        else:
            questions = []

        questions_list = []
        for i in range(len(questions)):
            questions_list.append(build_question_div(i, questions[i]))
        if questions_list:
            return html.Div([
                dcc.Store(id={'name': 'exercise-questions', 'mode': mode}, data=questions),
                html.Div(id={'name': 'exercise-questions-list', 'mode': mode}, children=questions_list),
                html.Div(
                    id={'name': 'exercise-submit', 'mode': mode},
                    children=[
                        html.Div(
                            id='exercise-back',
                            children='刷新网页返回上一级。'
                        ),
                        dbc.Button(
                            id={'name': 'exercise-submit-button', 'mode': mode},
                            children='提交'
                        )
                    ],
                    className='d-flex align-items-center justify-content-between mb-5 mx-4'
                )
            ])
        else:
            return html.Div('无满足条件的题目')
    elif mode == 'exam':
        return html.Div('exercise_content_exam')


@app.callback(
    [Output({'name': 'exercise-submit', 'mode': 'norm'}, 'children'),
     Output({'name': 'answer-status', 'id': ALL}, 'hidden')],
    Input({'name': 'exercise-submit-button', 'mode': 'norm'}, 'n_clicks'),
    [State({'name': 'exercise-bank-info', 'mode': 'norm'}, 'data'),
     State({'name': 'exercise-questions', 'mode': 'norm'}, 'data'),
     State({'name': 'user-answer', 'id': ALL}, 'value'),
     State('stu_id', 'data')],
    prevent_initial_call=True
)
def update_exercise_submit(n, bank_info, questions, user_answer_list, stu_id):
    if n:
        res = core.store_record(bank_info['bank_id'], questions, user_answer_list, stu_id, 'norm')
        return '已提交！' if res else '提交失败。', [False for _ in range(len(questions))]
    else:
        raise PreventUpdate


@app.callback(
    Output({'name': 'answer-status', 'id': MATCH}, 'children'),
    Input({'name': 'answer-status', 'id': MATCH}, 'hidden'),
    [State({'name': 'user-answer', 'id': MATCH}, 'value'),
     State({'name': 'answer', 'id': MATCH}, 'children')],
    prevent_initial_call=True
)
def update_question_answer(hidden, user_answer, answer):
    if not hidden:
        if type(user_answer) == list:
            user_answer = sorted(user_answer)
        flag = True if user_answer == answer else False
        return dbc.Badge(
            children='正确' if flag else '错误，正确答案：{}'.format(answer),
            color="success" if flag else "danger"
        )
    else:
        raise PreventUpdate


@app.callback(
    [Output({'name': 'star-icon', 'id': MATCH}, 'style'),
     Output({'name': 'star-icon', 'id': MATCH}, 'children'),
     Output({'name': 'star', 'id': MATCH}, 'value')],
    Input({'name': 'star', 'id': MATCH}, 'n_clicks'),
    [State({'name': 'star', 'id': MATCH}, 'value'),
     State('stu_id', 'data'),
     State({'name': 'exercise-bank-info', 'mode': ALL}, 'data')],
    prevent_initial_call=True
)
def update_question_star(n, flag, stu_id, bank_info):
    if n:
        flag = not flag
        bank_id = bank_info[0]['bank_id']
        stars = core.get_stars(stu_id, bank_id)
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
        _id = json.loads(changed_id.split('.')[0])['id']
        if flag:
            stars.append(_id)
        else:
            stars.remove(_id)
        core.update_stars(json.dumps(stars, ensure_ascii=False), stu_id, bank_id)
        return {'color': '#0041A3' if flag else 'black'}, '已收藏' if flag else '收藏', flag
    else:
        raise PreventUpdate


if __name__ == "__main__":
    app.run_server(debug=False)
