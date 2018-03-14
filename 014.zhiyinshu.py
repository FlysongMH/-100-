'''题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。'''

def reduceNum01(n):
    if not isinstance(n,int) or n <=0 :
        print('输入错误！%s'%n)
        return
    print('%d = '%n, end='')
    if n==1:
        print(n)
        return

    while n!=1:
        for idx in range(2,n+1):
            if n % idx == 0 :
                n //= idx#要使用整除运算符
                if n==1:
                    print(idx)#最后一次了
                else:
                    print('%d * '%idx, end='')
                break


if __name__ == '__main__':
    reduceNum01(90)
    reduceNum01(100)