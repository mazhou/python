<pre>
import kNN
group,labels = kNN.createDataSet()
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
</pre>