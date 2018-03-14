'''题目：使用lambda来创建匿名函数。'''

MAXIMUM = lambda x,y:(x>=y)*x+(x<y)*y
MINIMUM = lambda x,y:(x<=y)*x+(x>y)*y

if __name__ == '__main__':
    a = 10
    b = 10
    print(MAXIMUM(a, b))
    print(MINIMUM(a, b))