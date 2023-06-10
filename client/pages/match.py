from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

from api import API

class MatchPage(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.__controller = controller

    def run(self, params):
        response = API().POST('/match-by-id', params)
        lobby1 = self.__createLobby(response['lobby_1']['lobbyname'], response['lobby_1']['users'])
        lobby2 = self.__createLobby(response['lobby_2']['lobbyname'], response['lobby_2']['users'])
        lobby1.pack(side=LEFT, padx=50)
        lobby2.pack(side=RIGHT, padx=50)
        buttonSubmit = Button(self, text="Terminar partida", bg="#0D9EF1", fg="#FFFFFF")
        buttonSubmit.pack(side=BOTTOM, pady=10)
        return None

    def __createLobby(self, lobbyName, lobbyUsers):
        lobbyFrame = Frame(self, width=135, height=259)
        lobbyFrame.configure(background='#292C3D', highlightbackground="white", highlightthickness=1)
        lobbyFrame.pack_propagate(False)
        headingText = Label(lobbyFrame, text=lobbyName, font="16",bg="#292C3D", fg="#FFFFFF")
        headingText.pack(side=TOP, pady=10)
        for idx, user in enumerate(lobbyUsers):
            self.__placeUser(lobbyFrame, idx, user)

        return lobbyFrame

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