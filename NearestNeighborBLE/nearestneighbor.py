import csv, math, glob
class TrainData:
    def __init__(self,realx,realy,edge_1,edge_2,edge_3,edge_8,edge_9,edge_10,edge_11,edge_12,edge_13):
        self.realx = float(realx)
        self.realy = float(realy)
        self.edge_1 = float(edge_1) 
        self.edge_2 = float(edge_2)
        self.edge_3 = float(edge_3)
        self.edge_8 = float(edge_8)
        self.edge_9 = float(edge_9)
        self.edge_10 = float(edge_10)
        self.edge_11 = float(edge_11)
        self.edge_12 = float(edge_12)
        self.edge_13 = float(edge_13)

class TestData:
    def __init__(self,realx,realy,edge_1,edge_2,edge_3,edge_8,edge_9,edge_10,edge_11,edge_12,edge_13):
        self.realx = float(realx)
        self.realy = float(realy)
        self.edge_1 = float(edge_1) 
        self.edge_2 = float(edge_2)
        self.edge_3 = float(edge_3)
        self.edge_8 = float(edge_8)
        self.edge_9 = float(edge_9)
        self.edge_10 = float(edge_10)
        self.edge_11 = float(edge_11)
        self.edge_12 = float(edge_12)
        self.edge_13 = float(edge_13)

class Classification:
    def __init__(self,classifiedx,classifiedy):
        self.classifiedx = classifiedx
        self.classifiedy = classifiedy

def Calculate2DEuclideanDistance(classifieddata, testdata):
    distanceSquared = (classifieddata.classifiedx - testdata.realx)**2 + (classifieddata.classifiedy - testdata.realy)**2
    return math.sqrt(distanceSquared)

def CalculateEuclideanDistance(traindata, testdata):
    distanceSquared = (traindata.edge_1 - testdata.edge_1)**2 + (traindata.edge_2 - testdata.edge_2)**2 + (traindata.edge_3 - testdata.edge_3)**2 + (traindata.edge_8 - testdata.edge_8)**2 + (traindata.edge_9 - testdata.edge_9)**2 + (traindata.edge_10 - testdata.edge_10)**2 + (traindata.edge_11 - testdata.edge_11)**2 + (traindata.edge_12 - testdata.edge_12)**2 + (traindata.edge_13 - testdata.edge_13)**2
    return math.sqrt(distanceSquared)

def NearestNeighbor(trainingdata, testdata):
    distances = []
    for train in trainingdata:
        distance = CalculateEuclideanDistance(train,testdata)
        distances.append((distance,train))
    distances.sort(key=lambda tup: tup[0])
    #list.sort(distances)
    return Classification(distances[0][1].realx, distances[0][1].realy)


trainingdata = []
for filename in glob.glob("experiment1\\train\\*data_wide.csv"):
    with open(filename,newline='\n') as csvfile:
        trainreader = csv.DictReader(csvfile, delimiter=',')
        for row in trainreader:
            traindata = TrainData(row['realx'],row['realy'],row['edge_1'],row['edge_2'],row['edge_3'],row['edge_8'],row['edge_9'],row['edge_10'],row['edge_11'],row['edge_12'],row['edge_13'])
            trainingdata.append(traindata)

testingdata = []
with open('experiment1\\test\\2018-09-24T23-22-15-500000_9_data_wide.csv',newline='\n') as csvfile:
    testreader = csv.DictReader(csvfile, delimiter=',')
    for row in testreader:
        testdata = TestData(row['realx'],row['realy'],row['edge_1'],row['edge_2'],row['edge_3'],row['edge_8'],row['edge_9'],row['edge_10'],row['edge_11'],row['edge_12'],row['edge_13'])
        testingdata.append(testdata)

distSum = 0
for test in testingdata:
    classification = NearestNeighbor(trainingdata, test)
    distSum += Calculate2DEuclideanDistance(classification, test)

avgDist = distSum / len(testingdata)

print("Avg Distance from Reality: " + str(avgDist))
