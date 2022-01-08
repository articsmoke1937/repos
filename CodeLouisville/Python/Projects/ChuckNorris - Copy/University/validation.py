import json
from University.user_profile import user as up
import University.globals as g
import tkinter as ttk
import tkinter.messagebox
from tkinter import *
import University.globals as globals
# import GUIMaster as gm

checkin='start'

def yes_press():#function of the button
    userconfirm=1
    print(userconfirm)
    # uval_win.destor
    return(userconfirm)

def no_press():#function of the button
    userconfirm=2
    print(userconfirm)
    # uval_win.destor
    return(userconfirm)

def can_press():#function of the button
    userconfirm=5
    print(userconfirm)
    # uval_win.destor
    return(userconfirm)

def user_val_win(pname):
    uval_win=Tk()
    uval_win.title("User Validation")
    content=ttk.Frame(column=0,row=0)
    mainframe = ttk.Frame(content,column=0,row=0, padding="3 3 12 12")

    content.columnconfigure(0, weight=1)  
    content.rowconfigure(0, weight=1)
    border_label=Label(mainframe, text= globals.border) 
    name_label=Label(mainframe, text=f'Are you {pname}?') 
    border_label=Label(mainframe, text= globals.border) 

    yes_btn=Button(mainframe,text="Yes",command=yes_press)
  
    no_btn=Button(mainframe,text="No",command=no_press)
    
    can_btn=Button(mainframe,text="Cancel",command=uval_win.destroy)
    
    
    #grid Layout
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    # yes_btn.pack(side=LEFT)
    # no_btn.pack(side=LEFT)
    # can_btn.pack(side=LEFT)
    # border_label.pack(side=TOP)
    # name_label.pack(side=BOTTOM)
    border_label.grid(column=0, row=0, columnspan=3)
    name_label.grid(column=1, row=1, columnspan=1)
    yes_btn.grid(column=0, row=3,columnspan=1)
    no_btn.grid(column=1, row=3,columnspan=1)
    can_btn.grid(column=2, row=3,columnspan=1)

    userconfirm=yes_press()
    uval_win.mainloop()
    return(userconfirm)
    
    # Label(uval_win, text= globals.border, height=1, width=20).grid(row=3)     

def user_validation(user_log,pname):
    userconfirm=1
    checkin='start'
    while checkin!='complete':
        if user_log=='y':
            while userconfirm < 3:
                if user_log=='y':
                    # user_val_win(pname)
                    # print(f'Are you {pname}?\n1. Yes\n2. No')
                    # userconfirm=user_val_win
                    # uval_win.
                    if userconfirm==1:
                        user_id=up.user_id_get(g.users_file,pname)[0]
                        user_id,pname,lname,city,age=up.get_user_info(g.users_file,user_id)
                        print(user_id,'test1')##test
                        print(g.border)
                        print(f"Welcome back, {pname} from {city}")
                        userconfirm=3
                        checkin='complete'
                        userrecognized=True
                        break
                    elif userconfirm==2:
                        userrecognized=False
                        user_log='n'
                    break
                else:
                    break
        else:
            userrecognized=False
            print('Please tell me with whom I have the pleasure to speak.')
            print("What is your first name: ")
            pname=input(g.prompt)
            pname=pname.capitalize()
            user_log=up.username_check(g.users_file,pname)
            if user_log=='n':
                # print(user_id)
                user_id=up.user_id_get(g.users_file,pname)[1]
                print(user_id)
                print("You are a new user and we will need to get you set up")
                # up.add_user(users_file,'user_id',0,int(int(new_user_id)+1))       
                # up.add_user(users_file,'first',0,pname)
                with open(g.user_log_filename,'w') as f:
                    json.dump(pname,f)
                user_id,pname,lname,city,age=up.get_new_user_info(g.users_file,user_id,pname)
                dogage=age*8
                print(f'\n{g.border}')
                print(f"Well it is very nice to meet you {pname}.")
                print(f"Did you know that you age in dog years is {dogage}?")
                print(f'{g.border}\nYou have also been added to the Users list')
                print(g.border)
                # userconfirm==2+1
                checkin='complete'
                userrecognized==True
                up.add_user(g.users_file,'user_id',0,user_id)       
                up.add_user(g.users_file,'first',0,pname)
                up.add_user(g.users_file,'last',0,lname)
                up.add_user(g.users_file,'city',0,city)
                up.add_user(g.users_file,'age',0,age)
            elif user_log=='y':
                # print(user_id)
                user_id=up.user_id_get(g.users_file,pname)[0]
                print(user_id)
                user_id,pname,lname,city,age=up.get_user_info(g.users_file,user_id)
                print(user_id,pname,lname,city,age)
                with open(g.user_log_filename,'w') as f:
                    json.dump(pname,f)
                print(g.border)
                print(f'Ohhhh, you have been here before {pname}!')
                print(f'Welcome back!! I hope {city} is treating you well!')
                # userconfirm==2+1
                checkin='complete'
            else:
                break
   
    return(userrecognized,user_id)
