'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''
def fun01(n):
    '''
    计算广义水仙花数，
    输入一个位数n，求得各个数字的n次方之和等于该数的某个n位数
    '''
    startNum = 10**(n-1)
    endNum   = 10**n
    listn = []
    for theNum in range(startNum,endNum):
        #print(theNum)
        temp=0
        for stri in str(theNum):
            temp+= int(stri)**n
            #print(temp)
        if temp == theNum :
            listn.append(theNum)
    print('%d位数的广义水仙花数有%d个：\n'%(n,len(listn)),listn)



if __name__ == '__main__':
    for i in range(1,6):
        fun01(i)
