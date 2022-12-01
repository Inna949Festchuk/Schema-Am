# ТОЧКА ВХОДА
# import math as math
import csv
from xy import Points # Импорт класса Point из файла xy.py
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