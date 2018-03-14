'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

'''

def fun01(a,n):
    if not isinstance(a,int) or not isinstance(n,int) or a<1 or n<1:
        print('请输入正确的数字')
        return

    s=0
    an=0
    for i in range(n):
        an = 10*an + a
        print(an)
        s+=an

    print('计算和为：', s)


if __name__ == '__main__':
    fun01(4,4)
    fun01(5, 6)