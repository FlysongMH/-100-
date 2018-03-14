from itertools import permutations
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

def permutation00():
    '''使用集合去除重复'''
    list = []
    n = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if len(set([i,j,k])) == 3:
                    list.append([i,j,k])
                    n += 1
    print('能组成%d个互不相同且无重复数字的三位数：'%n)
    print(list)

def permutation01():
    '''单独判断'''
    d=[]
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                if (a!=b) and (a!=c) and (c!=b):
                    d.append([a,b,c])
    print("总数量：", len(d))
    print(d)

def permutation02():
    '''列表推导式直接得到'''
    list_num = [1, 2, 3, 4]
    list = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num if
            (j != i and k != j and k != i)]
    print()
    print('能组成%d个互不相同且无重复数字的三位数：' % len(list))
    print(list)

def permutation03():
    '''使用库中的迭代器函数'''
    list = []
    for temp in permutations([1, 2, 3, 4], 3):
        list.append(temp)
    print('能组成%d个互不相同且无重复数字的三位数：' % len(list))
    print(list)

def permutation04():
    '''使用位运算从 00 01 10  到  11 10 01'''
    for num in range(6, 58):
        a = num >> 4 & 3
        b = num >> 2 & 3
        c = num & 3
        if ((a ^ b) and (b ^ c) and (c ^ a)):
            print([a + 1, b + 1, c + 1])

def permutation05():
    ''''''
    d = []
    for j in range(1, 5):
        for k in range(1, 5):
            for l in range(1, 5):
                if l != j != k != l:
                    d.append(int(str(j) + str(k) + str(l)))
    print('能组成%d个互不相同且无重复数字的三位数：' % len(d))
    print(d)



if __name__ == '__main__':
    permutation05()

