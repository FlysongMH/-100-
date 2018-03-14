'''题目：输入某年某月某日，判断这一天是这一年的第几天？'''

if __name__ == '__main__':

    year  = int(input('请输入年：'))
    month = int(input('请输入月：'))
    day   = int(input('请输入日：'))

    DaysOfMonth = [(0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
                   (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)]

    specialyear = (year%400==0) or (year%4==0 and year%100!=0)
    sumday=day
    for i in range(0,month):
        sumday+=DaysOfMonth[specialyear][i]

    print('it is the %dth day.' % sumday)