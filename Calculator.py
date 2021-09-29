from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Калькулятор')

memory = 0

def calc(key):
    global memory
    str1 = "-+*./0123456789"
    if key == '=':
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, '=' + str(result))
        except ZeroDivisionError:
            calc_entry.delete(0, END)
            messagebox.showerror('Ошибка!', 'На ноль делить нельзя!')
        except:
            calc_entry.delete(0, END)
            messagebox.showerror('Ошибка!', 'Проверь правильность данных!')
    elif key == 'C':
        calc_entry.delete(0, END)
    elif key == '+/-':
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        elif calc_entry.get()[0] == '-':
            calc_entry.delete(0)
        else:
            calc_entry.insert(0, '-')
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

bttn_list = [
    '7','8','9', '+', '-',
    '4','5','6', '*', '/',
    '1','2','3', '+/-', '=',
    '0', '.', 'C'
]

r=1
c=0
for i in bttn_list:
    rel=''
    cmd=lambda x=i: calc(x)
    Button(root, text=i, height=2, width=10, command=cmd).grid(row=r, column=c)
    c+=1
    if c>4:
        c=0
        r+=1

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0,column=0,columnspan=5)

root.mainloop()