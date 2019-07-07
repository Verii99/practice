from tkinter import *
from tkinter import messagebox
import postgresql
root = Tk()
root.geometry("300x200")
root.title("Войти в систему")

def login():
    text_enter_login = Label(text="Введите логин:")
    enter_login = Entry()
    text_enter_password = Label(text="Введите пароль:")
    enter_password = Entry(show="*")
    button_enter = Button(text="Войти")
    text_enter_login.pack()
    enter_login.pack()
    text_enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_enter.pack()

login()
root.mainloop()
