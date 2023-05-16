from tkinter import *
from PIL import ImageTk, Image
import os

import pages.login

class RegisterPage(Frame):
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

        headingFormText = Label(loginFormFrame, text="Faça o seu cadastro", font="16",bg="#292C3D", fg="#FFFFFF")
        headingFormText.pack(side=TOP)

        voltarLink = Label(loginFormFrame, text="voltar", bg="#292C3D", fg="#FFFFFF", cursor="hand2", font=('Roboto 8 underline'))
        voltarLink.place(y=5)
        voltarLink.bind("<Button-1>", lambda e: self.__controller.showFrame(pages.login.LoginPage))

        formFrame = Frame(loginFormFrame, bg="#292C3D")
        formFrame.pack(fill=BOTH, pady=50)