#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python常用数据类型_元组.py
@Date  : 2019/10/29 0029 16:24
@Author: xibei
'''


''' 元组 tuple（）'''  # 有序不可变

# t = ()
# print(type(t))
#
# t_1 = (1,)
# print(type(t_1))
#
# t_2 = (1)
# print(type(t_2))

'''
# 1: 可以有空元组
# 2：如果只有一个数据， 需要加一个逗号 不然就会变成非元组
# 3：元组内什么类型的数据都可以放
# 4： 取单个元素 元组名[索引值]   索引从0开始
# 5: 支持切片，同字符串操作
# 6： 元组中还可以嵌套放元组
'''

# t_3 = ([1, 2], (1, 2, 3))
# print(len(t_3))
# print(t_3[1])
# print(t_3[1][1])


''' 注意点 '''
# 元组中的值不能修改 如增删改全不可以用

'''常用函数'''
# t.count() # 统计字符或字符串的个数 用法同字符串
# t.index() # 查找字符或字符串的索引 用法同字符串

t_4 = (1, 2, 3, 4, 5, 6, 1, 5, 1, 2)
print(t_4.count(1))
print(t_4.index(2))

t_5 = ((1, 2, 3), (1, 2, 3), 4, 5, 6, 1, 5, 1, 2)
print(t_5.count(1))
print(t_5.index(2))
print(t_5.index((1, 2, 3)))
print(t_5.count((1, 2, 3)))
