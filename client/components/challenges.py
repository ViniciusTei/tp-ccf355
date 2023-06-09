from tkinter import *

l = [
    {'name': 'TIME_Vinicius'},
    {'name': 'TIME_Matheus'}
]

class ChallengesView(Frame):
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent, height=35)

    def run(self):
        