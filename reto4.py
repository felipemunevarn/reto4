#Defining a constant for limits in tuple of tuples
#            0:male      1:female
limits = ((12.2, 16.6), (12.6, 15))
#         0:low,1:high  0:low,1:high

hemoglobin = []
gender = []
mean = []

def dataEntry(): #fill the data
    number = eval(input())
    for index in range(number):
        hemoglobin.append(list(map(float, input().split())))
        gender.append(int(hemoglobin[index].pop(0)))

def calculateMeans():
    max, min, posMax, posMin = 0, 0, 0, 0
    for i in range(len(hemoglobin)):#cycle in patients
        mean.append(sum(hemoglobin[i]) / len(hemoglobin[i]))
        if max < mean[i]:#finding maximus and position
            max = mean[i]
            posMax = i
        if min > mean[i]:#finding minimum and position
            min = mean[i]
            posMin = i
    return posMax, posMin

def checkLimitsAndPrint(index):
    #according gender compare hemoglobin vs low limit
    for value in index:
        if mean[value] < limits[gender[value] - 1][0]:
            print(gender[value], "%.2f" % mean[value], 'Baja')
        #according gender compare hemo vs high limit
        elif mean[value] > limits[value][1]:
            print(gender[value], "%.2f" % mean[value], 'Alta')
        else:
            print(gender[value], "%.2f" % mean[value], 'Normal')

def countPatientsByGender():
    male, female = 0, 0
    for patient in gender:
        male = male + 1 if patient == 1 else male
        female = female + 1 if patient == 2 else female
    print(male, female)

dataEntry()
keysValues = calculateMeans()
checkLimitsAndPrint(keysValues)
countPatientsByGender()
