from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

from api import API

class MatchPage(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.__controller = controller