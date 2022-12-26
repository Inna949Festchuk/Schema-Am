import csv
import matplotlib.pyplot as plt

from xy import Points

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
        plt.xlabel('Координата_Y, метры')
        plt.ylabel('Координата_X, метры')
        plt.title('Схема движения по азимутам') 
        plt.plot(y, x)
        plt.scatter(y, x)
        plt.show()
        