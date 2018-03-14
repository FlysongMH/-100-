
'''题目：求1+2!+3!+...+20!的和。'''

def fun01(n=20):
    t = 1
    s = 0
    tlist=[1]
    slist=[]
    for i in range(1,n+1):
        t *= i
        s+=t
        tlist.append(t)
        slist.append(s)

        print('%d!=%d'%(i,t))

        # print('%d!'%i, end='')
        # if i != n:
        #     print('+',end='')
        # else:
        #     print('=')

    print('1!+2!+3!+...+%d!=%d' % (n,s))
    # print(tlist)
    # print(slist)







if __name__ == '__main__':
    fun01()

