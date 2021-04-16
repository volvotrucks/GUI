from tkinter import*
import sqlite3
from tkinter import ttk
from openpyxl.workbook import Workbook #Create workbook in our own
from openpyxl import load_workbook # file that has been already created



def register_user():

	user_info = username.get()
	pw_info = password.get()

	conn = sqlite3.connect('Form.db')
	with conn:
		cursur = conn.cursor()
	cursur.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, password TEXT NOT NULL);")
	cursur.execute('INSERT INTO user(username, password) VALUES(?,?)',(user_info,pw_info))
	conn.commit()
	Label(w2, text = "Registration Success", fg = "green", font = ("calibri",  11)).pack()

def  login_verify():

	while True:
		user1 = user_verify.get()
		pw1 = pw_verify.get()
		with sqlite3.connect("Form.db") as db:
			cursur = db.cursor()
		find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
		cursur.execute(find_user,[(user1), (pw1)])
		result = cursur.fetchall()
		if result:
			import gui


def register():
	global w2
	w2 = Toplevel(w1)
	w2.title("Register")
	w2.geometry("300x250")

	global username
	global password
	global user_entry
	global pw_entry
	username = StringVar()
	password = StringVar()


	Label(w2, text = "Please enter details below ").pack()
	Label(w2, text = "").pack()
	Label(w2, text = "Username Email ").pack()
	user_entry = Entry(w2, textvariable = username)
	user_entry.pack()
	Label(w2, text = "Password ").pack()
	pw_entry = Entry(w2, textvariable = password)
	pw_entry.pack()
	Label(w2, text = "").pack()
	Button(w2, text = "Register", width = 10, height = 1, command = register_user).pack()
def login():
	global w3
	w3 = Toplevel(w1)
	w3.title("Login")
	w3.geometry("300x250")
	Label(w3, text = "Please enter details below ").pack()
	Label(w3, text = "").pack()

	global user_verify
	global pw_verify
	user_verify = StringVar()
	pw_verify = StringVar()

	global user_entry1
	global pw_entry1

	Label(w3, text = "Username Email ").pack()
	user_entry1 = Entry(w3, textvariable = user_verify)
	user_entry1.pack()
	Label(w3, text = "Password ").pack()
	pw_entry1 = Entry(w3, textvariable = pw_verify, show = "*")
	pw_entry1.pack()
	Label(w3, text = "").pack()
	Button(w3, text = "Login", width = 10, height = 1, command = login_verify).pack()

	




def main_window():
	global w1
	w1 = Tk()
	w1.geometry("400x600")
	w1.title("Volvo")
	Label(text ="Volvo's Trucks Home Page", bg = "grey", width ="300", height = "2", font = ("Calibri, 13") ).pack()
	Label(text = " ").pack()
	Button(text = "Login", width ="30", height = "2", command = login).pack()
	Label(text = " ").pack()
	Button(text = "Register", width ="30", height = "2", command = register).pack()

	w1.mainloop()
main_window()

