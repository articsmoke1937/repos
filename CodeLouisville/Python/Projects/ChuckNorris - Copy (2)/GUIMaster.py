import tkinter.messagebox
from tkinter import *
import University.globals as globals
from tkinter import ttk
import json
from University.user_profile import user as up
import University.globals as g
from University.validation import user_validation
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox

LargeFont = ("Verdana", 12)

def options():
    print ('''\n**************************************************************
          Welcome to the GUI interface of the python program
**************************************************************''')

# Main GUI class.  Holds up entire program interface
class app_gui:
    print("Greetings!p")
    def __init__(self, master):
        self.master = master
        master.title("Do Everything Program")
        self.label = Label(master, text="Welcome to My World!!!")
        self.label.pack()

        self.start_button = Button(master, text="Start Program", command=self.start)
        self.start_button.pack()

        self.close_button = Button(master, text="Close", command=master.destroy)
        self.close_button.pack()
 
 #Start program with app window loop
    def start():
        print("Greetings!")
        start=PageContainer()
        start.mainloop()
        # start=program.cndiapprogram

####################
#  Validate user or create new user
#  Show other window frames based off selection
# User to select if they want to validate current user or create a new user
#################3##
class validation_page(tk.Frame):    
   
   #Print Welcome message and first menu
	def __init__(self, parent, controller):
		print("Greetings!2")
		tk.Frame.__init__(self, parent)   
		label = tk.Label(self, text=f"Welcome to My World", font = LargeFont)
		label.pack(pady=10,padx=10)
        
		yes_btn = tk.Button(self, text = "Validate Current User",
			command = lambda: controller.show_frame(validate_user), width = 20, height = 1)     
        
		no_user_btn = tk.Button(self, text = "New User",
		 	command = lambda: controller.show_frame(user_check), width = 20, height = 1)    

		exit_btn = tk.Button(self, text = "Cancel",
			command =controller.destroy, width = 20, height = 1)
		
		yes_btn.pack()
		no_user_btn.pack()
		exit_btn.pack()

        
#Validate user to confirm that they are last user logged in.  If not enter credentials
# , this will check if user exists, if yes, then program starts, if not, new user is created
class validate_user(tk.Frame):
	print("Greetings3!")
	#set username to last user in logfile
	g.pname=up.last_user(globals.user_log_filename)
	
	#check user name to see if it is in the global user log
	user_log=up.username_check(globals.users_file,g.pname)
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)   
		label = tk.Label(self, text=f"Are you {g.pname}?", font = LargeFont)
		label.pack(pady=10,padx=10)

		val_btn = tk.Button(self, text = "Yes",
			command = lambda: [self.user_val_yes(parent,controller),controller.show_frame(StartPage)], width = 20, height = 1)     
        
		new_user_btn = tk.Button(self, text = "No",
		 	command = lambda: controller.show_frame(user_check), width = 20, height = 1)    

		back_to_main_menu_btn = tk.Button(self, text = "Back to Main Menu",
			command = lambda: controller.show_frame(validation_page), width = 20, height = 1)
		
		val_btn.pack()
		new_user_btn.pack()
		back_to_main_menu_btn.pack()
	
	def user_val_yes(self,parent,controller):
		g.user_id=user_add_gui.user_id_get()[0]
		g.user_id,g.pname,g.lname,g.city,g.age=user_add_gui.get_user_info_org(g.users_file,g.user_id)
		tkinter.messagebox.showinfo("Do It All Program",f'{g.border}\nWelcome back {g.pname} from {g.city}!!!!\n{g.border}')
		lambda: controller.show_frame(user_check)


