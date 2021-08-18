# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         hw02
# Description: Python 语法基础程序设计实训作业
# Author:       ZYT
# Date:         2021-8-14
# 1、使用Python 将下列四个变量year、month、day 、many_year拼接到不完整text的字符串当中，实现输出完整形式为“2021年7月1号是中国共产党成立100周年。“   year = 2021、month =7 、day = 1、many_year = 100    text = "年月号是中国共产党成立周年。"
# 2、来找出 a 列表中 [0,-1,2,-10,9,5] 列表中小于5的数字，并装进b 列表，并把b 列表排好序进行打印输出。
# 3、使用Python 的While 循环技术计算出投资的年利率为7.8%，试求从2万块增长到8万块，需要花费多少年 以及打印出投资两年后的收益。
# 4、现有同乐学堂博客中2021年07月10号的 web系统访问日志（apache_byu4034710001_20210710.log），需要读取log日志文件，并且过滤出里面的IP地址。把文件中的所有ip装载到列表中，对列表中的ip 进行去重, 并统计出7月10号有多少个用户访问同乐学堂。
# 去重提示：可以使用set 数据结构，例如 ：set([1,2,3,4,5,3]) 的功能是去除列表中的重复数字3
# 提取IP地址正则：regex = r'\d+\.\d+\.\d+\.\d+'
# 获取列表的长度函数：len
#-------------------------------------------------------------------------------

import re


def increase():
    n = 0
    while True:
        n = n+1
        yield n


def question_split_line(line):
    print(('※ Answer For Question %d ' % next(line)).center(160,'-'))


# 1、第一题考察 字符串拼接能力,
def question1():
    year = 2021
    month = 7
    day = 1
    many_year = 100
    text = "年月号是中国共产党成立周年。"

    list_text = list(text)
    list_text.insert(list_text.index('年'), str(year))
    list_text.insert(list_text.index('月'), str(month))
    list_text.insert(list_text.index('号'), str(day))
    list_text.insert(list_text.index('周'), str(many_year))
    print("".join(list_text))


# 2、第二题考察列表操作、for循环遍历列表、逻辑判断的知识点的结合。
def question2():
    a = [0, -1, 2, -10, 9, 5]
    b = []
    for i in a :
        if i < 5:
            b.append(i)
    b.sort()
    print(b)


def income(money:float):
    return money*rate+money


def get_income_by_years(capital: float, years: int):
    '''
    年计收入
    :param capital:本金
    :param years: 投资期
    :return: 总收益
    '''
    your_income = capital
    while years > 0:
        your_income = income(your_income)
        years -= 1
    return your_income


def get_dest_income_for_year(capital: float, total_income: float):
    '''
    计算一定本金，按利率复利多少年可达到预期值
    :param capital: 本金
    :param total_income:目标收入
    :return: 预计投资期
    '''
    result_years = 0
    current_money = capital
    while current_money < total_income:
        result_years += 1
        current_money = income(current_money)
    return result_years


# 3.第三题考察python 的while 循环技术，结合数学计算，解决生活中投资理财问题。
def question3():
    total_income = 80000     # 目标收入
    your_capital = 20000    # 本金

    global rate
    rate = 0.078    # 当前利率

    print('【复利计息】')
    print('从 %d 块增长到 %d 块，需要花费 %d 年 ' % (your_capital, total_income,
                                         get_dest_income_for_year(your_capital, total_income)))
    print('投资两年后的收益为： %s' % str(get_income_by_years(your_capital, 2)))


# 4、第四题实际项目问题，使用Python 对网站日志文件，进行读取，正则匹配，数据去重。
def question4():
    # 读日志文件
    log_path = r"apache_byu4034710001_20210710.log"
    with open(log_path, 'r', encoding='gbk') as f:
        txt = f.read()
    # regx_ip2 = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    # result2 = re.findall(regx_ip2, txt)
    # set_ips2 = set(result2)
    regx_ip = r"\d+\.\d+\.\d+\.\d+"
    result = re.findall(regx_ip, txt)
    set_ips = set(result)
    # print(set_ips-set_ips2)
    print("去重后的ip如下：")
    print(set_ips)
    print("共 %d 个用户访问同乐学堂" % len(set_ips))



if __name__ == '__main__':
    line = increase()
    question_split_line(line)
    question1()
    question_split_line(line)
    question2()
    question_split_line(line)
    question3()
    question_split_line(line)
    question4()
