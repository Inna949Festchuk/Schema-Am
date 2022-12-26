import math as math
import csv
import matplotlib.pyplot as plt

class Points:
    def __init__(self, x1, y1, x2, y2, Pn):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.Pn = Pn
    '''
    Класс предназначен для построения схемы движения по магнитным азимутам в пешем порядке
    на основе решения Обратной геодезической задачи
    x1, y1 - плоские прямоугольные координаты точки стояния
    x2, y2 - плоские прямоугольные координаты ориентира
    Pn - поправка направления
    '''    
    def Am(self):
        '''
        Функция решения Обратной геодезической задачи
        '''   
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
        Am_degre = a - self.Pn
        Am_grad = int(Am_degre)
        Am_min = int(60*(Am_degre - Am_grad))
        Am_sec = round(60*(60*(Am_degre - int(Am_degre)) - Am_min), 1)
        Am = ''.join([str(Am_grad)+"°",str(Am_min)+"'",str(Am_sec)+'"'])    
        return Am, S

if __name__ == '__main__':
    input('Схема движения по азимутам 1.0.0\nPress Enter')
    x = []
    y = []
    with open('indata.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            point = Points(float(row.get('xone')), float(row.get('yone')), float(row.get('xtwo')), 
                           float(row.get('ytwo')), float(row.get('P')))
            with open('outdata.txt', 'a', encoding = 'utf-8') as doc:
                output_str = ','.join([str(point.x1), str(point.y1), str(point.x2), str(point.y2), 
                                       str(point.Am()[0]), '{0:.0f}'.format(point.Am()[1])+' п.ш.'])
                doc.write(output_str + '\n')
            x.append(point.x1)
            x.append(point.x2)
            y.append(point.y1)
            y.append(point.y2)
        print('Успешно!')
        plt.xlabel('Координата_Y, метры')
        plt.ylabel('Координата_X, метры')
        plt.title('Схема движения по азимутам') 
        plt.plot(y, x)
        plt.scatter(y, x)
        plt.show()
        
    
    
