from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

class ImageSelect:
    def __init__(self, parent) -> None:
        self.frame = Frame(parent, bg="#292C3D")

        image = Image.open(os.getcwd() + '/client/assets/user_images/default.png')
        image = image.resize((60,60), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.__label = Label(self.frame, image=photo)
        self.__label.image=photo
        self.__label.pack(side=TOP)

        self.__selectedValue = StringVar()
        combobox = ttk.Combobox(self.frame, textvariable=self.__selectedValue, width=8)
        combobox['values'] = ['default.png', 'avatar.png']
        combobox['state'] = 'readonly'
        combobox.pack(side=BOTTOM,padx=5, pady=5)
        combobox.set('default.png')
        combobox.bind('<<ComboboxSelected>>', self.__onChangeSelect)
        pass
    
    def get(self):      
        return self.__selectedValue.get()
    
    def __onChangeSelect(self, event):
        selectedImage = self.get()
        self.__label.destroy()
        self.__placeImage(selectedImage)

    def __placeImage(self, image):
        image = Image.open(os.getcwd() + '/client/assets/user_images/' + image)
        image = image.resize((60,60), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.__label = Label(self.frame, image=photo)
        self.__label.image=photo
        self.__label.pack(side=TOP)