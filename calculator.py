from tkinter import *

root = Tk()
root["bg"] = "lightblue"
root.geometry("245x245")
root.title("Калькулятор")
result = StringVar()
expression = ""
expression_field = Entry(text=result, font=("Calibri", 18))
expression_field.grid(columnspan=4, ipadx=0)

a = [['C', 'DEL', 'x^2', '%'], ['1', '2', '3', '*'], ['4', '5', '6', '/'], ['7', '8', '9', '+'], ['0', ',', '=', '-']]
for i in range(len(a)):
    for j in range(len(a[i])):
        Button(text=str(a[i][j]), height=2, width=7, command=lambda x=a[i][j]: press_num(x)).grid(row=i + 2, column=j)

def press_num(num):
    global expression
    if num == '=':
        try:
            total = str(eval(expression))
            result.set(total)
            expression = total
        except:
            result.set('error')
            expression = ''
    elif num == 'C':
        expression = ''
        result.set("")
    else:
        expression += str(num)
        result.set(expression)


root.mainloop()