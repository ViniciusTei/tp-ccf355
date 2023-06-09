from tkinter import *
import threading
import time

l = [
    {'name': 'TIME_Vinicius'},
    {'name': 'TIME_Matheus'}
]

class ChallengesView(Frame):
    __challenges = []
    def  __init__(self, parent, controller):
        Frame.__init__(self, parent, background='#292C3D', height=35)
        Label(self, text="Desafios ativos:   ", bg="#292C3D", fg="#FFFFFF", cursor="hand2", font=('Roboto 8')).pack(side=LEFT)

    def run(self):
        t = threading.Thread(target=self.__fetchChallenges)
        t.start()

    def __fetchChallenges(self):
        while True:
            #TODO: get challenges from api
            challenges = l
            for c in self.__challenges:
                if (c):
                    c.destroy()
            
            for lobby in challenges:
                l_frame = Frame(self)
                l_frame.configure(background='#292C3D', highlightbackground="white", highlightthickness=1)
                time_name = Label(l_frame, text=lobby['name'], bg="#292C3D", fg="#FFFFFF", cursor="hand2", font=('Roboto 8'))
                time_name.pack(side=LEFT)
                btn_aceitar = Button(l_frame, text="V", command=self.__handleAccept, bg="#0D9EF1", fg="#FFFFFF", width=4)
                btn_rejeitar = Button(l_frame, text="X", command=self.__handleReject, bg="#F46275", fg="#FFFFFF", width=4)
                btn_aceitar.pack(side=LEFT,padx=8)
                btn_rejeitar.pack(side=LEFT)

                l_frame.pack(side=LEFT)
                self.__challenges.append(l_frame)
            
            time.sleep(8)

    def __handleAccept(self):
        print('Accept')

    def __handleReject(self):
        print('Reject')