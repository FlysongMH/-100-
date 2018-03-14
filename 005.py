'''题目：输入三个整数x,y,z，请把这三个数由小到大输出。'''

if __name__ == '__main__':
    inputlist = []
    for i in range(3):
        x=int(input('请输入第%d个整数：'%i))
        inputlist.append(x)
    inputlist.sort()
    print('从小到大的顺序是：', inputlist)
    inputlist.sort(reverse=True)
    print('从大到小的顺序是：', inputlist)