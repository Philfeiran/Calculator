from calculator import calculator
import unittest
import csv


def readFile (file):
    csvFile = open(file, "r")
    reader = csv.reader(csvFile)
    IsThreeVar = True
    x=[]
    y=[]
    result=[]
    for item in reader:
        if reader.line_num==1:
            if item[2]==' ':
                IsThreeVar=False
            continue
        x.append(float(item[0]))
        if not IsThreeVar:
            result.append(float(item[1]))
        else:
            y.append(float(item[1]))
            result.append(float(item[2]))

    if IsThreeVar:
        return x,y,result
    else:
        return x,result

class testCalculator(unittest.TestCase):
    cal = calculator()
    def testAddition(self):
        self.assertEqual(self.cal.add(2,2),4)
    def testSubtraction(self):
        self.assertEqual(self.cal.minus(2,2),0)
    def testMultiplication(self):
        self.assertEqual(self.cal.multply(2,2),4)
    def testDivision(self):
        self.assertEqual(self.cal.divide(2,4),2)
    def testSquare(self):
        self.assertEqual(self.cal.square(4),16)
    def testSquareRoot(self):
        self.assertEqual(self.cal.squareRoot(4),2)
    def testCSVfiles(self):
        #test addition file
        xADD,yADD,resultADD = readFile("./src/Unit Test Addition.csv")
        xSUB,ySUB,resultSUB= readFile("./src/Unit Test Subtraction.csv")
        xMUL,yMUL,resultMUL=readFile("./src/Unit Test Multiplication.csv")
        xDIV, yDIV, resultDIV = readFile("./src/Unit Test Division.csv")
        xSQU, resultSQU = readFile("./src/Unit Test Square.csv")
        xSQR, resultSQR = readFile("./src/Unit Test Square Root.csv")

        #All CSV files have 18 exapmle
        for i in range (18):
            self.assertEqual(self.cal.add(xADD[i],yADD[i]),resultADD[i])
            self.assertEqual(self.cal.minus(xSUB[i],ySUB[i]),resultSUB[i])
            self.assertEqual(self.cal.multply(xMUL[i],yMUL[i]),resultMUL[i])
            #for divison and square root, I only campare 6 demicial places
            self.assertEqual(round(self.cal.divide(xDIV[i],yDIV[i]),6),round(resultDIV[i],6))
            self.assertEqual(self.cal.square(xSQU[i]),resultSQU[i])
            self.assertEqual(round(self.cal.squareRoot(xSQR[i]),6),round(resultSQR[i],6))



if __name__ == '__main__':

    unittest.main()
