import trees
myDat, labels = trees.createDataSet()
trees.splitDataSet(myDat, 0, 1)
trees.splitDataSet(myDat, 0, 0)
trees.chooseBestFeatureToSplit(myDat)
myTree = trees.createTree(myDat,labels)