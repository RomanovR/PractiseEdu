import csv
import datetime
import sqlite3

""" Установка промежутка,  в который собирается статистика """
# - 7 hours
# Указание отметок
timeStart = datetime.datetime(2019, 10, 21, 13, 37)
timeEnd = datetime.datetime(2019, 10, 21, 16, 30)

# Конвертирование в timestamp
tsStart = int(datetime.datetime.timestamp(timeStart))
tsEnd = int(datetime.datetime.timestamp(timeEnd))
print(tsStart)
print(tsEnd)

""" Запрос списка сердцебиения и подключение к БД """
conn = sqlite3.connect('data/db21_10_2019_1500_1558.sqlite')
cursor = conn.cursor()

cursor.execute("SELECT * FROM heartrate WHERE time BETWEEN ? AND ?", (tsStart + 1, tsEnd))
hrOut = cursor.fetchall()

""" Запрос списка шагов и закрытие соединения с БД"""
cursor.execute("SELECT steps, time FROM steps WHERE time BETWEEN ? AND ?", (tsStart, tsEnd))
stepsOut = cursor.fetchall()
conn.close()

# Debug
# print(hrOut)
# print(hrOut.__len__())
# print(type(hrOut))
# print(stepsOut)
# print(stepsOut.__len__())
# print(type(stepsOut))

""" Перенос данных из списка в массив, отбросив пустые ячейки """
"""
hrOut[i][1] - проход по пульсу
hrOut[i][0] - проход по ts

stepsOut[i][0] - проход по шагам
stepsOut[i][1] - проход по ts
"""
hrList = [["Date", "Heartrate"]]
hrTemp = []
for i in range(len(hrOut)):
    hrTemp.append(str(datetime.datetime.fromtimestamp(hrOut[i][0])))
    hrTemp.append(hrOut[i][1])
    hrList.append(hrTemp[:])
    hrTemp.clear()

stepsList = [["Date", "Steps"]]
stepsTemp = []
for i in range(len(stepsOut)):
    stepsTemp.append(str(datetime.datetime.fromtimestamp(stepsOut[i][1])))
    stepsTemp.append(stepsOut[i][0])
    stepsList.append(stepsTemp[:])
    stepsTemp.clear()

# Debug
# print(hrList)
# print(len(hrList))
# print(stepsList)
# print(len(stepsList))

"""How not to do"""
"""for i in range(len(hrList)):
    if 10 < i < len(hrList) - 10:
        hrList[i][1] = int((float(hrList[i - 4][1]) + float(hrList[i - 3][1]) + float(hrList[i - 2][1]) + float(
            hrList[i - 1][1]) + float(hrList[i][1]) + float(hrList[i + 1][1]) + float(hrList[i + 2][1]) + float(
            hrList[i + 3][1]) + float(hrList[i + 4][1])) / 9)
"""
myFile = open('hrdata.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(hrList)

myFile = open('stepsdata.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(stepsList)

print("Writing complete")
