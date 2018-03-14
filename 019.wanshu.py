'''题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。'''


def judgeComplteNum(n):
    sumn = 0
    k = []
    for i in range(1,n):
        if n % i == 0:
            sumn+=i
            k.append(i)
    if sumn==n:
        print(n)
        print(k)

if __name__ == '__main__':

    for i in range(1,1001):
        judgeComplteNum(i)