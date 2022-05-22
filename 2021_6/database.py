# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:21:45 2021

@author: Niji
"""

import re
import pymysql

conn = pymysql.connect(host='localhost', port = 3307, user = "root", passwd = "123456", db = "exampool")
cur = conn.cursor()

query = 'insert into modern_history values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'

with open("./question_bank/modern_history/all.txt", "r", encoding='utf-8') as f:
    raw_data = f.read()
    chaps = re.split('(?:第[一二三四五六七八九十]+章)', raw_data)[1:]
    
    try:
        _id = 1
        for i in range(len(chaps)):
            chap = chaps[i]
            lines = chap.split('\n')[1:]
            questions = []
            for num in range(int(len(lines)/5)):
                questions.append(lines[5*num:5*num+5])
            
            for question in questions:
                _chap = i + 1
                
                stem_and_answer = re.match('(.*)\(([ABCD])\)', question[0])
                
                _stem = stem_and_answer.group(1)
                _answer = stem_and_answer.group(2)
                _type = 'Single4'
                _A = re.match('[ABCD][.、](.*)', question[1]).group(1)
                _B = re.match('[ABCD][.、](.*)', question[2]).group(1)
                _C = re.match('[ABCD][.、](.*)', question[3]).group(1)
                _D = re.match('[ABCD][.、](.*)', question[4]).group(1)
                
                cur.execute(query, (_id, _chap, _stem, _A, _B, _C, _D, _answer, _type))
                _id = _id + 1
                # print('question', _id, 'success!')
                
            print('chap', _chap, 'success!')
            
        conn.commit()
        print('all success!')
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        

