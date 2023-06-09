# Python class para criar uma aplicao com 
# multiplas paginas com tkinter
# o codigo para essa aplicao pode ser encontrado aqui
# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

from tkinter import *
from PIL import ImageTk, Image
import os

from pages import HomePage, LoginPage, RegisterPage, PerfilPage, LobbyPage, MatchPage

layouts = (LoginPage, RegisterPage, HomePage, PerfilPage, LobbyPage, MatchPage)

map_layouts = {
  'login': LoginPage,
  'register': RegisterPage,
  'home': HomePage,
  'perfil': PerfilPage,
  'lobby': LobbyPage,
  'match': MatchPage
}

class App(Tk):
  user = None

  def __init__(self, *args, **kwargs):
    Tk.__init__(self, *args, **kwargs)

    # create main container
    container = Frame(self)
    container.configure(background="#1C1D2C")
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(1, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.__menu = Frame(container, height=20, background="#1C1D2C")
    self.__menu.grid(row=0, column=0, sticky="nsew")
    self.__menu.grid_remove()
    logoImage = Image.open(os.getcwd() + '/client/assets/Logo.png')
    logoImage = logoImage.resize((145,45), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logoImage)
    labelLogo = Label(self.__menu, image=logo, background="#1C1D2C")
    labelLogo.image = logo
    labelLogo.place(x=20, y=10)

    menuItemHome = Label(self.__menu, text="Inicio", bg="#1C1D2C", fg="#0D9EF1", cursor="hand2", font=('Roboto 10'))
    menuItemHome.place(x=500, y=25)
    menuItemHome.bind("<Button-1>", lambda e: self.showFrame('home', True))
    
    menuItemHistory = Label(self.__menu, text="Histórico", bg="#1C1D2C", fg="#0D9EF1", cursor="hand2", font=('Roboto 10'))
    menuItemHistory.place(x=560, y=25)
    menuItemHistory.bind("<Button-1>", lambda e: self.showFrame('home', True))
    
    menuItemProfile = Label(self.__menu, text="Perfil", bg="#1C1D2C", fg="#0D9EF1", cursor="hand2", font=('Roboto 10'))
    menuItemProfile.place(x=640, y=25)
    menuItemProfile.bind("<Button-1>", lambda e: self.showFrame('perfil', True))
    
    menuItemLeave = Label(self.__menu, text="Sair", bg="#1C1D2C", fg="#0D9EF1", cursor="hand2", font=('Roboto 10'))
    menuItemLeave.place(x=700, y=25)
    menuItemLeave.bind("<Button-1>", lambda e: self.showFrame('login'))

    self.__pages = {}

    for p in layouts:
      frame = p(container, self)
      frame.configure(background="#1C1D2C")
      self.__pages[p] = frame

      frame.grid(row=1, column=0, sticky="nsew")

    self.showFrame('login')

  def showFrame(self, cont, showMenu=False, pageParams=None):
    if showMenu:
      self.__placeMenu()
    else:
      self.__menu.grid_remove()
    
    if cont not in map_layouts.keys():
      print('Page not found!')
      return

    layout = map_layouts[cont]

    frame = self.__pages[layout]
    frame.tkraise()

    if hasattr(frame, 'run'):
      if pageParams:
        frame.run(pageParams)
      else:
        frame.run()

  def __placeMenu(self):
    self.__menu.grid(row=0, column=0, sticky="nsew")