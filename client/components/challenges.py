from tkinter import *
from tkinter import messagebox
import threading
import time

from service import ChallengesService

class ChallengesView(Frame):
    __challenges = []
    def  __init__(self, parent, controller, lobbyid):
        Frame.__init__(self, parent, background='#292C3D', height=35)
        Label(self, text="Desafios ativos:   ", bg="#292C3D", fg="#FFFFFF", cursor="hand2", font=('Roboto 8')).pack(side=LEFT)
        self.__lobbyid = lobbyid
        self.__controller = controller

    def run(self):
        t = threading.Thread(target=self.__fetchChallenges)
        t.daemon = True
        t.start()
        return t

    def __fetchChallenges(self):
        while True:
            response = ChallengesService().getChallenges(self.__lobbyid)
            print(response)
            challenges = response['lobbies']
            for c in self.__challenges:
                if (c):
                    c.destroy()
            
            for lobby in challenges:
                l_frame = Frame(self)
                l_frame.configure(background='#292C3D', highlightbackground="white", highlightthickness=1)
                time_name = Label(l_frame, text=lobby['name'], bg="#292C3D", fg="#FFFFFF", cursor="hand2", font=('Roboto 8'))
                time_name.pack(side=LEFT)
                btn_aceitar = Button(l_frame, text="V", command= lambda: self.__handleAccept(lobby['lobbyid']), bg="#0D9EF1", fg="#FFFFFF", width=4)
                btn_rejeitar = Button(l_frame, text="X", command= lambda: self.__handleReject(lobby['lobbyid']), bg="#F46275", fg="#FFFFFF", width=4)
                btn_aceitar.pack(side=LEFT,padx=8)
                btn_rejeitar.pack(side=LEFT)

                l_frame.pack(side=LEFT)
                self.__challenges.append(l_frame)
            
            time.sleep(8)

    def __handleAccept(self, id):
        response = ChallengesService().acceptChallenge(self.__lobbyid, id)

        if response['status'] == 200:
            self.__controller.showFrame('match', True, {'matchId': response['match']})
        else:
            messagebox.showerror('Erro', response['message'])

    def __handleReject(self, id):
        response = ChallengesService().rejectChallenge(self.__lobbyid, id)

        if response['status'] == 200:
            messagebox.showinfo('Recusado!', response['message'])
        else:
            messagebox.showerror('Erro', response['message'])