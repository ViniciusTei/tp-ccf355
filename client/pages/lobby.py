from tkinter import *

from api import API
from components import UserView

class LobbyPage(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.__controller = controller
        self.__frame = Frame(self, width=250, background="#292C3D")

    def run(self, params):
        response = API().POST('/lobby-by-id', params)
        lobby = response['lobby']

        self.__frame = Frame(self, width=250, background="#292C3D")
        self.__frame.pack(fill=Y, side=LEFT)
        self.__frame.pack_propagate(False)
        Label(self.__frame, text=lobby['lobbyname'], background="#292C3D", fg="#FFFFFF", font=('Roboto 12')).pack(pady=10)
        
        for idx, user in enumerate(lobby['users']):
            u = UserView(self.__frame, userName=user['username'], userImage=user['userimage'])
            pos = u.calculatePos(idx)
            u.place(x=10, y=pos)
        
        buttonSubmit = Button(self.__frame, text="Deixar sala", command=self.__handleLeave, bg="#F46275", fg="#FFFFFF")
        buttonSubmit.pack(side=BOTTOM, pady=30)

    def __handleLeave(self):
        self.__frame.destroy()
        self.__controller.showFrame('home', True)
        
