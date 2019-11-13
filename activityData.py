import csv
import datetime
import sqlite3


def read_convert_db(year, month, day, start_hour, start_minute, end_hour, end_minute):
    """ Установка промежутка,  в который собирается статистика """
    # Указание отметок
    timeStart = datetime.datetime(year,
                                  month,
                                  day,
                                  start_hour,
                                  start_minute)
    timeEnd = datetime.datetime(year,
                                month,
                                day,
                                end_hour,
                                end_minute)

    # Конвертирование в timestamp
    tsStart = int(datetime.datetime.timestamp(timeStart))
    tsEnd = int(datetime.datetime.timestamp(timeEnd))

    """ Запрос списка сердцебиения и подключение к БД """
    conn = sqlite3.connect('data/db21_10_2019_1500_1558.sqlite')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM heartrate WHERE time BETWEEN ? AND ?", (tsStart + 1, tsEnd))
    hrOut = cursor.fetchall()

    """ Запрос списка шагов и закрытие соединения с БД"""
    cursor.execute("SELECT steps, time FROM steps WHERE time BETWEEN ? AND ?", (tsStart, tsEnd))
    steps_out = cursor.fetchall()
    conn.close()

    """ Перенос данных из списка в массив, отбросив пустые ячейки """
    """
    hrOut[i][1] - проход по пульсу
    hrOut[i][0] - проход по ts
    
    steps_out[i][0] - проход по шагам
    steps_out[i][1] - проход по ts
    """
    hr_list = [["Date", "Heartrate"]]
    hr_temp = []
    for i in range(len(hrOut)):
        hr_temp.append(str(datetime.datetime.fromtimestamp(hrOut[i][0])))
        hr_temp.append(hrOut[i][1])
        hr_list.append(hr_temp[:])
        hr_temp.clear()

    steps_list = [["Date", "Steps"]]
    steps_temp = []
    activity_min = []
    for i in range(len(steps_out)):
        ts_to_date = str(datetime.datetime.fromtimestamp(steps_out[i][1]))
        steps_temp.append(ts_to_date)
        steps_temp.append(steps_out[i][0])
        steps_list.append(steps_temp[:])
        steps_temp.clear()
        if int(steps_out[i][0]) > 0:
            activity_min.append(ts_to_date[11:])

    write_flag_hr = False
    write_flag_st = False
    myFile = open('hrdata.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(hr_list)
        write_flag_hr = True

    myFile = open('stepsdata.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(steps_list)
        write_flag_st = True

    return activity_min
