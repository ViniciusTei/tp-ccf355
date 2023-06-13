from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os

from components import Input, ImageSelect
from service import SessionService

class RegisterPage(Frame):
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

        headingFormText = Label(loginFormFrame, text="Faça o seu cadastro", font="16",bg="#292C3D", fg="#FFFFFF")
        headingFormText.pack(side=TOP)

        voltarLink = Label(loginFormFrame, text="voltar", bg="#292C3D", fg="#FFFFFF", cursor="hand2", font=('Roboto 8 underline'))
        voltarLink.place(y=5)
        voltarLink.bind("<Button-1>", lambda e: self.__controller.showFrame('login'))

        formFrame = Frame(loginFormFrame, bg="#292C3D")
        formFrame.pack(fill=BOTH, pady=35)
        formFrame.grid_rowconfigure(3, weight=1)
        formFrame.grid_columnconfigure(0, weight=1)

        self.__entryUserImage = ImageSelect(formFrame)
        self.__entryUserImage.frame.grid(row=1, column=1, rowspan=2, padx=10)

        self.__entryUser = Input(formFrame, label="Usuário")
        self.__entryUser.frame.grid(row=1, column=0)

        self.__entryPassword = Input(formFrame, label="Senha", show="*")
        self.__entryPassword.frame.grid(row=2, column=0)

        self.__entryConfirmPassword = Input(formFrame, label="Confirmar Senha", show="*")
        self.__entryConfirmPassword.frame.grid(row=3, column=0)

        buttonSubmit = Button(formFrame, text="Cadastrar", command=self.__submit, bg="#0D9EF1", fg="#FFFFFF", width=12)
        buttonSubmit.grid(row=4, column=0, columnspan=2, pady=10)

    def __submit(self):
        username = self.__entryUser.get()
        password = self.__entryPassword.get()
        confirmPassword = self.__entryConfirmPassword.get()
        image = self.__entryUserImage.get()

        if password != confirmPassword:
            messagebox.showerror('Erro', 'As senhas precisam ser iguais!')
        else:
            response = SessionService().createUser(username, password, image)

            if (response['status'] == 200):
                self.__controller.user = response['user']
                self.__controller.showFrame('home', True)
            else:
                messagebox.showerror('Erro', 'Tente novamente mais tarde.')

        