class user_check(tk.Frame):	
	print("Greetings!4")
	def __init__(self,parent,controller):
		tk.Frame.__init__(self, parent)   
		intro_label = tk.Label(self, text=f'Well I need to know who you are!', font = LargeFont)
		intro_label.pack(pady=5,padx=5)
		get_name_label=tk.Label(self,text="Please enter your first name:")
		get_name_label.pack(pady=10,padx=10)
		
		#Get Username entry
		get_username=tk.Entry(self)
		get_username.pack(pady=5,padx=5)
		# g.pname=get_username.get()
		# g.pname=g.pname.capitalize()
		# with open(g.user_log_filename,'w') as f:
		# 		json.dump(g.pname,f)

		submit_btn = tk.Button(self, text = "Submit",
		 	command = lambda: [self.submit_name(controller,get_username)], width = 20, height = 1)

		back_to_main_menu_btn = tk.Button(self, text = "Back to Main Menu",
			command = lambda: controller.show_frame(validation_page), width = 20, height = 1)
		
		submit_btn.pack()
		back_to_main_menu_btn.pack()
	

	def submit_name(self,controller,get_username):
		#set g.pname variable to captured username
		g.pname=get_username.get()
		g.pname=g.pname.capitalize()
		with open(g.user_log_filename,'w') as f:
				json.dump(g.pname,f)
		self.user_check_val(controller)


	def user_check_val(self,controller):
		user_log=up.username_check(g.users_file,g.pname)
		if user_log=='n':
			g.user_id=up.user_id_get(g.users_file,g.pname)[1]
			setup_label=tk.Label(self, text=f'You are a new user\nso we will need to get you set up, {g.pname}',font=LargeFont)
			setup_label.pack(pady=5,padx=5)
			submit_btn = tk.Button(self, text = "OK",command =  lambda: controller.show_frame(user_add_gui), width = 20, height = 1)
			submit_btn.pack()
		
		elif user_log=='y':
			g.user_id=up.user_id_get(g.users_file,g.pname)[0]
			g.user_id,g.pname,g.lname,g.city,g.age=up.get_user_info(g.users_file,g.user_id)
			with open(g.user_log_filename,'w') as f:
				json.dump(g.pname,f)
			messagebox.showinfo('infromation',f'{g.border}\nOhhhh, you have been here before {g.pname}!\nWelcome back!! I hope {g.city} is treating you well!')
		
			submit_btn = tk.Button(self, text = "OK",command =  lambda: controller.show_frame(StartPage), width = 20, height = 1)
			submit_btn.pack()

class user_add_gui(tk.Frame):
	print("Greetings!5")
	def __init__(self,parent,controller):
		tk.Frame.__init__(self, parent)
		
		greeting_label=tk.Label(self,text=f'Please provide the information requested below {g.pname}',font=LargeFont)
		greeting_label.pack(pady=5,padx=5)
	
		firstname_get_label = tk.Label(self, text=f'First Name {g.pname}', font = LargeFont)
		firstname_get_label.pack(pady=5,padx=5)
		
		lastname_get_label = tk.Label(self, text=f'Last Name', font = LargeFont)
		lastname_get_label.pack(pady=5,padx=5)
		lastname_get_entry=tk.Entry(self)
		lastname_get_entry.pack(pady=5,padx=5)

		age_get_label = tk.Label(self, text=f'Age', font = LargeFont)
		age_get_label.pack(pady=5,padx=5)
		age_get_entry=tk.Entry(self)
		age_get_entry.pack(pady=5,padx=5)

		city_get_label = tk.Label(self, text=f'City', font = LargeFont)
		city_get_label.pack(pady=5,padx=5)
		city_get_entry=tk.Entry(self)
		city_get_entry.pack(pady=5,padx=5)
 		
		# lambda:self.get_user_info(firstname_get_entry,lastname_get_entry,age_get_entry,city_get_entry)
		save_btn = tk.Button(self, text = "Save",command =  lambda:[self.get_user_info(lastname_get_entry,age_get_entry,city_get_entry,controller),controller.show_frame(user_add_confirmation)], width = 20, height = 1)
		save_btn.pack()
	
	#Set user information from entry fields and print confirmation and add Ok button	
	def get_user_info(self,lastname_get_entry,age_get_entry,city_get_entry,controller):
		self.lastname_set(lastname_get_entry)
		self.age_set(age_get_entry)
		self.city_set(city_get_entry)
		self.update_users_file()
		# messagebox.showinfo('infromation',f'You have officially been setup, {g.pname}!\nWelcome to My World!!\nLet us have some fun!')
		# lambda:controller.show_frame(user_add_confirmation)
		# setup_label=tk.Label(self, text=f'Your User is setup, {g.pname}!!',font=LargeFont)
		# setup_label.pack(pady=5,padx=5)
		# submit_btn = tk.Button(self, text = "OK",command =  lambda: controller.show_frame(StartPage), width = 20, height = 1)
		# submit_btn.pack()

	##################
	# set user information to global variables
	###################

	def lastname_set(self,lastname_get_entry):
		g.lname=lastname_get_entry.get()
		g.lname=g.lname.capitalize()
		print(g.lname)

	def age_set(self,age_get_entry):
		g.age=age_get_entry.get()
		g.age=g.age.capitalize()

	def city_set(self,city_get_entry):
		g.city=city_get_entry.get()
		g.city=g.city.capitalize()

	def user_id_get():
		with open(g.users_file) as open_user_file:
			username_check=json.load(open_user_file)
		user_id=-1
		new_user_id=0
		for x in username_check['first'][0]:
			if x != g.pname:
				user_id=int(user_id)+1
				new_user_id=int(user_id)+1 
			else:
				break
		user_id=int(user_id)+1
		return user_id, new_user_id
