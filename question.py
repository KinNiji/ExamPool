import datetime
import json
import re
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

from mysql import insert_record, select


class Pre:

    @staticmethod
    def chaoxing_crawler():
        service = Service('lib/chromedriver.exe')

        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        # 设置隐式等待为3s
        driver.implicitly_wait(3)

        url_init = 'https://mooc1.chaoxing.com/mycourse/studentstudy?' \
                   'chapterId=197463575&' \
                   'courseId=206450119&' \
                   'clazzid=42484255&' \
                   'enc=909c1fbbf88d95706f37fc589a3df97e&' \
                   'mooc2=1&' \
                   'cpi=114063416&' \
                   'openc=f3cfa7dad19f9b6030c75e4622309cf6'

        # 登录
        with open('config/accounts.json') as f_accounts:
            accounts = json.load(f_accounts)
        phone, password = None, None
        for account in accounts:
            if account['platform'] == 'chaoxing':
                phone = account['info']['phone']
                password = account['info']['password']
                break
        if phone and password:
            driver.get(url_init)
            driver.find_element(By.CSS_SELECTOR, '#phone').send_keys(phone)
            driver.find_element(By.CSS_SELECTOR, '#pwd').send_keys(password)
            driver.find_element(By.CSS_SELECTOR, '#loginBtn').click()
        else:
            raise Exception('账号信息缺失')

        # 定位本章测验，穿过3层iframe获取指定章节内容
        driver.get(url_init)
        chaps = driver.find_elements(By.XPATH, '//*[@title="本章测验"]')
        for chap in chaps:
            ajax = chap.get_attribute('onclick')
            if ajax:
                # 没实现自动滚动右侧边栏，运行的时候要手动滚动一下，保证页面显示下一章节
                # ActionChains(driver).move_to_element(chap).perform()
                # chap.send_keys(Keys.PAGE_DOWN)
                chap.click()
                driver.switch_to.frame('iframe')
                middle_iframe = driver.find_element(By.TAG_NAME, 'iframe')
                driver.switch_to.frame(middle_iframe)
                driver.switch_to.frame('frame_content')

                ce_yan = driver.find_element(By.CSS_SELECTOR, '#RightCon > div > div.CeYan')
                chapter_name = ce_yan.find_element(By.CSS_SELECTOR, 'h3')
                questions = ce_yan.find_elements(By.CSS_SELECTOR, '#ZyBottom > div.TiMu')

                with open('question_bank/mao_theories/all.txt', 'a', encoding='utf-8') as f:
                    print(chapter_name.text.strip())
                    f.write(chapter_name.text.strip())

                    question_dict_list = []
                    for question in questions:
                        question_dict = {}

                        stem = question.find_element(By.CSS_SELECTOR, 'div.clearfix').text
                        print(stem.strip())
                        question_dict['stem'] = stem.strip()

                        try:
                            option_list = []
                            options = question.find_elements(By.CSS_SELECTOR, 'ul.Zy_ulTop > li')
                            for option in options:
                                print(option.text.strip())
                                option_list.append(option.text.strip())
                            question_dict['options'] = option_list
                        except StaleElementReferenceException:
                            print('无选项')
                            question_dict['options'] = None

                        answer = question.find_element(By.CSS_SELECTOR, 'div.Py_answer').text
                        print(answer.strip())
                        question_dict['answer'] = answer.strip()

                        question_dict_list.append(question_dict)
                    f.write(json.dumps(question_dict_list, indent=2, ensure_ascii=False))

                    print()
                    driver.switch_to.parent_frame()
                    driver.switch_to.parent_frame()
                    driver.switch_to.parent_frame()
            else:
                continue

    @staticmethod
    def chaoxing_process(file):
        def type_mapping(type_str, option_len):
            if type_str == '【单选题】':
                return 'S' + option_len
            elif type_str == '【多选题】':
                return 'M' + option_len
            else:
                return None

        with open(file, 'r', encoding='utf-8') as f:
            raw = json.load(f)
        for chap, questions in raw.items():
            print(chap)
            for question in questions:
                stem_raw = question['stem']
                options_raw = question['options']
                answer_raw = question['answer']

                options = []
                for option_raw in options_raw:
                    options.append(option_raw.split('\n')[1])

                stem_raw_split = stem_raw.split('\n')
                type_raw = stem_raw_split[1]
                stem = stem_raw_split[2].strip()

                type_id = type_mapping(type_raw, str(len(options)))

                answer = None
                if type_id:
                    pattern = r'：(.*)我'
                    answer_seg = re.findall(pattern, answer_raw)
                    if answer_seg:
                        answer = answer_seg[0].strip()
                else:
                    answer = answer_raw.split('\n')[1].strip()

                print(chap, type_id, stem, answer)
                if type_id is not None:
                    print(options)

                insert_record('question', {'bank_id': 1002,
                                           'chap': chap,
                                           'stem': stem,
                                           'options': json.dumps(options, ensure_ascii=False) if options else None,
                                           'answer': answer,
                                           'type': type_id if type_id else 'JD'})
            print()

    @staticmethod
    def text_process():
        with open('question_bank/mao_theories/毛概题库.txt', 'r', encoding='utf-8') as f:
            file_raw = f.read()
        # [(一、单选题)(二、多选题)(三、是非题)(四、论述题)]
        raw_split = file_raw.split('四、论述题')
        jd_raw = raw_split[1]
        raw_split = raw_split[0].split('三、是非题')
        pd_raw = raw_split[1]
        raw_split = raw_split[0].split('二、多选题')
        multiple_raw = raw_split[1]
        raw_split = raw_split[0].split('一、单选题')
        singles_raw = raw_split[1]

        raw_dict = {'S4': singles_raw, 'M4': multiple_raw, 'PD': pd_raw, 'JD': jd_raw}
        for _type, type_raw in raw_dict.items():
            raw = type_raw.split('\n')[1:]
            if _type == 'S4' or _type == 'M4':
                for i in range(int(len(raw) / 6)):
                    stem = raw[6 * i].split('.')[1].strip().replace('（', '(').replace('）', ')').replace(' ', '').replace('　', '')
                    options = [option.strip().split('.')[1] for option in raw[6 * i + 1: 6 * i + 1 + 4]]
                    answer = raw[6 * i + 5].split('：')[1].strip()
                    # print(stem)
                    # print(options)
                    # print(answer)
                    insert_record('question', {'bank_id': 1003,
                                               'chap': '概论题库',
                                               'stem': stem,
                                               'options': json.dumps(options, ensure_ascii=False),
                                               'answer': answer,
                                               'type': _type})
            elif _type == 'PD':
                for i in range(int(len(raw) / 2)):
                    stem = raw[2 * i].split('.')[1].strip()
                    answer = {'√': 'T', '×': 'F'}[raw[2 * i + 1].split('：')[1].strip()]
                    # print(stem)
                    # print(answer)
                    insert_record('question', {'bank_id': 1003,
                                               'chap': '概论题库',
                                               'stem': stem,
                                               'answer': answer,
                                               'type': _type})


