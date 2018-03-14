
'''题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''

def fun01():
    heighti  = 100.0
    heightList = []
    TourList = []
    Total = 0
    for i in range(10):
        # 落地下降距离
        Total += heighti
        # 反弹距离
        heighti /= 2
        heightList.append(heighti)
        TourList.append(Total)
        # 落地上升新增距离
        Total += heighti



    print(TourList)
    print(heightList)

def fun02():
    tour = []
    height = []

    hei = 100.0  # 起始高度
    tim = 10  # 次数

    for i in range(1, tim + 1):
        # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
        if i == 1:
            tour.append(hei)
        else:
            tour.append(2 * hei)
        hei /= 2
        height.append(hei)

    print('每次落地新增距离：tour = {0}'.format(tour))
    print('总高度：tour = {0}'.format(sum(tour)))
    print('反弹高度 = {0}'.format(height))

if __name__ == '__main__':
    print('fun01:')
    fun01()
    print('fun02:')
    fun02()