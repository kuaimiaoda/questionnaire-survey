# 问卷调查 excel中产生随机结果
import random as rd
import pandas as pd
import os


# 获取桌面路径
def get_desk_p():
    return os.path.join(os.path.expanduser('~'), "Desktop")


# 单选题随机方式
def single(question, option_num):
    alp = alphabet[:option_num]
    random_answer = []
    for item in range(0, int(num)):
        random_answer.append(rd.choice(alp))
    fd[question] = pd.Series(random_answer)


# 多选题随机方式
def multiple(question, option_num):
    alp = alphabet[:option_num]
    random_answer = []
    for item in range(0, int(num)):
        lst = rd.sample(alp, rd.randint(2, option_num))
        lst.sort()
        random_answer.append(','.join(lst))
    fd[question] = pd.Series(random_answer)


# 选定题目，选项，题目类型
def questions():
    q = input('请输入问题：')  # 选定题目（作为excel列表头）
    o_n = int(input('请输入问题选项个数：'))  # 选定选项个数
    # 选定题目类型
    while True:
        question_type = input('请输入该题类型，单选题输入S，多选题输入M：')
        if question_type == 'S' or question_type == 's':
            c = 1
            break
        elif question_type == 'M' or question_type == 'm':
            c = 0
            break
        else:
            print('输入有误，请重新输入！')
    # 按题目类型执行随机生成问卷结果
    if c:
        single(q, o_n)
    else:
        multiple(q, o_n)
    # 是否继续生成其它问题随机结果
    while True:
        print('此题答案已生成！')
        print("请确认是否继续调查其它问题，输入Y/N")
        in_content = input("请输入：")
        if in_content == 'Y' or in_content == 'y':
            questions()
            break
        elif in_content == 'N' or in_content == 'n':
            print('问卷已生成至桌面！')
            break
        else:
            print('输入有误，请重新输入！')


num = input('请输入您希望生成的问卷份数：')
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
fd = pd.DataFrame()
questions()
fd.to_excel(get_desk_p() + '/questionnaire survey.xlsx', index=False)