#Get updated user information
	def get_user_info_org(user_file,user_id):
		with open(user_file) as open_user_file:
			username_check=json.load(open_user_file)
			print(g.user_id)
			user_id_get=username_check['user_id'][0][int(user_id)]
			pname=username_check['first'][0][(user_id)]
			lname=username_check['last'][0][(user_id)]
			city=username_check['city'][0][(user_id)]
			age=username_check['age'][0][(user_id)]
		return user_id_get,pname,lname,city,age
	# Save User Information to json file	
	def add_user(user_file, key,v1,value):
		with open(user_file) as f:
			users_file_decoded=json.load(f)
			users_file_decoded[key][v1].append(value)
		json.dump(users_file_decoded, open(user_file, 'w'))

	#save user inforamtion to user file	
	def update_users_file(self):
		# print(g.user_id,g.pname,g.lname,g.city,g.age)
		up.add_user(g.users_file,'user_id',0,g.user_id)       
		up.add_user(g.users_file,'first',0,g.pname)
		up.add_user(g.users_file,'last',0,g.lname)
		up.add_user(g.users_file,'city',0,g.city)
		up.add_user(g.users_file,'age',0,g.age)

class user_add_confirmation(tk.Frame):
	print("Greetings!6")
	def __init__(self,parent,controller):
		tk.Frame.__init__(self, parent)
		print(g.pname,'init33')  
		confirm_label=tk.Label(self,text=f'Your information has been saved {g.pname}!',font=LargeFont)
		confirm_label.pack(pady=5,padx=5)
		submit_btn = tk.Button(self, text = "OK",command =  lambda: controller.show_frame(StartPage), width = 20, height = 1)
		submit_btn.pack()

class PageContainer(tk.Tk):  
	print("Greetings!7")
	def __init__(self, *args, **kwargs):  
		# options()
		tk.Tk.__init__(self, *args, **kwargs)
		# tk.Tk.iconbitmap(self,default="ico_image.ico")  

		container = tk.Frame(self)  
		tk.Tk.geometry(self,'500x500')  
		container.pack(side='top', fill='both', expand = True )     
		# container.title('Do Everything Program')
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frame = {}

		for F in (validation_page,validate_user,user_check,user_add_gui,user_add_confirmation,StartPage, chuck_norris,stock_program,rocks_paper_scissors,Project_4, Project_5,Project_6,Project_7):

			frame = F(container, self)

			self.frame[F] = frame

			frame.grid(row = 0, column = 0, sticky = "nsew") 

		# self.show_frame(validation_page)

	def show_frame(self, cont):

		frame = self.frame[cont]    
		frame.tkraise()    

