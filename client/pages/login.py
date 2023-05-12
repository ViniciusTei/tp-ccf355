from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os

import api

class Login:
    def  __init__(self, window, server):
        self.window = window
        self.server = server
        ## create background with image and logo
        logoImage = Image.open(os.getcwd() + '/client/assets/' + os.listdir('./client/assets')[0])
        ninjaImage = Image.open(os.getcwd() + '/client/assets/' + os.listdir('./client/assets')[1])

        logo = ImageTk.PhotoImage(logoImage)
        labelLogo = Label(self.window, image=logo, background="#1C1D2C")
        labelLogo.image = logo
        
        labelLogo.place(x=60, y=40)

        ninja = ImageTk.PhotoImage(ninjaImage)

        labelNinja = Label(self.window, image=ninja, background="#1C1D2C")
        labelNinja.image = ninja
        
        labelNinja.place(x=90, y=200)

        ## login form
        loginFormFrame = Frame(self.window, bg="#292C3D", bd=10, width=295, height=328)
        loginFormFrame.pack(side=RIGHT, padx=45)
        loginFormFrame.pack_propagate(False)

        headingFormText = Label(loginFormFrame, text="Faça o login", font="16",bg="#292C3D", fg="#FFFFFF")
        headingFormText.pack(side=TOP)

        formFrame = Frame(loginFormFrame, bg="#292C3D")
        formFrame.pack(fill=BOTH, side=BOTTOM, pady=80)

        Label(formFrame, text="Usuário", font="12",bg="#292C3D", fg="#FFFFFF").pack()
        self.entryUser = Entry(formFrame)
        self.entryUser.pack()
        Label(formFrame, text="Senha", font="12",bg="#292C3D", fg="#FFFFFF").pack()
        self.entryPassword = Entry(formFrame, show="*")
        self.entryPassword.pack()

        buttonSubmit = Button(formFrame, text="Entrar", command=self.submit, bg="#0D9EF1", fg="#FFFFFF", width=12, height=60)
        buttonSubmit.pack(pady=10)

        
    def start(self):
        self.window.mainloop()

    def submit(self):
        user = self.entryUser.get()
        password = self.entryPassword.get()
        
        payload = {
            "username": user,
            "password": password
        }

        apiInstance = api.API()
        response = apiInstance.POST('/session', payload)
        print('from server', response)

def loginPage(root, server):
    return Login(root, server)

    
    