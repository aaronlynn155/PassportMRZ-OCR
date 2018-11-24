#stores lists of users on no-fly lists, including several arguments
#preforms comparison algorithm
import io

#This imports PyQT into the program and provides us with what we need
import sys
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
    #checks given triple nested array, flip flopping bad confidence to known alternate characters as necessary.
    inFile = open("confidence.txt","r")
    advancedDataList = inFile.readlines()
    inFile.close()

    

def comparison_Alg():
    #Compares/ Slices imported user data against NoFly Lists.
    inFile = open("out.txt","r")
    dataList = inFile.readlines()
    inFile.close()
    y = 0
    matches = 0
    userCountryCode = ""
    userLName = ""
    userPID = ""
    userBirthCode = ""
    for x in dataList:
        x.rstrip()
        print(x)
        if y == 1:
            dataPoint1 = x
            userCountryCode = dataPoint1[0:3]
            for i in noFlyIssuingCountryCodes:
                if userCountryCode == i:
                    print("Match on Country Code!")
                    matches += 1

            userLName = dataPoint1[3:-1]
            for i in noFlyLNames:
                if userLName == i:
                    print("Match on Last Name!")
                    matches += 1

        if y == 2:
            dataPoint2 = x
            userFName = dataPoint2[:-1]
            for i in noFlyFNames:

                if userFName == i:
                    print("Match on First Name!")
                    matches += 1

        if y == 3:
            dataPoint3 = x
            userPID = dataPoint3[:-1]
            for i in noFlyPIDs:
                if userPID == i:
                    print("Match on PID!")
                    matches += 1

        if y == 4:
            dataPoint4 = x
            userNationality = dataPoint4[1:4]
            for i in noFlyNationalities:
                if userNationality == i:
                    print("Match on Nationality!")
                    matches += 1

            userBirthCode = dataPoint4[4:10]
            for i in noFlyBirthCodes:
                if userBirthCode == i:
                    print("Match on Birth Code!")
                    matches += 1

            userExpireyCode = dataPoint4[12:-2]
            for i in noFlyExpireyDates:
                if userExpireyCode == i:
                    print("Match on Expirey Code!")
                    matches += 1

        y += 1

    if matches >= 5:
        app = QApplication([])
        label = QLabel("Matches: ", matches, "Close Match detected. Check Passport Before Alerting Security.")
        label.show()
        app.exec()
        print(matches, "matches found, Close Match detected. Check Passport Before Alerting Security.")
    else:
        app = QApplication([])
        label = QLabel("No matches found")
        label.show()
        app.exec()
        print("No matches found.")

if __name__ == '__main__':
    comparison_Alg()
