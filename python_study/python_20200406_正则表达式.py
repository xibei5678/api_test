# -*- coding: utf-8 -*-
# @Time : 2020/4/6 21:52
# @Author : xibei
# @filename : python_20200406_正则表达式.py
# @description ：正则表达式的学习以及在python中的使用

'''正则表达式'''

# 1. 一种字符串匹配的模式（pattern），可以用来检查一串是否含有某种子串、将匹配的子串替换或者从某个串中取出符合某个条件的子串等。

# 2.常用字符：
#  $	匹配输入字符串的结尾位置。
# ( )	标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。
#  *	匹配前面的子表达式零次或多次。
#  +	匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+。
#  .	匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。
#  [	标记一个中括号表达式的开始。要匹配 [，请使用 \[。
#  ?	匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。
#  \	将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符。
#  ^	匹配输入字符串的开始位置，除非在方括号表达式中使用，当该符号在方括号表达式中使用时，表示不接受该方括号表达式中的字符集合。
#  {	标记限定符表达式的开始。
#  |	指明两项之间的一个选择。

# 3.运算优先级
#   \	转义符
#   (), (?:), (?=), []	圆括号和方括号
#   *, +, ?, {n}, {n,}, {n,m}	限定符
#   ^, $, \任何元字符、任何字符	定位点和序列（即：位置和顺序）
#   |	替换，"或"操作， 字符具有高于替换运算符的优先级，使得"m|food"匹配"m"或"food"。
#       若要匹配"mood"或"food"，请使用括号创建子表达式，从而产生"(m|f)ood"。

# 4.示例
# 1、匹配整数或者小数（包括正数和负数）
#
# 　　-?\d+(\.\d+)?

# 　　　　-?表示-匹配0次或一次,\d表示整数,+表示匹配一次或多次,(\.\d+)?表示小数

# 2、匹配年月日日期 格式2018-12-6
#
# 　　^[1-9]\d{0,3}-(1[0-2]|0?[1-9])-(3[01]|[12]\d|0?[1-9])$
#
# 　　　　1.^[1-9]表示年是以数字1-9开头的,\d{0,3}表示年的位数,^[1-9]\d{0,3}就表示1-9999年之间
#
# 　　　　2.(1[0-2]|0?[1-9])中|前面的1[0-2]表示从10到12,后面的0?[1-9]表示01-09或者1-9,
#
# 　　　　　　(1[0-2]|0?[1-9])表示月,01-12或者1-12
#
# 　　　　3.(3[01]|[12]\d|0?[1-9])$其中3[01]表示30或31,[12]\d表示从10-29,最后的0?[1-9]表示从
#
# 　　　　　　01-09或者是从1-9.整体就表示从01-31或者1-31
#
# 3、匹配qq号
#
# 　　[1-9]\d{4,11}
#
# 　　　　表示5位到12位qq.第一位为非0
#
# 4、11位的电话号码
#
# 　　1[3-9]\d{9}
#
# 　　　　第一位数字为1,第二位为3-9,后面随便9位数




'''python中操作正则表达式的re模块'''

# 1. re模块，python自带模块，通过正则表达式是用来匹配处理字符串的
# 2.常用模块方法：

''' match()函数'''
#
# match，从头匹配一个符合规则的字符串，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
# match(pattern, string, flags=0)
# # pattern： 正则模型
# # string ： 要匹配的字符串
# # falgs ： 匹配模式

import  re

str = "hello egon bcd egon lge egon acd 19"
patter = "\w+"
# patter = "e\w+"   # 未从起始位置开始，匹配失败，返回none
res = re.match(pattern=patter, string=str)
# print(res)


''' search()函数'''
# search,浏览全部字符串，匹配第一符合规则的字符串，浏览整个字符串去匹配第一个，未匹配成功返回None
# search(pattern, string, flags=0)
# # pattern： 正则模型
# # string ： 要匹配的字符串
# # falgs ： 匹配模式

patter_01 = "eg\w+"
res_01 = re.search(pattern=patter_01, string=str)
# print(res_01)

patter_02 = "(eg)(\w+)"
res_02 = re.search(pattern=patter_02, string=str)
# print(res_02)  # 返回对象
# print(res_02.group())  # 全匹配  # egon
# print(res_02.group(1))  # 匹配第一个分组的字符  # eg
# print(res_02.group(2))  # 匹配第二个分组的字符  # on



'''findall()函数'''
# 浏览全部字符串，匹配所有合规则的字符串，匹配到的字符串放到一个列表中，未匹配成功返回空列表
# findall(pattern, string, flags=0)
# # pattern： 正则模型
# # string ： 要匹配的字符串
# # falgs ： 匹配模式
# 注意：一旦匹配成，再次匹配，是从前一次匹配成功的，后面一位开始的，也可以理解为匹配成功的字符串，不在参与下次匹配

# 无分组
r = re.findall("\d+\w\d+", "a2b3c4d5")  # 浏览全部字符串，匹配所有合规则的字符串，匹配到的字符串方到一个列表中
print(r)
# ['2b3', '4d5'] #匹配成功的字符串，不再参与下次匹配，所以3c4也符合规则但是没有匹配到

# 有分组：只将匹配到的字符串里，组的部分放到列表里返回，相当于groups()方法
r_1 = re.findall("a(\w+)", "ca2b3 caa4d5") #有分组：只将匹配到的字符串里，组的部分放到列表里返回
print(r_1)
# ['2b3', 'a4d5'] # 返回匹配到组里的内容返回

# 多个分组：只将匹配到的字符串里，组的部分放到一个元组中，最后将所有元组放到一个列表里返回
r_2 = re.findall("(a)(\w+)", "ca2b3 caa4d5")  # 有多分组：只将匹配到的字符串里，组的部分放到一个元组中，最后将所有元组放到一个列表里返回
print(r_2)
# [('a', '2b3'), ('a', 'a4d5')] # 返回的是多维数组




''' sub()函数 '''
#
# 替换匹配成功的指定位置字符串
#
# sub(pattern, repl, string, count=0, flags=0)
#
# # pattern： 正则模型
# # repl   ： 要替换的字符串
# # string ： 要匹配的字符串
# # count  ： 指定匹配个数
# # flags  ： 匹配模式

r_sub = re.sub("a\w", "替换", "sdfadfdfadsfsfafsff")
print(r_sub)
# sdf替换fdf替换sfsf替换sff


'''subn()函数'''

# 替换匹配成功的指定位置字符串,并且返回替换次数，可以用两个变量分别接受

# subn(pattern, repl, string, count=0, flags=0)

# pattern： 正则模型
# repl   ： 要替换的字符串
# string ： 要匹配的字符串
# count  ： 指定匹配个数
# flags  ： 匹配模式

a, b = re.subn("a\w", "替换", "sdfadfdfadsfsfafsff")  # 替换匹配成功的指定位置字符串,并且返回替换次数，可以用两个变量分别接受
print(a)  # 返回替换后的字符串
print(b)  # 返回替换次数