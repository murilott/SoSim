from tkinter import *
from tkinter import ttk

class MemAlocada:
    def __init(self, nome, quan_memoria, ativo):
        self.nome = nome
        self.quan_memoria = quan_memoria
        self.ativo = ativo

    def ativar(self):
        if not self.ativo:
            self.ativo = True

    def deativar(self):
        if self.ativo:
            self.ativo = False

class Application:
    def __init__(self, master=None):
        
        # self.frame = Frame(master)
        # self.frame["width"] = 250
        # self.frame["height"] = 250
        # self.frame.pack(side="top")

        self.desktopContainer = Frame(master, borderwidth = 1, bg="gray")
        self.desktopContainer["pady"] = 10
        self.desktopContainer["width"] = 200
        self.desktopContainer["height"] = 100
        self.desktopContainer.pack(fill="both", expand=False, side="top")

        self.botMinimizar = Button(self.desktopContainer, text="Minimizar", command=self.minimizar)
        self.botMinimizar["width"] = 10
        self.botMinimizar.pack(side="top")

        self.botApagar = Button(self.desktopContainer, text="Fechar", command=self.fechar)
        self.botApagar.pack(side="top")

    def fechar(self):
        pass



    def minimizar(self): #, event
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"

        # self.msg = Label(self.frame, text="Primeiro widget")
        # self.msg.pack(side="top")

        # self.sair = Button(self.frame, text="Sair", command=self.frame.quit)
        # self.sair.pack(side="right")

        # # self.outro = Button(self.frame, text="Abrir", command=self.mudarTexto)
        # self.outro = Button(self.frame, text="Abrir")
        # self.outro.bind("<Button-1>", self.mudarTexto)
        # self.outro.pack(side="bottom")
    
    # def mudarTexto(self, event): #, event
    #     if self.msg["text"] == "Primeiro widget":
    #         self.msg["text"] = "O botão recebeu um clique"
    #     else:
    #         self.msg["text"] = "Primeiro widget"


root = Tk()
# root["width"] = 250
# root["height"] = 250
Application(root)
root.mainloop()