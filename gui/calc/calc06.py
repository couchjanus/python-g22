from tkinter import *
from tkinter import messagebox

class Calc:
    def __init__(self, master):
        """Constructor method"""

        master.title('Simple calculator')
        master.geometry()
        
        self.e = Entry(master, bg='white', fg='blue', font='Arial 14')
        self.e.grid(row=0, column=0, columnspan=4, sticky=N+S+W+E, pady=3)
        entry = Entry()

        self.e.focus_set() # Sets focus on the input text area
        
        Button(master, text='c', width = 10, bg='red', fg='white', font='Arial 14', command=lambda : self.clear()).grid(row=0, column = 4)
        Button(master, text='CA', width = 10, bg='red', fg='white', font='Arial 14', command=lambda: self.clearall()).grid(row=0, column = 5)

        bttn_list = (
        "7", "8", "9", "/", "(",  ")",
        "4", "5", "6", "*", "xⁿ", "√2",
        "1", "2", "3", "-", "sin", "cos",
        "0", ".", "±", "+", "n!", "π", 
        )

        # Создаем кнопки для калькулятора:

        r = 1
        c = 0
        for i in bttn_list:
            cmd=lambda x=i: self.action(x)
            
            Button(master, text=i, width=10, bg='blue', fg='white', font='Arial 14', command=cmd).grid(row=r, column = c)
            c += 1
            if c > 5:
                c = 0
                r += 1
        
        Button(master, text='=', bg='red', fg='white', font='Arial 14', width=20, command=lambda:self.equals()).grid(row=5, columnspan=2, column=0, sticky=N+S+W+E)
    
    def action(self, val):
        """pressed button's value is inserted into the end of the text area"""

        self.e.insert(END, val)

    def clearall(self):
        """when clear button is pressed,clears the text input area"""

        self.e.delete(0,END)
    
    def clear(self):
        self.txt=self.e.get()[:-1]
        self.e.delete(0,END)
        self.e.insert(0,self.txt)

    def equals(self):
        """when the equal button is pressed"""

        self.expression = self.e.get()
        ops = "-+0123456789.*/)("
        if self.expression[0] not in ops:
            self.e.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")

        try:
            self.value= eval(self.expression) #evaluate the expression using the eval function
        except SyntaxError or NameErrror:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        except ZeroDivisionError:
            self.e.delete(0,END)
            self.e.insert(0,'Division by zero!')
            messagebox.showerror("ZeroDivisionError!", "Division by zero!")
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)

# Main
root = Tk()
obj=Calc(root) # object instantiated
root.mainloop()


