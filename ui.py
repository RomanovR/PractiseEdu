from tkinter import *

import plotlytesting


def read_db():
    print("run activityData.py")


def show_graph():
    print("Show graph")
    plotlytesting.draw_graph()


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
buttonRead.config(command=read_db)

# Кнопка для вывода графика в браузере
buttonShow = Button(root,
                    text='График активности')
buttonShow.grid(row=10,
                column=1,
                sticky=E)
buttonShow.config(command=show_graph)
Label(root, text='     ').grid(row=11,
                               column=0)

root.mainloop()
