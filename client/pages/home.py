from tkinter import *

class HomePage(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)

        headingText = Label(self, text="Home", font="16",bg="#292C3D", fg="#FFFFFF")
        headingText.pack(side=TOP)