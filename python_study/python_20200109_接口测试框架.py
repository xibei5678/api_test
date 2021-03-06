#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20200109_接口测试框架.py
@Date  : 2020/1/9 0009 16:58
@Author: xibei
'''

''' 接口自动化框架 '''

# 1. 学习接口自动化框架之前需要了解的问题

#   1）什么是接口：模块与模块之间，系统与系统之间交互的方式
#      接口类型：根据协议划分：http、webservice、socket等
#      http类型的接口请求方式：get、post、put、delete等

#   2）做接口测试的方式：工具（postman、jmeter、soapui）、代码
#     用代码的优点：更灵活，对于工作中的特殊需求能更好的完成
#     开始代码自动化的时间：项目已基本稳定时，项目前期使用工具更快更好的完成测试工作
#     版本迭代过于频繁：根据测试计划，先实现一部分优先核心的接口，再实现全部
#     接口重构是否适用：适用（重构：重新构造功能代码，换一种方式实现功能（代码优化，接口规则、地址不会变））
#
#   3）接口自动化的特点：输入传参，检验出参的过程（传入输入，检查输出）
#      接口自动化的实质：使用代码的方式进行功能测试
#      接口自动跟手工对比：自动化不会出现执行遗漏等情况

# 2. 接口自动化测试
#   1） 设计测试用例：根据设计方法加设计要素进行编写测试用例
#       设计方法：等价类划分法、边界值分析法、因果图判断法、场景法（与功能测试相同）
#       设计要素：功能、逻辑、异常、安全

#   2）代码书写规则：可读性(1.好的命名规范；2.写注释)
#                  可维护性(case的独立性，一个接口一个py文件；点对点、端对端)
#                  可扩展性（case的可迁移性、case的可重用性）
#                  高性能性（ case的效率）
#
#   3）如何管理测试数据：
#                基础数据：（每个case都需要用的数据）放在配置文件
#                测试数据：放在excel
#                临时数据：只在一个case中需要用到，直接写在脚本中


'''迁移环境'''

#  (原环境)导出所有第三方库的版本：pip freeze > requirements.txt
# （新环境）安装所有包：pip install requirements.txt
