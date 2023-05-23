from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os

from api import API 
from components import Input, ImageSelect

class PerfilPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        self.__controller = controller

        loginFormFrame = Frame(self, bg="#292C3D", bd=10, width=295, height=328)
        loginFormFrame.pack( padx=45)
        loginFormFrame.pack_propagate(False)

        headingFormText = Label(loginFormFrame, text="Perfil", font="16",bg="#292C3D", fg="#FFFFFF")
        headingFormText.pack(side=TOP)

        voltarLink = Label(loginFormFrame, text="voltar", bg="#292C3D", fg="#FFFFFF", cursor="hand2", font=('Roboto 8 underline'))
        voltarLink.place(y=5)
        voltarLink.bind("<Button-1>", lambda e: self.__controller.showFrame('home', True))

        formFrame = Frame(loginFormFrame, bg="#292C3D")
        formFrame.pack(fill=BOTH, pady=35)
        formFrame.grid_rowconfigure(3, weight=1)
        formFrame.grid_columnconfigure(0, weight=1)

        self.__entryUserImage = ImageSelect(formFrame)
        self.__entryUserImage.frame.grid(row=1, column=1, rowspan=2, padx=10)
        
        self.__entryUser = Input(formFrame, label="Alterar nome de usuário")
        self.__entryUser.frame.grid(row=1, column=0)
        
        self.__entryPassword = Input(formFrame, label="Alterar senha", show="*")
        self.__entryPassword.frame.grid(row=2, column=0)

        self.__entryConfirmPassword = Input(formFrame, label="Confirmar Senha", show="*")
        self.__entryConfirmPassword.frame.grid(row=3, column=0)

        buttonSubmit = Button(formFrame, text="Salvar",command =self.__submit, bg="#0D9EF1", fg="#FFFFFF", width=12)
        buttonSubmit.grid(row=4, column=0, columnspan=2, pady=10)

    def __submit(self):
        user = self.__entryUser.get()
        password = self.__entryPassword.get()
        payload = {
            "username":user,
            "password":password
        }

        apiIntance = API()
        response = apiIntance.POST('/update', payload)
        print('from server', response)

        if(response['status']==200):
            self.__controller.showFrame('home', True)
        else:
            messagebox.showerror('Erro','Erro ao alterar os seus dados tente novamente mais tarde')