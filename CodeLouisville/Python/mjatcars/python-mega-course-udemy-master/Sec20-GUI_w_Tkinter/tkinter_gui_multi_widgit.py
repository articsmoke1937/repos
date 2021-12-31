from tkinter import *

window=Tk()

def conv():
    print(e1_value.get())
    gm=float(e1_value.get())*1.6
    t1.insert(END,gm)

    lb=float(e1_value.get())*1.8
    t2.insert(END,lb)

    oz=float(e1_value.get())*2.0
    t3.insert(END,oz)


e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",command=conv)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()
