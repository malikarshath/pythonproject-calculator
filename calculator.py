from tkinter import *
from math import factorial

calc = Tk()
calc.title("calculator")
calc.geometry()

for block in range(6):
    Grid.columnconfigure(calc,block,weight=1)
    Grid.rowconfigure(calc,block,weight=1)

display = Entry(calc)
display.grid(row=0,columnspan=6,sticky='nsew')

Button(calc,text='1',command= lambda :get_variable('1')).grid(row=1,column=0,sticky='nsew')
Button(calc,text='2',command= lambda :get_variable('2')).grid(row=1,column=1,sticky='nsew')
Button(calc,text='3',command= lambda :get_variable('3')).grid(row=1,column=2,sticky='nsew')

Button(calc,text='4',command= lambda :get_variable('4')).grid(row=2,column=0,sticky='nsew')
Button(calc,text='5',command= lambda :get_variable('5')).grid(row=2,column=1,sticky='nsew')
Button(calc,text='6',command= lambda :get_variable('6')).grid(row=2,column=2,sticky='nsew')

Button(calc,text='7',command= lambda :get_variable('7')).grid(row=3,column=0,sticky='nsew')
Button(calc,text='8',command= lambda :get_variable('8')).grid(row=3,column=1,sticky='nsew')
Button(calc,text='9',command= lambda :get_variable('9')).grid(row=3,column=2,sticky='nsew')

Button(calc,text='AC',command= lambda :clear_all()).grid(row=4,column=0,sticky='nsew')
Button(calc,text='0',command= lambda :get_variable('0')).grid(row=4,column=1,sticky='nsew')
Button(calc,text='.',command= lambda :get_variable('.')).grid(row=4,column=2,sticky='nsew')

Button(calc,text='+',command= lambda :get_operation('+')).grid(row=1,column=3,sticky='nsew')
Button(calc,text='-',command= lambda :get_operation('-')).grid(row=2,column=3,sticky='nsew')
Button(calc,text='*',command= lambda :get_operation('*')).grid(row=3,column=3,sticky='nsew')
Button(calc,text='/',command= lambda :get_operation('/')).grid(row=4,column=3,sticky='nsew')

Button(calc,text='pi',command= lambda :get_operation('3.14')).grid(row=1,column=4,sticky='nsew')
Button(calc,text='%',command= lambda :get_operation('%')).grid(row=2,column=4,sticky='nsew')
Button(calc,text='(',command= lambda :get_operation('(')).grid(row=3,column=4,sticky='nsew')
Button(calc,text='exp',command= lambda :get_operation('**')).grid(row=4,column=4,sticky='nsew')

Button(calc,text='<-',command= lambda : undo()).grid(row=1,column=5,sticky='nsew')
Button(calc,text='x!',command= lambda : fact()).grid(row=2,column=5,sticky='nsew')
Button(calc,text=')',command= lambda :get_operation(')')).grid(row=3,column=5,sticky='nsew')
Button(calc,text='^2',command= lambda :get_operation('**2')).grid(row=4,column=5,sticky='nsew')

Button(calc,text='=',command= lambda :calculate()).grid(row=5,columnspan=6,sticky='nsew')

i = 0
def get_variable(num):
    global i
    display.insert(i,num)
    i += 1
def clear_all():
    display.delete(0,END)
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i += length
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except:
        clear_all()
        display.insert(0,"Error")
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")
        
def calculate():
    entire_string = display.get()
    try:
        result = eval(entire_string)
        clear_all()
        display.insert(0,result)
    except:
        clear_all()
        display.insert(0,"Error")
calc.mainloop()
