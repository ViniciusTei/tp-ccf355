from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os

from api import API
from pages import HomePage, RegisterPage

class LoginPage(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.__controller = controller

        ## create background with image and logo
        logoImage = Image.open(os.getcwd() + '/client/assets/' + os.listdir('./client/assets')[0])
        logo = ImageTk.PhotoImage(logoImage)
        labelLogo = Label(self, image=logo, background="#1C1D2C")
        labelLogo.image = logo
        labelLogo.place(x=60, y=45)

        ninjaImage = Image.open(os.getcwd() + '/client/assets/' + os.listdir('./client/assets')[1])
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

        Label(formFrame, text="Usuário", font="12",bg="#292C3D", fg="#FFFFFF").pack()
        self.__entryUser = Entry(formFrame)
        self.__entryUser.pack()
        Label(formFrame, text="Senha", font="12",bg="#292C3D", fg="#FFFFFF").pack()
        self.__entryPassword = Entry(formFrame, show="*")
        self.__entryPassword.pack()

        buttonSubmit = Button(formFrame, text="Entrar", command=self.__submit, bg="#0D9EF1", fg="#FFFFFF", width=12)
        buttonSubmit.pack(pady=10)

        link = Label(formFrame, text="Criar nova conta", bg="#292C3D", fg="#FFFFFF", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e: self.__controller.showFrame(RegisterPage))

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
            self.__controller.showFrame(HomePage)
        else:
            messagebox.showerror('Erro', 'Usuário inválido! Tente novamente ou faça um cadastro.')

        

    
    