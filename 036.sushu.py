'''题目：求100之内的素数。'''

'''
在 python 中，for … else 表示这样的意思，
for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，
while … else 也是一样。
'''


def fun01(startNum=1, endNum=100):
    for num in range(startNum,endNum+1):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)

if __name__ == '__main__':
    fun01()