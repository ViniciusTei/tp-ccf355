from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os

from api import API 
from components import Input

class LoginPage(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.__controller = controller

        ## create background with image and logo
        logoImage = Image.open(os.getcwd() + '/client/assets/Logo.png')
        logo = ImageTk.PhotoImage(logoImage)
        labelLogo = Label(self, image=logo, background="#1C1D2C")
        labelLogo.image = logo
        labelLogo.place(x=60, y=45)

        ninjaImage = Image.open(os.getcwd() + '/client/assets/ninja.png')
        ninja = ImageTk.PhotoImage(ninjaImage)
        labelNinja = Label(self, image=ninja, background="#1C1D2C")
        labelNinja.image = ninja
        labelNinja.place(x=60, y=200)

        # login form
        loginFormFrame = Frame(self, bg="#292C3D", bd=10, width=295, height=328)
        loginFormFrame.pack(side=RIGHT, padx=45)
        loginFormFrame.pack_propagate(False)

        headingFormText = Label(loginFormFrame, text="Faça o login", font="16",bg="#292C3D", fg="#FFFFFF")
        headingFormText.pack(side=TOP)

        formFrame = Frame(loginFormFrame, bg="#292C3D")
        formFrame.pack(fill=BOTH, pady=50)

        self.__entryUser = Input(formFrame, label="Usuário")
        self.__entryUser.frame.pack()

        self.__entryPassword = Input(formFrame, label="Senha", show="*")
        self.__entryPassword.frame.pack()

        buttonSubmit = Button(formFrame, text="Entrar", command=self.__submit, bg="#0D9EF1", fg="#FFFFFF", width=12)
        buttonSubmit.pack(pady=10)

        link = Label(formFrame, text="Criar nova conta", bg="#292C3D", fg="#FFFFFF", cursor="hand2", font=('Roboto 8 underline'))
        link.pack()
        link.bind("<Button-1>", lambda e: self.__controller.showFrame('register'))

    def __submit(self):
        user = self.__entryUser.get()
        password = self.__entryPassword.get()
        
        payload = {
            "username": user,
            "password": password
        }

        apiInstance = API()
        response = apiInstance.POST('/session', payload)
        print('from server', response)
        # messagebox.showinfo('Info', response)

        if (response['status'] == 200):
            self.__controller.user = response['user']
            self.__controller.showFrame('home', True)
        else:
            messagebox.showerror('Erro', 'Usuário inválido! Tente novamente ou faça um cadastro.')

        

    
    