from tkinter import *
from PIL import ImageTk, Image
import os

class UserView(Frame):
    def  __init__(self, parent, userName, userImage):
        Frame.__init__(self, parent, background='#292C3D')

        image = Image.open(os.getcwd() + '/client/assets/user_images/' + userImage)
        image = image.resize((28,28), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        labelImage = Label(self, image=photo, background='#292C3D')
        labelImage.image=photo
        labelImage.grid(row=0, column=0)
        userLabel = Label(self, text=userName, background='#292C3D', fg="#FFFFFF")
        userLabel.grid(row=0, column=1)
      
    def calculatePos(self, idx):
        return 40 + (idx * 35)