from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

from api import API
from components import UserView

class LobbyPage(Frame):
    __lobby = None
    __currentPage = 0
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.__controller = controller
        self.__frame = Frame(self, width=200, background="#292C3D")
        self.__lobiesContainer = Frame(self, width=730, height=300)
        self.__lobiesContainer.configure(background="#1C1D2C")
        self.__totalLobbies = 0
        

  
    def run(self, params):
        response = API().POST('/lobby-by-id', params)
        self.__lobby = response['lobby']
        response2 = API().POST('/lobby-by-page', {'page': self.__currentPage})
        lobbies = response2['lobbies']
        print("TESTESTESTEESTTSETSETEST", response2)
        print("TESTESTESTEESTTSETSETEST22222222222222222", response)

        self.__lobiesContainer.destroy()
        self.__lobiesContainer = Frame(self, width=730, height=300)
        self.__lobiesContainer.configure(background="#2fdaaa")
        self.__lobiesContainer.place(x=10, y=50)
        self.__frame = Frame(self, width=250, background="#292C3D")
        self.__frame.pack(fill=Y, side=LEFT)
        self.__frame.pack_propagate(False)
        Label(self.__frame, text=self.__lobby['lobbyname'], background="#292C3D", fg="#FFFFFF", font=('Roboto 12')).pack(pady=10)
        
        for idx, user in enumerate(self.__lobby['users']):
            u = UserView(self.__frame, userName=user['username'], userImage=user['userimage'])
            pos = u.calculatePos(idx)
            u.place(x=10, y=pos)
        
        buttonSubmit = Button(self.__frame, text="Deixar sala", command=self.__handleLeave, bg="#F46275", fg="#FFFFFF")
        buttonSubmit.pack(side=BOTTOM, pady=30)
        for l in lobbies:
            print("entrei no forzin\n")
            self.__placeLobby(self.__totalLobbies, l['lobbyid'], l['lobbyname'], l['users']) 
                
    def __lobbysFrame(self):

        self.__frameLobbys = Frame(self.__frame,width=500,height=500, background="#FFF")
        self.__frameLobbys.pack(side=RIGHT)
        self.__frameLobbys.pack_propagate(False)
        Label(self.__frameLobbys, text=self.__lobby['lobbyname'], background="#292C3D", fg="#FFFFFF", font=('Roboto 12')).pack(pady=10)


        
    def __placeLobby(self, col, lobbyid, lobbyName, lobbyUsers):
        lobbyFrame = Frame(self.__lobiesContainer, width=158 , height=259)
        lobbyFrame.configure(background='#292C3D', highlightbackground="white", highlightthickness=1)
        lobbyFrame.pack_propagate(False)
        lobbyFrame.pack(side=RIGHT)
        lobbyFrame.grid(row =0, column =1 ,padx=10,pady=10)
        headingText = Label(lobbyFrame, text=lobbyName, font="16",bg="#292C3D", fg="#FFFFFF")
        headingText.pack(side=TOP, pady=10)
        buttonSubmit = Button(lobbyFrame, text="Desafiar", bg="#0D9EF1", fg="#FFFFFF")
        for idx, user in enumerate(lobbyUsers):
            self.__placeUser(lobbyFrame, idx, user)


    def __handleLeave(self):
        response = API().POST('/lobby-leave', {'lobbyid': self.__lobby['lobbyid'], 'userid': self.__controller.user['id']})

        if response['status'] == 200:
            self.__frame.destroy()
            self.__controller.showFrame('home', True)
        else:
            messagebox.showerror('Erro', response['message'])
    
    def __placeUser(self, parent, userIndex, user):
        userFrame = Frame(parent, background='#292C3D')
        image = Image.open(os.getcwd() + '/client/assets/user_images/' + user['userimage'])
        image = image.resize((28,28), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        labelImage = Label(userFrame, image=photo, background='#292C3D')
        labelImage.image=photo
        labelImage.grid(row=0, column=0)
        userLabel = Label(userFrame, text=user['username'], background='#292C3D', fg="#FFFFFF")
        userLabel.grid(row=0, column=1)
        userPos = 40 + (userIndex * 35)
        userFrame.place(x=10, y=userPos)


