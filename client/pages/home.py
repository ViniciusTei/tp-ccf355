from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

class HomePage(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)

        buttonSubmit = Button(self, text="Criar lobby", command=self.__handleCreateLobbyButton, bg="#0D9EF1", fg="#FFFFFF", width=12)
        buttonSubmit.place(x=20, y=20)

        self.__lobiesContainer = Frame(self, width=730, height=300)
        self.__lobiesContainer.configure(background="#1C1D2C")
        self.__lobiesContainer.place(x=10, y=50)

        self.__totalLobbies = 0

        # place lobby
        self.__placeLobby(self.__totalLobbies)
        self.__placeLobby(self.__totalLobbies)
        self.__placeLobby(self.__totalLobbies) 
        

    def __handleCreateLobbyButton(self):
        createLobbyFrame = Frame(self, width=300, height=100, bg="#1C1D2C")
        createLobbyFrame.place(x=250, y=50)
        createLobbyFrame.pack_propagate(False)
        Label(createLobbyFrame, text="Selecione o jogo que deseja", background="#1C1D2C", fg="#FFFFFF", font=('Roboto 12')).pack()
        selectedValue = StringVar()
        combobox = ttk.Combobox(createLobbyFrame, textvariable=selectedValue)
        combobox['values'] = ['Counter Strike']
        combobox['state'] = 'readonly'
        combobox.pack(padx=5, pady=5)
        btnFrame = Frame(createLobbyFrame, bg="#1C1D2C")
        btnFrame.pack(side=BOTTOM, pady=10)
        Button(btnFrame, text="Fechar", command=createLobbyFrame.destroy, bg="#0D9EF1", fg="#FFFFFF").grid(row=0, column=0, padx=10)
        buttonSubmit = Button(btnFrame, text="Criar", command=createLobbyFrame.destroy, bg="#0D9EF1", fg="#FFFFFF")
        buttonSubmit.grid(row=0, column=1)
        # combobox.bind('<<ComboboxSelected>>', self.__onChangeSelect)

    def __handleEntryLobby(self):
        print('Entrar lobby')

    def __placeLobby(self, col):
        lobbyFrame = Frame(self.__lobiesContainer, width=158, height=259)
        lobbyFrame.configure(background='#292C3D', highlightbackground="white", highlightthickness=1)
        lobbyFrame.pack_propagate(False)
        headingText = Label(lobbyFrame, text="Time " + str(col), font="16",bg="#292C3D", fg="#FFFFFF")
        headingText.pack(side=TOP, pady=10)

        self.__placeUser(lobbyFrame, 0)
        self.__placeUser(lobbyFrame, 1)
        self.__placeUser(lobbyFrame, 2)
        self.__placeUser(lobbyFrame, 3)
        self.__placeUser(lobbyFrame, 4)

        buttonSubmit = Button(lobbyFrame, text="Entrar", command=self.__handleEntryLobby, bg="#0D9EF1", fg="#FFFFFF")
        buttonSubmit.pack(side=BOTTOM, pady=10)

        lobbyFrame.grid(row=0, column=col, pady=20, padx=10, ipadx=10, ipady=5)

        self.__totalLobbies+=1

    def __placeUser(self, parent, userIndex):
        userFrame = Frame(parent, background='#292C3D')
        image = Image.open(os.getcwd() + '/client/assets/user_images/default.png')
        image = image.resize((28,28), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        labelImage = Label(userFrame, image=photo, background='#292C3D')
        labelImage.image=photo
        labelImage.grid(row=0, column=0)
        userLabel = Label(userFrame, text="Vinicius", background='#292C3D', fg="#FFFFFF")
        userLabel.grid(row=0, column=1)
        userPos = 40 + (userIndex * 35)
        userFrame.place(x=10, y=userPos)