class Core:
    def __init__(self):
        self.opt_list = [char for char in 'ABCDEFGHIJ']

    def shuffle_mapping(self, questions, user_choices):
        mapped_choices = {}
        for _id, choice in user_choices.items():
            shuffled_opt_list = questions[int(_id) - 1]['shuffled_opt_list']
            mapped_choice = []
            for c in choice:
                mapped_choice.append(self.opt_list[shuffled_opt_list.index(c)])
            _id = questions[int(_id) - 1]['id']
            mapped_choices[_id] = mapped_choice
        return mapped_choices

    @staticmethod
    def parse_type(type_info):
        pre = type_info[0]
        tail = type_info[1]
        if pre == 'S':
            return ['单选题', int(tail)]
        elif pre == 'M':
            return ['多选题', int(tail)]
        elif pre == 'P':
            return ['判断题', 2]
        elif pre == 'J':
            return ['简答题', 0]

    def get_questions(self, bank_id, shuffle, wrong_filter, type_filter, chap_filter, stars, star_filter):
        questions = []
        sql = 'select * from question where bank_id=%s'
        if chap_filter:
            sql += ' having `chap` in {}'.format("('{}')".format(chap_filter[0]) if len(chap_filter) == 1 else str(tuple(chap_filter)))

        bank = select(sql, bank_id)
        _id = 1
        for line in bank:
            options = json.loads(line[4]) if line[4] else None
            answer = line[5]
            parsed = self.parse_type(line[6])
            _type, option_count = parsed[0], parsed[1]

            format_options = None
            shuffled_opt_list = None
            format_answer = answer
            if _type == '单选题' or _type == '多选题':
                shuffled_opt_list = self.opt_list.copy()[:option_count]
                if shuffle:
                    random.shuffle(shuffled_opt_list)
                format_options = [
                    {
                        'label': '{}、{}'.format(self.opt_list[i], options[shuffled_opt_list.index(self.opt_list[i])]),
                        'value': self.opt_list[i]
                    } for i in range(option_count)
                ]
                format_answer = sorted([shuffled_opt_list[self.opt_list.index(ans)] for ans in answer])
                if _type == '单选题':
                    format_answer = format_answer[0]
            elif _type == '判断题':
                format_options = [{'label': '正确', 'value': 'T'}, {'label': '错误', 'value': 'F'}]

            question = dict(
                id=_id,
                chap=line[2],
                stem=line[3],
                options=format_options,
                shuffled_opt_list=shuffled_opt_list,
                answer=format_answer,
                type=_type,
                star=True if _id in stars else False
            )
            questions.append(question)
            if type_filter:
                if _type not in type_filter:
                    questions.remove(question)
            if wrong_filter:
                if _id not in wrong_filter:
                    questions.remove(question)
            if star_filter:
                if not question['star']:
                    questions.remove(question)
            _id += 1

        if shuffle:
            random.shuffle(questions)
        return questions

    @staticmethod
    def get_banks():
        res = select('select * from bank')
        banks = []
        if res:
            for row in res:
                banks.append({'label': row[2] + ' ' + row[1], 'value': row[0]})
            banks = sorted(banks, key=lambda b: b['label'], reverse=True)
        return banks

    @staticmethod
    def get_bank_info(bank_id):
        bank_info = {}
        res1 = select('select name from bank where bank_id=%s', bank_id)
        if res1:
            bank_info['name'] = res1[0][0]

        res2 = select('select count(question_id) from question where bank_id=%s', bank_id)
        if res2:
            bank_info['count'] = res2[0][0]

        res3 = select(
            'SELECT `type`,`chap`,COUNT(question_id) FROM question WHERE bank_id=%s GROUP BY `type`,`chap`',
            bank_id
        )
        if res3:
            count_detail = []
            for r in res3:
                count_detail.append([r[0], r[1], r[2]])
            bank_info['count_detail'] = count_detail

        return bank_info

    @staticmethod
    def get_wrongs(stu_id, bank_id):
        res = select('select wrong from record where stu_id=%s and bank_id=%s', stu_id, bank_id)
        wrongs = []
        if res:
            for row in res:
                wrongs += json.loads(row[0])
        return sorted(list(set(wrongs)))

    @staticmethod
    def get_stars(stu_id, bank_id):
        res = select('select `index` from star where stu_id=%s and bank_id=%s', stu_id, bank_id)
        index = []
        if res:
            index = json.loads(res[0][0])
        else:
            insert_record('star', {'stu_id': stu_id, 'bank_id': bank_id, '`index`': json.dumps([])})
        return index

    @staticmethod
    def update_stars(stars, stu_id, bank_id):
        return select('update star set `index`=%s where stu_id=%s and bank_id=%s', stars, stu_id, bank_id)

    @staticmethod
    def store_record(bank_id, questions, user_answer_list, stu_id, mode):
        user_answer_dict = {}
        wrong = []
        # wrong_display = []
        for i in range(len(user_answer_list)):
            user_answer = user_answer_list[i]
            if type(user_answer) == list:
                user_answer = sorted(user_answer)

            if user_answer:
                _id = questions[i]['id']
                user_answer_dict[_id] = user_answer
                if user_answer != questions[i]['answer'] and questions[i]['type'] != '简答题':
                    print(_id, user_answer, questions[i]['answer'])
                    wrong.append(_id)
                    # wrong_display.append(i)

        res = insert_record(
            'record',
            {'stu_id': stu_id,
             'time': datetime.datetime.now(),
             'bank_id': bank_id,
             'mode': mode,
             'record': json.dumps(user_answer_dict, ensure_ascii=False),
             'wrong': json.dumps(wrong, ensure_ascii=False)}
        )
        return res


if __name__ == '__main__':
    core = Core()
    print(core.get_bank_info('1003'))
