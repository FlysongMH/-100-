'''题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。'''
'''
分析：输入的奇数odd，满足存在一个整数m使得，odd*m = 10**n-1
n即为9的个数，且为正数。
题目不是一定有解的
'''
def fun01(oddj = 51):
    n = 1
    while 1:
        n9 = 10**n-1
        if n9%oddj == 0:
            print('%d 个 9 可以被 %d 整除 : %d' % (n, oddj, n9))
            print('显示：%d / %d = %d' % (n9, oddj, n9/oddj))
            print('校验：%d * %d = %d' % (n9/oddj, oddj, n9))
            break
        else:
            n+=1


if __name__ == '__main__':
    for i in range(1,100,10):
        fun01(i)