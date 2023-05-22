from tkinter import *

from api import API 

class LobbyPage(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text="Lobby", background="#292C3D", fg="#FFFFFF", font=('Roboto 12')).pack()

    def run(self, params):
        print('Lobby params', params)