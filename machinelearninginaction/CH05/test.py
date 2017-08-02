from numpy import *

fr = open('testSet.txt')
dataMat=[];
for line in fr.readlines():
    lineArr = line.strip().split()
    #print(lineArr)
    dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])

dataMatrix = mat(dataMat)
m,n = shape(dataMatrix)
print(m,n)
