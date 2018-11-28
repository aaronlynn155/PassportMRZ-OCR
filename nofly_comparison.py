#stores lists of users on no-fly lists, including several arguments
#preforms comparison algorithm
#
import io

#this will import PyQT5 and provide us the needed materials for a popup
from PyQt5.QtWidgets import QApplication, QLabel

#TABLE IS ORGANIZED IN COLUMN
noFlyFNames = ["JOSEPH","GREG","GEORGE","NAMA"]
noFlyLNames = ["STALIN","POPOVICH","ClOONEY","LENGKAP"]
noFlyPIDs = ["123456789", "123456789", "123456789","X000000"]
noFlyIssuingCountryCodes = ["USA","USA","USA","IDN"]
noFlyNationalities = ["USA","GBR","USA","IDN"]
noFlyBirthCodes = ["850101","950225","990329","450817"] #85/01/19 format
noFlyExpireyDates = ["180112","170314","160530","160126"] #85/01/19 Format
noFlyPersonalCodes = ["111111111111111","22222222222222","3333333333333333"]

def confidence_flip_flop():

    resultFile = open("result_text.txt ", "r")
    confidenceFile = open("result_confidence.txt","r")
    resultFileDataList = resultFile.readlines()
    comparisonDataList = confidenceFile.readlines()
    resultFile.close
    confidenceFile.close()
    tempCharList = []
    tempCompList = []
    counter = 0
    counter2 = 0
    for word in resultFileDataList:
        for character in word:
            tempCharList.append(character)

    for compnum in comparisonDataList:
            tempCompList.append(compnum)

    for tempChar, compnum in zip(tempCharList,tempCompList):
        if compnum != '\n' and compnum != 1.0:
            int_compnum = int(compnum[2:4])

            if int_compnum <= 35 and int_compnum != 0:
                if tempChar == '5':
                    tempCharList[counter] = 'S'
                    break
                if tempChar == 'S':
                    tempCharList[counter] = '5'
                    break
                if tempChar == '4':
                    tempCharList[counter] = 'A'
                    break
                if tempChar == 'A':
                    tempCharList[counter] = '4'
                    break
                if tempChar == '0':
                    tempCharList[counter] = 'O'
                    break
                if tempChar == 'O':
                    tempCharList[counter] = '0'
                    break
                if tempChar == '8':
                    tempCharList[counter] = 'B'
                    break
                if tempChar == 'B':
                    tempCharList[counter] = '8'
                    break

        counter += 1

    for tempChar, compnum in zip(tempCharList, tempCompList):
        if compnum != '\n' and compnum != 1.0:
            int_compnum = int(compnum[2:4])
            print(tempChar, int_compnum)




def comparison_Alg():
    #Compares/ Slices imported user data against NoFly Lists.
    inFile = open("result_text.txt","r")
    dataList = inFile.readlines()
    inFile.close()
    y = 0
    matches = 0
    matchIndex = []
    columnMatch = False
    for x in dataList:
        x.rstrip()
        print(x)
        if y == 1:
            setCount1 = 0
            setCount2 = 0
            dataPoint1 = x
            userCountryCode = dataPoint1[0:3]
            for i in noFlyIssuingCountryCodes:
                if userCountryCode == i:
                    print("Match on Country Code!")
                    matches += 1
                    matchIndex.append(setCount1)

                setCount1 +=1

            userLName = dataPoint1[3:-1]
            for i in noFlyLNames:
                if userLName == i:
                    print("Match on Last Name!")
                    matches += 1
                    matchIndex.append(setCount2)
                setCount2 +=1

        if y == 2:
            setCount = 0
            dataPoint2 = x
            userFName = dataPoint2[:-1]
            for i in noFlyFNames:

                if userFName == i:
                    print("Match on First Name!")
                    matches += 1
                    matchIndex.append(setCount)
                setCount +=1

        if y == 3:
            setCount = 0
            dataPoint3 = x
            userPID = dataPoint3[:-1]
            for i in noFlyPIDs:
                if userPID == i:
                    print("Match on PID!")
                    matches += 1
                    matchIndex.append(setCount)
                setCount += 1

        if y == 4:
            setCount1 = 0
            setCount2 = 0
            setCount3 = 0
            dataPoint4 = x
            userNationality = dataPoint4[1:4]
            for i in noFlyNationalities:
                if userNationality == i:
                    print("Match on Nationality!")
                    matches += 1
                    matchIndex.append(setCount1)
                setCount1 += 1

            userBirthCode = dataPoint4[4:10]
            for i in noFlyBirthCodes:
                if userBirthCode == i:
                    print("Match on Birth Code!")
                    matches += 1
                    matchIndex.append(setCount2)
                setCount2 +=1

            userExpireyCode = dataPoint4[12:-2]
            for i in noFlyExpireyDates:
                if userExpireyCode == i:
                    print("Match on Expirey Code!")
                    matches += 1
                    matchIndex.append(setCount3)
                setCount3 +=1

        y += 1

    if matches >= 5 and matchIndex.count(matchIndex[0]) == len(matchIndex):
        #this is to provide a basic popup should the GUI itself not function properly
        app = QApplication([])
        label = QLabel("Close matches have been found, Check the passport before alerting security.\nTotal amount of "
                       "matches: ", matches)
        label.show()
        app.exec_()
        print(matches, "matches found, Close Match detected. Check Passport Before Alerting Security.")

if __name__ == '__main__':
    confidence_flip_flop()
    comparison_Alg()
