from tkinter import *

class Input():
    def __init__(self, parent, label, show=None) -> None:
        self.frame = Frame(parent, bg="#292C3D")

        label = Label(self.frame, text=label, bg="#292C3D", fg="#FFFFFF", cursor="hand2", font=('Roboto 9')).pack(side= TOP, anchor="w")
        self.__entry = Entry(self.frame, show=show)
        self.__entry.pack(side=BOTTOM)

        pass
    
    def getValue(self):
        return self.__entry.get()