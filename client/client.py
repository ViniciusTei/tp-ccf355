from tkinter import *
from pages import login

if __name__ == '__main__':
  main = Tk()
  main.geometry('750x425')
  main.configure(background="#1C1D2C")
  main.resizable(width=FALSE, height=FALSE)

  # login page
  loginPage = login.loginPage(main, server=None)
  
  loginPage.start()
  
