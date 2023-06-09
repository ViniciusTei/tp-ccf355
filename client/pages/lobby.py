from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import time

from components import UserView, ChallengesView
from utils import trhead
from service import LobbyService

class LobbyPage(Frame):
    __lobby = None
    __currentPage = 0
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.__controller = controller
        self.__frame = Frame(self, width=200, background="#292C3D")
        self.__lobiesContainer = Frame(self, width=730, height=300)
        self.__lobiesContainer.configure(background="#1C1D2C")
        self.__challengesContainer = Frame(self)
        self.__totalLobbies = 0
        self.__currentTrhead = None
  
    def run(self, params):
        t = trhead.thread_with_trace(target=self.__fetch, args=(params,))
        t.daemon = True
        t.start()
        return t

    def __fetch(self, params):
        while True:
            response_check = LobbyService().checkForChallengers(params['lobbyid'])

            if (response_check['match'] != None):
                if (self.__currentTrhead != None and self.__currentTrhead.is_alive()):
                    self.__currentTrhead.kill()
                self.__controller.showFrame('match', True, {'matchId': response_check['match']})
                break

            response_lobby_page = LobbyService().getLobbyById(params)
            self.__lobby = response_lobby_page['lobby']

            response_all_lobies = LobbyService().getLobbyPerPage(self.__currentPage)
            lobbies = response_all_lobies['lobbies']

            if (self.__currentTrhead != None and self.__currentTrhead.is_alive()):
                self.__currentTrhead.kill()

            # create my challenges frame
            self.__challengesContainer.destroy()
            self.__challengesContainer = ChallengesView(self, self.__controller, self.__lobby['lobbyid'])
            # self.__challengesContainer.configure(background="#1C1D2C")
            self.__challengesContainer.pack(fill=X, side=TOP)
            self.__currentTrhead = self.__challengesContainer.run()

            # create left frame with current lobby
            self.__frame.destroy()
            self.__frame = Frame(self, width=215, background="#292C3D")
            self.__frame.pack(fill=Y, side=LEFT)
            self.__frame.pack_propagate(False)
            Label(self.__frame, text=self.__lobby['lobbyname'], background="#292C3D", fg="#FFFFFF", font=('Roboto 12')).pack(pady=10)
            
            for idx, user in enumerate(self.__lobby['users']):
                u = UserView(self.__frame, userName=user['username'], userImage=user['userimage'])
                pos = u.calculatePos(idx)
                u.place(x=10, y=pos)
            
            buttonSubmit = Button(self.__frame, text="Deixar sala", command=self.__handleLeave, bg="#F46275", fg="#FFFFFF")
            buttonSubmit.pack(side=BOTTOM, pady=30)

            # create all lobbies to challenge
            self.__lobiesContainer.destroy()
            self.__lobiesContainer = Frame(self, width=730, height=300)
            self.__lobiesContainer.configure(background="#1C1D2C")
            self.__lobiesContainer.pack(fill=X, side=LEFT)
            
            for l in lobbies:
                self.__placeLobby(self.__totalLobbies, l['lobbyid'], l['lobbyname'], l['users'])
            
            time.sleep(8)

    def __handleLeave(self):
        response = LobbyService().leaveLobby(self.__lobby['lobbyid'], self.__controller.user['id'])

        if response['status'] == 200:
            self.__frame.destroy()
            self.__controller.showFrame('home', True)
        else:
            messagebox.showerror('Erro', response['message'])

    def __placeLobby(self, col, lobbyid, lobbyName, lobbyUsers):
        lobbyFrame = Frame(self.__lobiesContainer, width=135, height=259)
        lobbyFrame.configure(background='#292C3D', highlightbackground="white", highlightthickness=1)
        lobbyFrame.pack_propagate(False)
        headingText = Label(lobbyFrame, text=lobbyName, font="16",bg="#292C3D", fg="#FFFFFF")
        headingText.pack(side=TOP, pady=10)
        for idx, user in enumerate(lobbyUsers):
            self.__placeUser(lobbyFrame, idx, user)

        buttonSubmit = Button(lobbyFrame, text="Desafiar", command= lambda: self.__handleChallenge(lobbyid), bg="#0D9EF1", fg="#FFFFFF")
        buttonSubmit.pack(side=BOTTOM, pady=10)

        lobbyFrame.grid(row=0, column=col, pady=20, padx=10, ipadx=10, ipady=5)

        self.__totalLobbies+=1
    
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

    def __handleChallenge(self, lobbyid):
        response = LobbyService().acceptChallenger(self.__lobby['lobbyid'], lobbyid)

        if response['status'] == 200:
            messagebox.showinfo('Sucesso!', response['message'])
        else:
            messagebox.showerror('Erro!', response['message'])

