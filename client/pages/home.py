from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

from api import API 

class HomePage(Frame):
    __games = []
    __selectedGameValue = None
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.__controller = controller

        buttonSubmit = Button(self, text="Criar lobby", command=self.__handleCreateLobbyButton, bg="#0D9EF1", fg="#FFFFFF", width=12)
        buttonSubmit.place(x=20, y=20)

        self.__lobiesContainer = Frame(self, width=730, height=300)
        self.__lobiesContainer.configure(background="#1C1D2C")
        self.__lobiesContainer.place(x=10, y=50)

        self.__totalLobbies = 0

    def run(self):
        response = API().GET('/lobby')
        lobbies = response['lobbies']
        for l in lobbies:
            self.__placeLobby(self.__totalLobbies, l['lobbyid'], l['lobbyname'], l['users'])

    def __handleCreateLobbyButton(self):
        response = API().GET('/games')
        self.__games = response['games']
        gameValues = []
        for game in self.__games:
            gameValues.append(game['name'])

        createLobbyFrame = Frame(self, width=300, height=100, bg='#292C3D', highlightbackground="white", highlightthickness=1)
        createLobbyFrame.place(x=250, y=50)
        createLobbyFrame.pack_propagate(False)
        Label(createLobbyFrame, text="Selecione o jogo que deseja", background="#292C3D", fg="#FFFFFF", font=('Roboto 12')).pack()
        self.__selectedGameValue = StringVar()
        combobox = ttk.Combobox(createLobbyFrame, textvariable=self.__selectedGameValue)
        combobox['values'] = gameValues
        combobox['state'] = 'readonly'
        combobox.pack(padx=5, pady=5)
        btnFrame = Frame(createLobbyFrame, bg="#292C3D")
        btnFrame.pack(side=BOTTOM, pady=10)
        Button(btnFrame, text="Fechar", command=createLobbyFrame.destroy, bg="#0D9EF1", fg="#FFFFFF").grid(row=0, column=0, padx=10)
        buttonSubmit = Button(btnFrame, text="Criar", command=self.__createNewLobby, bg="#0D9EF1", fg="#FFFFFF")
        buttonSubmit.grid(row=0, column=1)
        # combobox.bind('<<ComboboxSelected>>', self.__onChangeSelect)

    def __createNewLobby(self):
        print('criar', self.__controller.user, self.__selectedGameValue.get())

    def __handleEntryLobby(self, lobbyid):
        self.__controller.showFrame('lobby', True, {'lobbyid': lobbyid})

    def __placeLobby(self, col, lobbyid, lobbyName, lobbyUsers):
        lobbyFrame = Frame(self.__lobiesContainer, width=158, height=259)
        lobbyFrame.configure(background='#292C3D', highlightbackground="white", highlightthickness=1)
        lobbyFrame.pack_propagate(False)
        headingText = Label(lobbyFrame, text=lobbyName, font="16",bg="#292C3D", fg="#FFFFFF")
        headingText.pack(side=TOP, pady=10)
        for idx, user in enumerate(lobbyUsers):
            print('lobbyUser', idx, user)
            self.__placeUser(lobbyFrame, idx, user)

        buttonSubmit = Button(lobbyFrame, text="Entrar", command= lambda: self.__handleEntryLobby(lobbyid), bg="#0D9EF1", fg="#FFFFFF")
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