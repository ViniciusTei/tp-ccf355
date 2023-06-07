from tkinter import *
from PIL import ImageTk, Image
import os

map_icons = {
    'next': '/client/assets/next.png',
    'back': '/client/assets/back.png'
}

class IconButton(Label):
    def __init__(self, parent, icon, onClick) -> None:
        if icon not in map_icons.keys():
          print('Icon not found!')
          pass

        imageIcon = Image.open(os.getcwd() + map_icons[icon])
        imageIcon = imageIcon.resize((16,16), Image.ANTIALIAS)
        photoIcon = ImageTk.PhotoImage(imageIcon)
        Label.__init__(self, parent, image=photoIcon, bg="#474C6B", cursor= "hand2")
        self.image=photoIcon

        if (onClick):
          self.bind('<Button-1>', lambda e: onClick)

        pass