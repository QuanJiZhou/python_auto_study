# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         hw03
# Description:
# 要求使用同乐老师讲的Python 自动化办公课程中的租房信息数据 house.xlsx，进行统计和计算：
# 1、统计出面积小于60平米的房子有多少个？
# 2、统计面积小于60平米的房子的平均租金?
# 3、统计出租金大于5千小于1万的房子有多少个？
# 4、统计标签中采光好并且 租金大于5千小于1万的房子有多少个？
# 5、统计统计标签中采光好并且 租金大于5千小于1万的房子的平均租金是多少？
# 6、通过requests、bs4 获取http://www.ztloo.com/sum_number.html 网页中所有数字，并计算出他们相加之后的总和.
# 7、获取同乐学堂首页热门标签内容，装载在字典中，并打印输出。例如：{‘mysql’:198,'python'：69}
# 8、获取标签为python 文章的，前三篇文章的，发布日期装进列表，打印输出。
# Author:       ZYT
# Date:         2021-8-18
#-------------------------------------------------------------------------------
import pandas as pd
import os

file_path = os.getcwd() + "\house.xlsx"
print(">>数据源文件路径："+file_path)
houses = pd.read_excel(file_path)

if __name__ == '__main__':

    # 将面积\房租进行格式转化
    houses["面积"] = houses.面积.str.split('㎡', expand=True)[0].astype("float")
    houses["房租"] = houses.房租.str.split('元', expand=True)[0].astype("int")


    houses_less_60 = houses[houses.面积 < 60]
    print("1. 面积小于60平米的房子有 %d 个" % int(houses_less_60.shape[0]))
    print("2. 面积小于60平米的房子的平均租金为 %.2f 元" % houses_less_60.房租.mean())

    houses_m5000_l10000 = houses[houses["房租"].between(5000, 10000)]
    print("3. 租金大于5千小于1万的房子有 %d 个" % len(houses_m5000_l10000))

    houses["采光好"] = 1 if  houses.标签.str.find('采光好') >0 else 0
    print(houses["采光好"])