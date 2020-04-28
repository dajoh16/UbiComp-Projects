import csv, math, glob, os
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
    return Classification(distances[0][1].realx, distances[0][1].realy)


trainingdata = []
for filename in glob.glob("experiment2\\train\\*data_wide.csv"):
    with open(filename,newline='\n') as csvfile:
        
        trainreader = csv.DictReader(csvfile, delimiter=',')
        for row in trainreader:
            traindata = TrainData(row['realx'],row['realy'],row['edge_50'],row['edge_51'],row['edge_52'],row['edge_53'],row['edge_54'],row['edge_55'],row['edge_56'],row['edge_57'],row['edge_58'])
            trainingdata.append(traindata)

allDist = []
testingdata = []

for filename in glob.glob("experiment2\\test\\*data_wide.csv"):
    with open(filename,newline='\n') as csvfile:
        testreader = csv.DictReader(csvfile, delimiter=',')
        
        for row in testreader:
            testdata = TestData(row['realx'],row['realy'],row['edge_50'],row['edge_51'],row['edge_52'],row['edge_53'],row['edge_54'],row['edge_55'],row['edge_56'],row['edge_57'],row['edge_58'])
            testingdata.append(testdata)
    actualFilename = os.path.basename(filename)
    output = open("output-"+actualFilename+".dat","w+")
    outputReal = open("outputReal-"+actualFilename+".dat","w+")
    outputClass = open("outputClass-"+actualFilename+".dat","w+")

    distSum = 0

    outputLines = []
    outputLinesReal = []
    outputLinesClass = []
    for test in testingdata:
        classification = NearestNeighbor(trainingdata, test)
        distSum += Calculate2DEuclideanDistance(classification, test)
        line1 = "-"+str(classification.classifiedx) + " " + str(classification.classifiedy) + "\n"
        line2 = "-"+str(test.realx) + " " + str(test.realy) + "\n"
        outputLines.append(line1)
        outputLines.append(line2+"\n")
        outputLinesReal.append(line2)
        outputLinesClass.append(line1)
        



    output.writelines(outputLines)
    outputReal.writelines(outputLinesReal)
    outputClass.writelines(outputLinesClass)

    avgDist = distSum / len(testingdata)
    allDist.append(avgDist)
    print("Avg Distance from Reality: " + str(avgDist))
sumD = 0
for dist in allDist:
    sumD += dist

avg = sumD / len(allDist)
print("Avg Distance for ALL test files: " + str(avg))