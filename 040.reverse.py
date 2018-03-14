'''题目：将一个数组逆序输出。'''

def fun01(a):
    print(a)
    b=a[::-1]
    print(b)


def fun02(a):
    print(a)
    b=a[:]     #   b复制了a的值，b指向另外的内存
    b.reverse()
    print(b)

def fun03(a):
    print(a)
    b=a     #   b和a指向了同一个内存，因此修改b也修改了a
    b.reverse()
    print(b)

if __name__ == '__main__':
    a=[9,6,5,4,1]
    # fun01(a)
    # print(a)
    fun02(a)
    print(a)