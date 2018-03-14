'''题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。'''

def fun01(n=12321):
    if not isinstance(n,int):
        print('请重新输入数字，以判断是否是回文数')
        return
    numlen = len(str(n))
    tempn=n
    m=0
    for i in range(numlen):
        m = m*10 + tempn%10
        tempn//=10
    if m==n:
        print('%d是个回文数'%n)
    else:
        print('%d不是个回个数'%n)

if __name__ == '__main__':
    fun01(159951)