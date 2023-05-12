# Python class para criar uma aplicao com 
# multiplas paginas com tkinter
# o codigo para essa aplicao pode ser encontrado aqui
# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

from tkinter import *

from pages import HomePage, LoginPage, RegisterPage

layouts = (LoginPage, RegisterPage, HomePage)

class App(Tk):
  def __init__(self, *args, **kwargs):
    Tk.__init__(self, *args, **kwargs)

    # create main container
    container = Frame(self)
    container.configure(background="#1C1D2C")
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.__pages = {}

    for p in layouts:
      frame = p(container, self)
      frame.configure(background="#1C1D2C")
      self.__pages[p] = frame

      frame.grid(row=0, column=0, sticky="nsew")

    self.showFrame(LoginPage)

  def showFrame(self, cont):
    frame = self.__pages[cont]
    frame.tkraise()