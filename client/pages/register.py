from tkinter import *

class RegisterPage(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)

        headingText = Label(self, text="Faça o seu cadastro", font="16",bg="#292C3D", fg="#FFFFFF")
        headingText.pack(side=TOP)