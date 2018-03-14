
# new list
testList=[10086,'中国移动',[1,2,4,5]]

# print('%-10s'%(r'len(): '), len(testList)) #长度
# print('%-10s'%(r'[:]: '),   testList[:]) #取范围
# print('%-10s'%(r'[1:]: '),  testList[1:]) #取范围
# print('%-10s'%(r'[1:9]: '), testList[1:9]) #取范围
# print('%-10s'%(r'[1:1]: '), testList[1:1]) #取范围
# print('%-10s'%(r'[-1]: '),  testList[-1]) #取范围
# print(r'[-5]: ', testList[-5]) #取范围，范围超出


# testList.append('I\'m new here!')
# print('%-10s'%(''),   testList)




# print('%-10s'%(r'.pop(1)'),   testList.pop(1)) #删除某个元素并返回
# print('%-10s'%(''),   testList)

# print(testList.pop(9)) #无法找到索引
# print(testList)

matrix = [\
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(matrix)
print(matrix[1]) #矩阵的第一维度是行

# col2 = [row[1] for row in matrix] #取矩阵的第一列
# print(col2)

col2even = [row[1] for row in matrix if  row[1] % 2 == 0]#filter odd item
print(col2even)