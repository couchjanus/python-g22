from tkinter import *

root = Tk()  # Корневое окно создано

# Размещение виджета задается через аргументы row и column, которым присваиваются соответственно номера строки и столбца. 

Label(text="Input:").grid(row=0, column=0)

Button(text="+").grid(row=1, column=0)
Button(text="-").grid(row=1, column=2)
Button(text="*").grid(row=1, column=3)

# Чтобы объединить ячейки по горизонтали, используется атрибут columnspan, которому присваивается количество объединяемых ячеек. 

table_name = Entry(width=30)

# Опция rowspan объединяет ячейки по вертикали.
table_name.grid(row=0, column=1, columnspan=3)

root.mainloop()
