'''题目：输出一个随机数。'''

import random
import matplotlib.pyplot as plt
from numpy.random import randn

def fun01():
    labels='frogs','hogs','dogs','logs'
    sizes=15,20,45,10
    colors='yellowgreen','gold','lightskyblue','lightcoral'
    explode=0,0.1,0,0
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
    plt.axis('equal')

    plt.show()

def fun02():
    fig = plt.figure()
    x = range(0, 1000)

    titile1 = 'random.uniform(0,1)'
    y1=[random.uniform(0,1) for i in x]
    Ax1 = fig.add_subplot(221) # Fig.add_subplot(1,1,1)
    Ax1.set_title(titile1)
    Ax1.plot(x,y1, 'r.')

    titile2 = 'random.randint(0,1)'
    y2=[random.randint(0,1) for i in x]
    Ax2 = fig.add_subplot(222) # Fig.add_subplot(1,1,1)
    Ax2.set_title(titile2)
    Ax2.plot(x,y2, 'r.')

    titile3 = 'random.gauss(10,1)'
    y3=[random.gauss(0,1) for i in x]
    Ax3 = fig.add_subplot(223) # Fig.add_subplot(1,1,1)
    Ax3.set_title(titile3)
    Ax3.plot(x,y3, 'r.')

    titile4 = 'random.randrange(0,1)'
    y4=[random.randrange(0,1) for i in x]
    Ax4 = fig.add_subplot(224) # Fig.add_subplot(1,1,1)
    Ax4.set_title(titile4)
    Ax4.plot(x,y4, 'r.')

    plt.show()

if __name__ == '__main__':
    fun02()