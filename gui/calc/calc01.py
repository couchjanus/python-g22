from tkinter import *

root = Tk()

root.title("Simple calculator")

# geometry
root.geometry("900x200+40+80")
root.resizable(width=False, height=False)

# entry = Entry(width=50)
entry = Entry()

entry.grid(row=0, column=0, columnspan=4, sticky=N+S+W+E)
entry.config(font='Arial 14', bg='white', fg='blue')

Button(root, text="<=", width = 10, bg='red', fg='white', font='Arial 14').grid(row=0, column = 4)
Button(root, text="C", width = 10, bg='red', fg='white', font='Arial 14').grid(row=0, column = 5)

bttn_list = (
"7", "8", "9", "/", "(",  ")",
"4", "5", "6", "*", "xⁿ", "√2",
"1", "2", "3", "-", "sin", "cos",
"0", ".", "±", "+", "n!", "π", 
 "=")

# Создаем кнопки для калькулятора:

r = 1
c = 0

for i in bttn_list:
    Button(root, text=i, width = 10, bg='blue', fg='white', font='Arial 14').grid(row=r, column = c)
    c += 1
    if c > 5:
        c = 0
        r += 1

# mainloop 
root.mainloop()
