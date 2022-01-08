import tkinter as ttk
from tkinter import *

class start_gui:
    def __init__(self, master):
        self.master = master
        master.title("Do Everything Program")

        self.label = Label(master, text="Welcome to My World!!!")
        self.label.pack()

        self.start_button = Button(master, text="Start Program", command=self.greet)
        self.start_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()