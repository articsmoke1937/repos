import tkinter.messagebox
from tkinter import *
import University.globals as globals
from tkinter import ttk
import Programs.activity_choice as activity_choice
from University.user_profile import user as up
import University.globals as globals
import University.validation as val
import Programs.activity_choice as activity_choice
import Programs.chucknorris
import Programs.weather
import Programs.stocks
import Programs.rocks_paper_scissors as rocks_paper_scissors
import Programs.admin as admin
import University.validation as validation


userrecognized=True

##########################################
#           Functions                    #


class AppGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = AppGUI(root)
root.mainloop()

def func():#function of the button
    tkinter.messagebox.showinfo(f"Greetings!", f"Welcome\nI'm your host, {globals.cname}")
    welcome_win()
    #tkinter.messagebox.showinfo(f"Greetings!",activity_choice.host_start(userrecognized))



#create 
def welcome_win(): 
    wel_win=Tk() #creating the main window and storing the window object in 'win'
    wel_win.title('Welcome Screen') #setting title of the window
    wel_win.geometry('300x100') #setting the size of the window
    wel_win.destroy

    wel_win.mainloop() #running the loop that works as a trigger
# 
def user_val_win():
    uval_win=Tk()
    uval_win.title("User Validation")
    uval_win.geometry('300x200')
    uval_win.mainloop()
    # Label(uval_win, text= globals.border, height=1, width=20).grid(row=1) 
    # Label(uval_win, text=f'Welcome To My World!', height=1, width=20).grid(row=2) 
    # Label(uval_win, text= globals.border, height=1, width=20).grid(row=3)      
    

##########################################
#          Main Window creation          #
##########################################
main_win=Tk() #creating the main window and storing the window object in 'win'
main_win.title('Do It All Program') #setting title of the window
main_win.geometry('300x100') #setting the size of the window
Label(main_win, text= globals.border, height=1, width=20).grid(row=1) 
Label(main_win, text=f'Welcome To My World!', height=1, width=20).grid(row=2) 
Label(main_win, text= globals.border, height=1, width=20).grid(row=3) 


#set username to last user in logfile
pname=up.last_user(globals.user_log_filename)

#check user name to see if it is in the global user log
user_log=up.username_check(globals.users_file,pname)

#Validate user with validation program
userrecognized,user_id=val.user_validation(user_log,pname)

#Program Start Button
start_program_btn=Button(main_win,activeforeground="blue",bg="lime", text="Start Program", width=10,height=2,command=lambda : validation.user_val_win(pname))
start_program_btn.place(x=195,y=15)

# btn=Button(main_win,activeforeground="blue",bg="lime", text="Start Program", width=10,height=2,command=func)
# btn.place(x=195,y=15)


#Entry Widget
#Label(main_win, text='Welcome To My World!', height=5, width=20).grid(row=3) 
# #Label(main_win, text='Email').grid(row=1) #Add Rows by increasing row count
# ent1 = Entry(main_win) 
# #ent2 = Entry(main_win) 
# ent1.grid(row=0, column=1) 
# #ent2.grid(row=1, column=1) 

main_win.mainloop() #running the loop that works as a trigger