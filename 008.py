'''题目：输出 9*9 乘法口诀表。'''
#暂停一秒输出，并格式化当前时间。
import time

def fun1():
    for i in range(1,10):
        for j in range(i, 10):
            ij = i*j
            endspace = 3-len(list(str(ij)))
            print('%d*%d=%d'%(i,j,ij), end=' '*endspace) #手动对齐字符串
        print('')

def fun2():
    for i in range(1,10):
        for j in range(1,i+1):
            #print('%s*%s=%-3s'%(i,j,i*j), end='') # %格式化字符串，'-'左对齐，长度3
            print('{}*{}={:<3d}'.format(i,j,i*j), end='')  # %格式化字符串，'-'左对齐，长度3
        print('')

if __name__ == '__main__':

    fun1()

    #暂停一秒输出，并格式化当前时间。
    print('休息一秒钟:-)')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    fun2()