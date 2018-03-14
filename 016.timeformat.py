'''题目：输出指定格式的日期。'''

import time

'''
时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。
太遥远的日期也不行，UNIX和Windows只支持到2038年。
'''

# # 打印时间戳
# print("time.time():\n", time.time())
#
# # 从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
# print("time.localtime :\n", time.localtime(time.time()))
#
# # 你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
# print("time.asctime( time.localtime(time.time())) :\n", time.asctime( time.localtime(time.time())))
#
# # 格式化日期
# # 格式化成2016-03-20 11:45:39形式
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))
# # 将格式字符串转换为时间戳
# a = "Sat Mar 03 20:34:37 2018"
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))) #注意不是一个函数strptime

import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

#
# import datetime
# # 输出今日日期
# print(datetime.date.today().strftime('%d/%m/%Y'))
#
# # 创建日期对象
# Mybirth = datetime.date(1990,12,30)
# print('默认日期格式：', Mybirth)
# print('日期格式"日/月/年"', Mybirth.strftime('%d/%m/%Y'))
#
# # 日期算术运算
# MybirthNextDay = Mybirth + datetime.timedelta(days=1)
# print('默认日期格式：', MybirthNextDay)
# print('日期格式dmy：',MybirthNextDay.strftime('%d/%m/%Y'))
#
# # 日期替换
