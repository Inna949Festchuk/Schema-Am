import math as math
import csv

class Points:
    def __init__(self, x1, y1, x2, y2, Pn):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.Pn = Pn
        
    def Am(self):
        dX = self.x2 - self.x1
        dY = self.y2 - self.y1
        if dX == 0:
            r = 90
        elif dY == 0:
            r = 0
        else:
            r = (180/math.pi)*math.atan(math.sqrt((dY/dX)**2))
        S = math.sqrt(dX**2 + dY**2)/1.5
        if dX >= 0 and dY >= 0:
            a = r
        elif dX < 0 and dY > 0:
            a = 180 - r
        elif dX <= 0 and dY <= 0:
            a = 180 + r
        else:
            a = 360 - r
        Am = a - self.Pn
        return Am, S

if __name__ == '__main__':
    input('Схема движения по азимутам 1.0.0\nPress Enter')
    with open('indata.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            point = Points(float(row.get('xone')), float(row.get('yone')), float(row.get('xtwo')), 
                           float(row.get('ytwo')), float(row.get('P')))
            with open('indata.txt', 'a') as doc:
                doc.write(str(point.x1) + ', ' + str(point.y1) + ', ' + str(point.x2) + ', ' 
                          + str(point.y2) + ', ' + str(point.Am()[0]) + ', ' + str(point.Am()[1]) + '\n')
    input('Успешно!')
