import os.path
from tkinter import *

import activitydata
import showgraphs


def check_read_db_event():
    year = int(entryYear.get())
    month = int(entryMonth.get())
    day = int(entryDay.get())
    start_hour = int(entryStartHour.get())
    start_minute = int(entryStartMinute.get())
    end_hour = int(entryEndHour.get())
    end_minute = int(entryEndMinute.get())
    s_er = '''Введите корректную дату и время.'''

    if year in range(2013, 2099) and month in range(1, 12) and day in range(1, 31):
        if start_hour in range(0, 23) and end_hour in range(0, 23):
            if start_minute in range(0, 59) and end_minute in range(0, 59):
                check = activitydata.read_convert_db(year,
                                                     month,
                                                     day,
                                                     start_hour,
                                                     start_minute,
                                                     end_hour,
                                                     end_minute)
                list_min = "Время физической активности " + str(len(check)) + " мин."
                show_message(list_min)
            else:
                show_message(s_er)
        else:
            show_message(s_er)
    else:
        show_message(s_er)


def check_graph_file_event():
    if os.path.exists("hrdata.csv") and os.path.exists("stepsdata.csv"):
        showgraphs.draw_graph()
    else:
        s_er = '''Не найден hrdata.csv или stepsdata.csv'''
        show_message(s_er)


def show_message(text):
    error_file = Tk()
    m_error_file = Message(error_file,
                           width=200,
                           text=text,
                           font="Helvetica 13")
    m_error_file.pack(expand=True, fill=BOTH)
    error_file.title("Message")
    error_file.resizable(False, False)
    error_file.mainloop()


root = Tk()
root.title('Активность ученика')
root.resizable(False, False)
# первая метка в строке 0, столбце 0 (0 по умолчанию)
# парамет sticky  означает выравнивание. W,E,N,S — запад, восток, север, юг
Label(root,
      text='Дата занятия:',
      font='Helvetica 13').grid(row=0)
Label(root,
      text='год',
      font='Helvetica 13').grid(row=1,
                                sticky=E)

# Год занятия
entryYear = Entry(root,
                  width=4,
                  font='Helvetica 13')
entryYear.grid(row=1,
               column=1,
               sticky=W)
entryYear.insert(END, '2019')
Label(root, text='месяц').grid(row=3,
                               column=0,
                               sticky=E)

# Месяц занятия
entryMonth = Entry(root,
                   width=2,
                   font='Helvetica 13')
entryMonth.grid(row=3,
                column=1,
                sticky=W)
entryMonth.insert(END, '10')
Label(root, text='день').grid(row=4,
                              column=0,
                              sticky=E)

# День занятия
entryDay = Entry(root,
                 width=2,
                 font='Helvetica 13')
entryDay.grid(row=4,
              column=1,
              sticky=W)

entryDay.insert(END, '21')

# Блок начала занятия
Label(root, text=' Начало занятия:').grid(row=5,
                                          column=0)

# Час начала занятия
entryStartHour = Entry(root,
                       width=2,
                       font='Helvetica 13')
entryStartHour.grid(row=6,
                    column=0,
                    sticky=E)
entryStartHour.insert(END, '13')
# Минуты начала занятия
entryStartMinute = Entry(root,
                         width=2,
                         font='Helvetica 13')
entryStartMinute.grid(row=6,
                      column=1,
                      sticky=W)
entryStartMinute.insert(END, '37')

# Блок конца занятия
Label(root, text=' Конец занятия:').grid(row=7,
                                         column=0)
# Час конца занятия
entryEndHour = Entry(root,
                     width=2,
                     font='Helvetica 13')
entryEndHour.grid(row=8,
                  column=0,
                  sticky=E)
entryEndHour.insert(END, '16')
# Минуты конца занятия
entryEndMinute = Entry(root,
                       width=2,
                       font='Helvetica 13')
entryEndMinute.grid(row=8,
                    column=1,
                    sticky=W)
entryEndMinute.insert(END, '30')

Label(root, text='     ').grid(row=9,
                               column=0)
# Кнопка для чтения БД
buttonRead = Button(root,
                    text='Поиск перерывов')
buttonRead.grid(row=10,
                column=0,
                sticky=E)
buttonRead.config(command=check_read_db_event)

# Кнопка для вывода графика в браузере
buttonShow = Button(root,
                    text='График активности')
buttonShow.grid(row=10,
                column=1,
                sticky=E)
buttonShow.config(command=check_graph_file_event)
Label(root, text='     ').grid(row=11,
                               column=0)

root.mainloop()
