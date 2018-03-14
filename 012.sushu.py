'''题目：判断101-200之间有多少个素数，并输出所有素数。'''

def fun01(startNum,endNum):
    n=0
    for num in range(startNum,endNum+1):
        div=2
        while (div**2 < num+1):
            if num%div == 0:
                break
            else:
                div+=1
        if div**2 >= num+1 :
            print(num)
            n+=1
    print('total number is %d'%n)


if __name__ == '__main__':

    fun01(101,200)


