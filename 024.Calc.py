'''题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。'''

def fun01(n=20):
    a = 2
    b = 1
    s=0
    for i in range(n):
       s+=a/b
       a,b=a+b,a
    print(s)




if __name__ == '__main__':
    fun01()
