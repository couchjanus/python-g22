from tkinter import *

# За создание окна отвечает класс Tk()
# Этот экземпляр принято называть root.

root = Tk()  # Корневое окно создано

# b1 = Button(text="Изменить", width=15, height=3)

button1=Button(root, text='Button', width=25, height=5, bg='black', fg='red', font='arial 14')

# кнопку необходимо разместить в окне. 
# Для этого, в Tkinter используются упаковщики

button1.pack()

# Entry - это виджет для ввода одной строки текста. 

# borderwidth - ширина border - позволяет регулировать ширину границы
# bd - сокращение от borderwidth
# width - задаёт длину элемента в знакоместах.
# show - задает отображаемый символ.

entry1=Entry(root, bd=2, width=30, bg='white', fg='red', font='Arial 14')

entry1.pack()


# Свойство font (шрифт):

l1 = Label(text="Машинное обучение", font="Arial 32")
l2 = Label(text="Распознавание образов", font=("Comic Sans MS", 24, "bold"))

l1.config(bd=12, bg='#ffaaaa')
l2.config(bd=12, bg='#aaffff')
l1.pack()
l2.pack()


# создаём виджет
closeButton = Button(root)

# конфигурируем виджет после создания
closeButton.configure(text="Close", fg="Red", bg="Yellow", font="Arial 24")
closeButton.pack(side=RIGHT, padx=15, pady=15)

okButton = Button()
# также можно использовать квадратные скобки:
okButton['text'] = "OK"
okButton['font'] = "Arial 24"
okButton['fg'] = "Green"
okButton.pack(side=RIGHT)

# title - заголовок окна
root.title("Simple Application")

# поместить окно в точку с координатам 300,300 и установить размер в 500x350
root.geometry("500x350+300+300")

# minsize и maxsize - минимальный / максимальный размер окна. Методы принимают два аргумента - ширина и высота окна. Если аргументы не указаны - возвращают текущее значение.

root.minsize(325, 230)
# размер окна может быть изменён только по горизонтали
root.resizable(True, False) 

# iconify / deiconify - свернуть / развернуть окно
root.iconify() 

# state

print(root.state())

# overrideredirect - указание оконному менеджеру игнорировать это окно. Аргументом является True или False. В случае, если аргумент не указан - получаем текущее значение. Если аргумент равен True, то такое окно будет показано оконным менеджером без обрамления (без заголовка и рамки). Может быть использовано, например, для создания splashscreen при старте программы.

# withdraw - "спрятать" (сделать невидимым) окно. Для того, чтобы снова показать его, надо использовать метод deiconify.

# Метод mainloop() объекта Tk запускает главный цикл обработки событий
root.mainloop()
