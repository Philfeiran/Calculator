from calculator import calculator
import unittest
import csv

class testCalculator(unittest.TestCase):

    def testAdd(self):
        cal = calculator()
        csvFile = open("Unit Test Addition.csv", "r")
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num ==1:
                continue
            x=float(item[0])
            y=float(item[1])
            result=float(item[2])
            self.assertEqual(cal.add(x,y),result)
    def testMinus(self):
        cal = calculator()
        csvFile = open("Unit Test Subtraction.csv", "r")
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num ==1:
                continue
            x=float(item[0])
            y=float(item[1])
            result=float(item[2])
            self.assertEqual(cal.minus(y,x),result)

    def testMultip(self):
        cal = calculator()
        csvFile = open("Unit Test Multiplication.csv", "r")
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num == 1:
                continue
            x = float(item[0])
            y = float(item[1])
            result = float(item[2])
            self.assertEqual(cal.multply(y, x), result)

    def testDivide(self):
        cal = calculator()
        csvFile = open("Unit Test Division.csv", "r")
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num == 1:
                continue
            x = float(item[0])
            y = float(item[1])
            result = float(item[2])
            self.assertEqual(round(cal.divide(y, x),5), round(result,5))

    def testSquare(self):
        cal = calculator()
        csvFile = open("Unit Test Square.csv", "r")
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num == 1:
                continue
            x = float(item[0])
            result = float(item[1])
            self.assertEqual(cal.square(x), result)


    def testSquareRoot(self):
        cal = calculator()
        csvFile = open("Unit Test Square Root.csv", "r")
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num == 1:
                continue
            x = int(item[0])
            result = float(item[1])
            self.assertEqual(round(cal.squareRoot(x),5), round(result,5))

if __name__ == '__main__':

    unittest.main()
