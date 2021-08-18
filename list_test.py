# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         list_test
# Description:
# Author:       HP
# Date:         2021-8-16
#-------------------------------------------------------------------------------
# Created time : 2021/6/27
# Author : Jiudan
# 1.打印
print('打印列表的方法'.center(60, '-'))
webList = ['Baidu', 'Google', 'Taobao', 'Tencent']
print(webList)
print(webList[1])
print(webList[-1])
print(webList[1:3])
print(webList[1:])
# 打印附带下标
for i, v in enumerate(webList):
    print(i, v)

# 2.查
print('查找列表的方法'.center(20, '-'))
webList = ['Baidu', 'Google', 'Taobao', 'Tencent', 'Baidu']
print(webList.index('Baidu'))  # 打印'Baidu'的下标index

# 3.增
print('增加列表的方法'.center(20, '-'))
webList = ['Baidu', 'Google', 'Taobao', 'Tencent']
webList.append('Weibo')  # 在末尾追加一个新的元素
webList.insert(3, 'Iqiyi')  # 在指定位置插入一个新的元素
print(webList)

# 4.改
print('修改列表的方法'.center(20, '-'))
webList = ['Baidu', 'Google', 'Taobao', 'Tencent']
webList[2] = 'Weibo'
print(webList)
webList.reverse()  # 将列表反转 #reverse：反转
print(webList)

# 5.删
print('删除列表的方法'.center(20, '-'))
webList = ['Baidu', 'Google', 'Taobao', 'Tencent']
webList.remove('Google')
print(webList)
del webList[2]
print(webList)
webList.pop(1)  # 根据索引删除元素，删除不存在的元素时会报错
print(webList)
webList.clear()  # 删除整个列表
print(webList)

# 6.计数
print('计数'.center(20, '-'))
webList = ['jiudan', 'jiudan', 'Jiudan', 'color']
print(webList.count('jiudan'))

# 7.排序
print('排序'.center(20, '-'))
list = [1, 5, 9, 6, 4, 3]
list.sort()
print('升序排列：', list)
list.sort(reverse=True)
print('降序排列：', list)
# 进阶
list_str = ['A', 'b', 'C', 'j']
list_str.sort()
print('区分大小写升序排列：', list_str)  # 默认区分大小写
list_str.sort(reverse=True)
print('区分大小写降序排列：', list_str)  # 默认区分大小写
list_str.sort(key=str.lower)
print('不区分大小写升序排列：', list_str)  # 不区分大小写,升序排列
list_str.sort(key=str.lower, reverse=True)
print('不区分大小写降序排列：', list_str)  # 不区分大小写,降序排列

# 8.列表的拓展
print('列表的拓展'.center(20, '-'))
webList1 = ['Baidu', 'Google', 'Taobao', 'Tencent']
webList2 = ['Weibo', 'Iqiyi', 'Zhihu']
webList1.extend(webList2)  # 拓展列表，将两个列表内容合并
print(webList1, webList2)  # 但不会清除webList2列表

# 9.列表的浅copy
print('列表的浅copy'.center(20, '-'))
webList1 = ['Baidu', 'Google', 'Taobao', 'Tencent']
webList2 = webList1.copy()
webList1[2] = 'Weibo'
print(webList1)
print(webList2)

# 10.列表的深copy
print('列表的深copy'.center(20, '-'))
import copy  # 导入copy库

list1 = ['1', '2', '3', ['4', '5', '6'], '7', '8']
list2 = copy.deepcopy(list1)
list1[1] = '二'
list1[3][1] = '五'
print(list1)
print(list2)  # 深复制


#-----------------------------------
a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
