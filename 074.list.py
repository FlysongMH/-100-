import random

def fun01():

    ptr = []
    for i in range(10):
        ptr.append(random.randrange(0,10))

    print('原始列表1为：', ptr)

    ptr.reverse()   # 反向输出一个列表
    print('逆序列表1为：', ptr)

    ptr.sort()   # 排序
    print('正向排序列表1：', ptr)

    ptr2 = [random.randrange(0,10) for i in range(5)]
    print('另一个列表2：', ptr2)

    print('合并列表2和列表1：', ptr+ptr2)

    ptr.extend(ptr2)
    print('合并列表2到列表1：', ptr)

    print('列表1：', ptr)
    print('列表2：', ptr2)


if __name__ == '__main__':
    fun01()