class StartPage(tk.Frame):    
	print("Greetings8!")
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)   
		label = tk.Label(self, text="Welcome To My World", font = LargeFont)
		label.pack(pady=10,padx=10)
		button1 = tk.Button(self, text = "Chuck Norris Jokes",
			command = lambda: controller.show_frame(chuck_norris), width = 20, height = 1)     
		button2 = tk.Button(self, text = " Stock Program ",
			command = lambda: controller.show_frame(stock_program), width = 20, height = 1)
		button3 = tk.Button(self, text = "Rocks Papers Scissors",
			command = lambda: controller.show_frame(rocks_paper_scissors), width = 20, height = 1)
		button4 = tk.Button(self, text = "Project4",
			command = lambda: controller.show_frame(Project_4), width = 20, height = 1)
		button5 = tk.Button(self, text = "    Project5    ",
			command = lambda: controller.show_frame(Project_5), width = 20, height = 1)
		button6 = tk.Button(self, text = "Projec6    ",
			command = lambda: controller.show_frame(Project_6), width = 20, height = 1)
		button7 = tk.Button(self, text = "Projec7",
			command = lambda: controller.show_frame(Project_7), width = 20, height = 1)
		button1.pack()
		button2.pack()
		button3.pack()
		button4.pack()
		button5.pack()
		button6.pack()
		button7.pack()

class chuck_norris(tk.Frame):
	print("Greetings8!")
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Chuck Norris Jokes", font = LargeFont)
		label.pack(pady=10,padx=10)
		# button1 = tk.Button(self, text = "Data Load",
		# 	command = data_load_all_proj, width = 25, height = 1)
		# button1.pack()
		# button2 = tk.Button(self, text = "Create QR Image",
		# 	command = generate_qr_code, width = 25, height = 1)
		# button2.pack()
		# button3 = tk.Button(self, text = "Generate Report",
		# 	command = generate_report, width = 25, height = 1)
		# button3.pack()
		# button4 = tk.Button(self, text = "Freeze Data",
		# 	command = freeze_data, width = 25, height = 1)
		# button4.pack()
		# button5 = tk.Button(self, text = "Delete Data",
		# 	command = delete_data, width = 25, height = 1)
		# button5.pack()
		# button6 = tk.Button(self, text = "Generate Revenue Report",
		# 	command = generate_revenue_report, width = 25, height = 1)
		# button6.pack()
		# button7 = tk.Button(self, text = "Back to Main Menu",
		# 	command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
		# button7.pack()

