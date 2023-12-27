import sys
from os import listdir
import numpy as np
import operator

#데이터셋 만들고
def createDataSet(dirname):
    labels = []
    FileList = listdir(dirname)
    m = len(FileList)
    matrix = np.zeros((m, 1024))

    for i in range(m):
        txtName = FileList[i]
        txtLabelPart = int(txtName.split('_')[0])
        labels.append(txtLabelPart)
        matrix[i, :] = getVector(dirname + '/' + txtName)
    return matrix, labels 

#거리계산
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2 
    sqDistances = sqDiffMat.sum(axis = 1) 
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort() 
    classCount = {}

    for i in range(k): 
        voteIlabel = labels[sortedDistIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def getVector(filename): 
    vector = np.zeros((1, 1024)) 
    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
        return vector        

trainingDigits = sys.argv[1]
testDigits = sys.argv[2]
testFileList = listdir(testDigits)
length = len(testFileList)
matrix, labels = createDataSet(trainingDigits)

for k in range(1, 21): 
    count = 0 #전체갯수
    errorCount = 0 #에러부분갯수
    
    for i in range(length):
        txtLabelPart = int(testFileList[i].split('_')[0])
        testData = getVector(testDigits + '/' + testFileList[i])
        classifiedResult = classify0(testData, matrix, labels, k)
        count += 1
        
        if txtLabelPart != classifiedResult :
            errorCount += 1
    
    print(int(errorCount / count * 100))