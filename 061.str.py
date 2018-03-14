'''题目：打印出杨辉三角形（要求打印出10行如下图）。'''

def yanghui_ij(i, j):
    if i==j or j==1:
        return 1
    else:
        return yanghui_ij(i-1,j-1)+yanghui_ij(i-1,j)

def yanghui01(n=10):
    '''递归法'''
    # rslt = [[yanghui_ij(i,j) for j in range(1,i+1)] for i in range(1,n+1)]
    # print(rslt)
    for i in range(1, n + 1):
        print([yanghui_ij(i,j) for j in range(1,i+1)])

def fun04():

    yanghui = [[1, 1]]  # 初始化
    for i in range(10 - 2):  # 打印10行，计算的行数只有8行
        l_temp = [1]  # 每行的第一个数为1
        for j in range(len(yanghui[i]) - 1):  # 遍历上一行
            l_temp.append(yanghui[i][j] + yanghui[i][j + 1])
        else:
            l_temp.append(1)  # 最后一行也为1
        yanghui.append(l_temp)  # 加入杨辉list中
    yanghui.insert(0, [1])  # 按要求添加第一行的元素
    for i in yanghui:
        print(i)  # 按要求输出


def fun02():
    l = [1]
    for i in range(10):
        for k in l:
            print(k, end='\t')
        print('\n ')
        l1 = l[:]
        l1.insert(0, 0)
        l1.append(0)
        l2 = []
        for i in range(len(l1) - 1):
            l2.append(l1[i] + l1[i + 1])
        l = l2[:]


def Pascal(n):
    ls = [[1]]
    for i in range (1, n):
        ls.append([1])
        for j in range(1, i):
            ls[i].append(ls[i-1][j-1] + ls[i-1][j])
        ls[i].append(1)
    for i in range(0, n): print(ls[i])
    return ls
def fun03():
    a = Pascal(10)

if __name__ == '__main__':
    yanghui01()