class stock_program(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Stock Program", font = LargeFont)
		label.pack(pady=10,padx=10)
		# button1 = tk.Button(self, text = "Data Load",
		# 	command = data_load_all_proj, width = 25, height = 1)
		# button1.pack()
		# button2 = tk.Button(self, text = "Create QR Image",
		# 	command = generate_qr_code, width = 25, height = 1)
		# button2.pack()
		# button3 = tk.Button(self, text = "Generate Report",
		# 	command = generate_report, width = 25, height = 1)
		# button3.pack()
		# button4 = tk.Button(self, text = "Freeze Data",
		# 	command = freeze_data, width = 25, height = 1)
		# button4.pack()
		# button5 = tk.Button(self, text = "Delete Data",
		# 	command = delete_data, width = 25, height = 1)
		# button5.pack()
		# button6 = tk.Button(self, text = "Generate Revenue Report",
		# 	command = generate_revenue_report, width = 25, height = 1)
		# button6.pack()
		# button7 = tk.Button(self, text = "Back to Main Menu",
		# 	command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
		# button7.pack()

class rocks_paper_scissors(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Rocks Papers Scissors", font = LargeFont)
		label.pack(pady=10,padx=10)
		# button1 = tk.Button(self, text = "Data Load",
		# 	command = data_load_all_proj, width = 25, height = 1)
		# button1.pack()
		# button2 = tk.Button(self, text = "Create QR Image",
		# 	command = generate_qr_code, width = 25, height = 1)
		# button2.pack()
		# button3 = tk.Button(self, text = "Generate Report",
		# 	command = generate_report, width = 25, height = 1)
		# button3.pack()
		# button4 = tk.Button(self, text = "Freeze Data",
		# 	command = freeze_data, width = 25, height = 1)
		# button4.pack()
		# button5 = tk.Button(self, text = "Delete Data",
		# 	command = delete_data, width = 25, height = 1)
		# button5.pack()
		# button6 = tk.Button(self, text = "Generate Revenue Report",
		# 	command = generate_revenue_report, width = 25, height = 1)
		# button6.pack()
		# button7 = tk.Button(self, text = "Back to Main Menu",
		# 	command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
		# button7.pack()

class Project_4(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Project 4", font = LargeFont)
		label.pack(pady=10,padx=10)
		# button1 = tk.Button(self, text = "Data Load",
		# 	command = data_load_all_proj, width = 25, height = 1)
		# button1.pack()
		# button2 = tk.Button(self, text = "Create QR Image",
		# 	command = generate_qr_code, width = 25, height = 1)
		# button2.pack()
		# button3 = tk.Button(self, text = "Generate Report",
		# 	command = generate_report, width = 25, height = 1)
		# button3.pack()
		# button4 = tk.Button(self, text = "Freeze Data",
		# 	command = freeze_data, width = 25, height = 1)
		# button4.pack()
		# button5 = tk.Button(self, text = "Delete Data",
		# 	command = delete_data, width = 25, height = 1)
		# button5.pack()
		# button6 = tk.Button(self, text = "Generate Revenue Report",
		# 	command = generate_revenue_report, width = 25, height = 1)
		# button6.pack()
		# button7 = tk.Button(self, text = "Back to Main Menu",
		# 	command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
		# button7.pack()


class Project_5(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Project 5", font = LargeFont)
		label.pack(pady=10,padx=10)
		# button1 = tk.Button(self, text = "Data Load",
		# 	command = data_load_all_proj, width = 25, height = 1)
		# button1.pack()
		# button2 = tk.Button(self, text = "Create QR Image",
		# 	command = generate_qr_code, width = 25, height = 1)
		# button2.pack()
		# button3 = tk.Button(self, text = "Generate Report",
		# 	command = generate_report, width = 25, height = 1)
		# button3.pack()
		# button4 = tk.Button(self, text = "Freeze Data",
		# 	command = freeze_data, width = 25, height = 1)
		# button4.pack()
		# button5 = tk.Button(self, text = "Delete Data",
		# 	command = delete_data, width = 25, height = 1)
		# button5.pack()
		# button6 = tk.Button(self, text = "Generate Revenue Report",
		# 	command = generate_revenue_report, width = 25, height = 1)
		# button6.pack()
		# button7 = tk.Button(self, text = "Back to Main Menu",
		# 	command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
		# button7.pack()

class Project_6(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Project 6", font = LargeFont)
		label.pack(pady=10,padx=10)
		# button1 = tk.Button(self, text = "Data Load",
		# 	command = data_load_all_proj, width = 25, height = 1)
		# button1.pack()
		# button2 = tk.Button(self, text = "Create QR Image",
		# 	command = generate_qr_code, width = 25, height = 1)
		# button2.pack()
		# button3 = tk.Button(self, text = "Generate Report",
		# 	command = generate_report, width = 25, height = 1)
		# button3.pack()
		# button4 = tk.Button(self, text = "Freeze Data",
		# 	command = freeze_data, width = 25, height = 1)
		# button4.pack()
		# button5 = tk.Button(self, text = "Delete Data",
		# 	command = delete_data, width = 25, height = 1)
		# button5.pack()
		# button6 = tk.Button(self, text = "Generate Revenue Report",
		# 	command = generate_revenue_report, width = 25, height = 1)
		# button6.pack()
		# button7 = tk.Button(self, text = "Back to Main Menu",
		# 	command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
		# button7.pack()

class Project_7(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Project 7", font = LargeFont)
		label.pack(pady=10,padx=10)
		# button1 = tk.Button(self, text = "Data Load",
		# 	command = data_load_all_proj, width = 25, height = 1)
		# button1.pack()
		# button2 = tk.Button(self, text = "Create QR Image",
		# 	command = generate_qr_code, width = 25, height = 1)
		# button2.pack()
		# button3 = tk.Button(self, text = "Generate Report",
		# 	command = generate_report, width = 25, height = 1)
		# button3.pack()
		# button4 = tk.Button(self, text = "Freeze Data",
		# 	command = freeze_data, width = 25, height = 1)
		# button4.pack()
		# button5 = tk.Button(self, text = "Delete Data",
		# 	command = delete_data, width = 25, height = 1)
		# button5.pack()
		# button6 = tk.Button(self, text = "Generate Revenue Report",
		# 	command = generate_revenue_report, width = 25, height = 1)
		# button6.pack()
		# button7 = tk.Button(self, text = "Back to Main Menu",
		# 	command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
		# button7.pack()

# def data_load_all_proj():
# 	var0 = tkSimpleDialog.askstring("Data Load","Please enter the month and year(mm-yyyy): ")
# 	tkMessageBox.showinfo("Message", "Please place the master file in specific folder")
# 	var1 = tkSimpleDialog.askstring("Data Load","Do you want to start loading master data? ")
# 	tkMessageBox.showinfo("Message", "Please place the files in specific folder")
# 	var2 = tkSimpleDialog.askstring("Data Load","Do you want to start loading data? (Y/N): ")
# 	tkMessageBox.showinfo("Message", "Please wait while the data is loading")
# 	master_data(var0,var1,var2)

# def master_data(var0,var1,var2):
# 	print(var0, var1, var2)

# def generate_qr_code():
# 	var0 = tkSimpleDialog.askstring("QR IRN Generate","Please enter the Invoice month and year(mm-yyyy): ")
# 	tkMessageBox.showinfo("Message", "Please wait while the QR IRN is generating")
# 	create_qr_image(var0)

# def create_qr_image(var0):
# 	print(var0)

# def generate_report():
# 	var0 = tkSimpleDialog.askstring("Generate Invoice","Please enter the Invoice month and year(mm-yyyy): ")
# 	tkMessageBox.showinfo("Message", "Please wait while the Invoice is gettting generated")
# 	generate_invoice(var0)

# def generate_invoice(var0):
# 	print(var0)

# def freeze_data():
# 	var0 = tkSimpleDialog.askstring("Freeze data","Please enter the Invoice month and year(mm-yyyy): ")
# 	tkMessageBox.showinfo("Message", "Please wait while the data is being freezed")
# 	freeze_data_function_call(var0)

# def freeze_data_function_call(var0):
# 	print(var0)

# def delete_data():
# 	var0 = tkSimpleDialog.askstring("Delete data","Please enter the Invoice month and year(mm-yyyy): ")
# 	tkMessageBox.showinfo("Message", "Please wait while the data is being deleted")
# 	delete_data_function_call(var0)

# def delete_data_function_call(var0):
# 	print(var0)

# def generate_revenue_report():
# 	var0 = tkSimpleDialog.askstring("Delete data","Please enter the Invoice month and year(mm-yyyy): ")
# 	tkMessageBox.showinfo("Message", "Please wait while the MIS Revenue Report is being generated")
# 	generate_revenue_report_function_call(var0)

# def generate_revenue_report_function_call(var0):
# 	print(var0)



# app = PageContainer()
# app.mainloop()   

 
    # def user_val_win(self,master,g.pname):
    #     self.master = master
    #     self.label = Label(master, text=f'Are you {g.pname}')
    #     self.label.pack()

    #     self.start_button = Button(master, text="Yes", command=lambda: master.close)
    #     self.start_button.pack()

    #     self.close_button = Button(master, text="Close", command=self.close or master.destroy)
        # self.close_button.pack()

# class user_val:
#     def user_validation():
#         userconfirm=1
#         checkin='start'
#         while checkin!='complete':
#             if user_log=='y':
#                 while userconfirm < 3:
#                     if user_log=='y':
#                         if userconfirm==1:
#                             user_id=up.user_id_get(g.users_file,g.pname)[0]
#                             user_id,g.pname,g.lname,city,age=up.get_user_info(g.users_file,user_id)
#                             print(user_id,'test1')##test
#                             print(g.border)
#                             print(f"Welcome back, {g.pname} from {city}")
#                             userconfirm=3
#                             checkin='complete'
#                             userrecognized=True
#                             break
#                         elif userconfirm==2:
#                             userrecognized=False
#                             user_log='n'
#                         break
#                     else:
#                         break
#             # else:
#             #     userrecognized=False
#             #     print('Please tell me with whom I have the pleasure to speak.')
#             #     print("What is your first name: ")
#             #     g.pname=input(g.prompt)
#             #     g.pname=g.pname.capitalize()
#             #     user_log=up.username_check(g.users_file,g.pname)
#             #     if user_log=='n':
#             #         # print(user_id)
#             #         user_id=up.user_id_get(g.users_file,g.pname)[1]
#             #         print(user_id)
#             #         print("You are a new user and we will need to get you set up")
#             #         # up.add_user(users_file,'user_id',0,int(int(new_user_id)+1))       
#             #         # up.add_user(users_file,'first',0,g.pname)
#             #         with open(g.user_log_filename,'w') as f:
#             #             json.dump(g.pname,f)
#             #         user_id,g.pname,g.lname,city,age=up.get_new_user_info(g.users_file,user_id,g.pname)
#             #         dogage=age*8
#             #         print(f'\n{g.border}')
#             #         print(f"Well it is very nice to meet you {g.pname}.")
#             #         print(f"Did you know that you age in dog years is {dogage}?")
#             #         print(f'{g.border}\nYou have also been added to the Users list')
#             #         print(g.border)
#             #         # userconfirm==2+1
#             #         checkin='complete'
#             #         userrecognized==True
#             #         up.add_user(g.users_file,'user_id',0,user_id)       
#             #         up.add_user(g.users_file,'first',0,g.pname)
#             #         up.add_user(g.users_file,'last',0,g.lname)
#             #         up.add_user(g.users_file,'city',0,city)
#             #         up.add_user(g.users_file,'age',0,age)
#             #     elif user_log=='y':
#             #         # print(user_id)
#             #         user_id=up.user_id_get(g.users_file,g.pname)[0]
#             #         print(user_id)
#             #         user_id,g.pname,g.lname,city,age=up.get_user_info(g.users_file,user_id)
#             #         print(user_id,g.pname,g.lname,city,age)
#             #         with open(g.user_log_filename,'w') as f:
#             #             json.dump(g.pname,f)
#             #         print(g.border)
#             #         print(f'Ohhhh, you have been here before {g.pname}!')
#             #         print(f'Welcome back!! I hope {city} is treating you well!')
#             #         # userconfirm==2+1
#         #     #         checkin='complete'
#         #         else:
#         #             break
    
#         # return(userrecognized,user_id)



# main_win=Tk() #creating the main window and storing the window object in 'win'
# main_win.title('Do It All Program') #setting title of the window
# main_win.geometry('300x100') #setting the size of the window

# def func():#function of the button
#     tkinter.messagebox.showinfo(f"Greetings!", f"Hello! Welcome to Do It All Progarm.\nI'm your host, {globals.cname}")
#     #tkinter.messagebox.showinfo(f"Greetings!",activity_choice.host_start(userrecognized))

# #Button Widget
# btn=Button(main_win,activeforeground="blue",bg="lime", text="Start Program", width=10,height=2,command=func)
# btn.place(x=195,y=15)

# #Entry Widget
# Label(main_win, text='Name').grid(row=0) 
# #Label(main_win, text='Email').grid(row=1) #Add Rows by increasing row count
# ent1 = Entry(main_win) 
# #ent2 = Entry(main_win) 
# ent1.grid(row=0, column=1) 
# #ent2.grid(row=1, column=1) 

# main_win.mainloop() #running the loop that works as a trigger