'''题目：利用递归方法求5!。'''

def fact(n=5):
    sum=0
    if n==1:
        sum=1
    else:
        sum=n*fact(n-1)
    return sum


if __name__ == '__main__':

    print(fact())