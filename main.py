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
        self.desktopContainer["pady"] = 20
        self.desktopContainer["width"] = 300
        self.desktopContainer["height"] = 100
        self.desktopContainer.pack(fill="both", expand=False, side="top")
        # self.desktopContainer.pack_propagate(False)

        self.appListContainer = Frame(master, borderwidth = 1, bg="lightgray")
        self.appListContainer["padx"] = 20
        self.appListContainer["pady"] = 10
        self.appListContainer["width"] = 250
        self.appListContainer["height"] = 100
        self.appListContainer.pack(expand=False, side="top")

        self.appContainer = Frame(self.desktopContainer, borderwidth = 1, bg="lightgray")
        self.appContainer["pady"] = 5
        self.appContainer["width"] = 500
        self.appContainer["height"] = 200
        self.appContainer.pack_propagate(False)

        self.botApp1 = Button(self.appListContainer, text="App 1", command=self.abrir_app) #self.desktopContainer, 1
        self.botApp1["width"] = 5
        self.botApp1.pack(side="left")

        self.botApp2 = Button(self.appListContainer, text="App 2")
        self.botApp2["width"] = 5
        self.botApp2.pack(side="left")

        self.botApp3 = Button(self.appListContainer, text="App 3")
        self.botApp3["width"] = 5
        self.botApp3.pack(side="left")

        self.botApagar = Button(self.appContainer, text="Fechar", command=self.fechar)
        self.botApagar["width"] = 8
        self.botApagar["height"] = 1
        self.botApagar.pack(side="right", anchor="ne")
        
        self.botMinimizar = Button(self.appContainer, text="Minimizar", command=self.abrir_app)
        self.botMinimizar["width"] = 8
        self.botMinimizar["height"] = 1
        self.botMinimizar.pack(side="right", anchor="ne")


    def abrir_app(self): #, root, app
        if self.appContainer.winfo_manager():
            self.appContainer.pack_forget()
        else:
            self.appContainer.pack(expand=False, side="bottom")

    def fechar(self):
        pass

    def minimizar(self): #, event
        self.desktopContainer.pack_forget() if self.desktopContainer.winfo_manager() else self.desktopContainer.pack(anchor=W, padx=5, pady=10)

    def minimizar2(self): #, event
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