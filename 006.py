'''题目：斐波那契数列。'''
'''1,1,2,3,5,...'''
def fib01(n):
    '''输入菲波那切数列的索引，得到一个值'''
    if n <2:
        return n
    else:
        return fib01(n-1)+fib01(n-2)

def fib02(n):
    '''输入菲波那切数列的索引，得到一个值'''
    f0,f1 = 0,1
    for i in range(n):
        #print(f0)
        f0,f1 = f1, f0+f1
    return f0


if __name__ == '__main__':
    n=10
    for i in range(n+1):
        fibval = fib02(i)
        print('第%d个斐波那契数是：%d'%(i,fibval))