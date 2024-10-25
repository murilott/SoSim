from tkinter import *
from tkinter import ttk

class MemGerenciador:
    def __init__(self, max, mem_so, mem_delimitador):
        self.memoria_grid = []
        self.memoria_max = max
        self.memoria_so = mem_so
        self.memoria_delimitador = mem_delimitador

        self.alocar(mem_so, 0)
        

        # Estrutura
        # memoria_grid = [ [5, 0], [11, 1], [8, 2], [17, 3]]
        # O primeiro item sendo a memória do sistema, e os demais dos apps
        # O segundo item dentro da lista representa o app, sendo 0 o SO
        # https://stackoverflow.com/questions/71586546/create-a-list-of-tuples-with-the-first-position-fixed
    
    def alocar(self, memoria, app):
        if [memoria, app] not in self.memoria_grid:
            self.memoria_grid.append([memoria, app])
        else:
            index = self.memoria_grid.index([memoria, app])
            self.memoria_grid[index] = [memoria, app]

    def liberar(self, memoria, app):
        if [memoria, app] in self.memoria_grid:
            self.memoria_grid.remove([memoria, app])

class MemAlocada:
    def __init(self, nome, quan_memoria, ativo):
        self.nome = nome
        self.quan_memoria = quan_memoria
        self.ativo = ativo

    def ativar(self):
        if not self.ativo:
            self.ativo = True

    def desativar(self):
        if self.ativo:
            self.ativo = False

class Application:
    def __init__(self, master=None):
        
        # self.frame = Frame(master)
        # self.frame["width"] = 250
        # self.frame["height"] = 250
        # self.frame.pack(side="top")

        self.app_list = []
        self.mem_gerenciador = MemGerenciador(70, 10, 20)

        self.desktopContainer = Frame(master, borderwidth = 1, bg="gray")
        self.desktopContainer["padx"] = 20
        self.desktopContainer["pady"] = 20
        self.desktopContainer["width"] = 300
        self.desktopContainer["height"] = 100
        self.desktopContainer.pack(fill="x", expand=False, side="top")
        # self.desktopContainer.pack_propagate(False)

        self.appListContainer = Frame(master, borderwidth = 1, bg="lightgray")
        self.appListContainer["padx"] = 20
        self.appListContainer["pady"] = 20
        self.appListContainer["width"] = 250
        self.appListContainer["height"] = 100
        self.appListContainer.pack(expand=False, side="top")

        self.memContainer = Frame(master, borderwidth = 1, bg="lightgray")
        # self.memContainer["padx"] = 20
        # self.memContainer["pady"] = 10
        self.memContainer["width"] = 300
        self.memContainer["height"] = 300



        # mem_total_atual = 0
        # for m in self.mem_gerenciador.memoria_grid:
        #     print(m)
        #     mem_total_atual += m[0]

        # tamanho_total = self.mem_gerenciador.memoria_max
        # # cells_y = self.mem_gerenciador.memoria_max

        # offset = 10
        # tamanho_cel = 15

        # self.memoria = Canvas(self.memContainer, width=tamanho_total+offset, height=tamanho_total+offset)

        # for x in range(offset, mem_total_atual//2, tamanho_cel+2):
        #     for y in range(offset, mem_total_atual//2, tamanho_cel+2):
        #         self.pagina = self.memoria.create_rectangle(x, y, x+tamanho_cel, y+tamanho_cel, fill="lightblue", outline = 'blue')
        #         # self.pagina.grid(row=i, column=j)

        # self.botMem = Button(self.memContainer, text="Memória", command=lambda: print(self.mem_gerenciador.memoria_grid, mem_total_atual)) #self.desktopContainer, 1
        # self.botMem["width"] = 10
        # self.botMem.grid(row=0, column=0)

        # self.memoria.grid(row=1, column=0)
        # self.memoria.pack()

        
                
        self.memContainer.pack(pady=20, expand=False, side="top")

        self.botApp1 = Button(self.appListContainer, text="App 1", command=lambda: self.abrir_app(self.desktopContainer, 1)) #self.desktopContainer, 1
        self.botApp1["width"] = 5
        self.botApp1.pack(side="left")

        self.botApp2 = Button(self.appListContainer, text="App 2", command=lambda: self.abrir_app(self.desktopContainer, 2))
        self.botApp2["width"] = 5
        self.botApp2.pack(side="left")

        self.botApp3 = Button(self.appListContainer, text="App 3", command=lambda: self.abrir_app(self.desktopContainer, 3))
        self.botApp3["width"] = 5
        self.botApp3.pack(side="left")


    def att_memoria(self):
        mem_total_atual = 0
        for m in self.mem_gerenciador.memoria_grid:
            print(m)
            mem_total_atual += m[0]

        tamanho_total = self.mem_gerenciador.memoria_max
        # cells_y = self.mem_gerenciador.memoria_max

        offset = 10
        tamanho_cel = 15

        self.memoria = Canvas(self.memContainer, width=tamanho_total+offset, height=tamanho_total+offset)

        for x in range(offset, mem_total_atual//2, tamanho_cel+2):
            for y in range(offset, mem_total_atual//2, tamanho_cel+2):
                self.pagina = self.memoria.create_rectangle(x, y, x+tamanho_cel, y+tamanho_cel, fill="lightblue", outline = 'blue')
                # self.pagina.grid(row=i, column=j)

        self.botMem = Button(self.memContainer, text="Memória", command=lambda: print(self.mem_gerenciador.memoria_grid, mem_total_atual)) #self.desktopContainer, 1
        self.botMem["width"] = 10
        self.botMem.grid(row=0, column=0)

        self.memoria.grid(row=1, column=0)

    def abrir_app(self, root, id): #, root, app
        app = None

        # Procura na lista de apps abertos
        for par in self.app_list:
            if id == par[1]:
                app = par[0]

        if app:
            if app.winfo_manager():
                app.pack_forget()
                
                for child in self.appListContainer.winfo_children():
                    if isinstance(child, Button):
                        nome = child["text"]
                
                        if nome == "App "+str(id):
                            child.config(bg="red")
            else:
                app.pack(expand=False, side="left") #padx=10, 

                for child in self.appListContainer.winfo_children():
                    if isinstance(child, Button):
                        nome = child["text"]
                
                        if nome == "App "+str(id):
                            child.config(bg="white")
        else:
            self.appContainer = Frame(root, borderwidth = 1, bg="lightgray")
            # self.appContainer["pady"] = 5
            self.appContainer["width"] = 500
            self.appContainer["height"] = 200
            self.appContainer.pack_propagate(False)

            self.labTitulo = Label(self.appContainer, text="App "+str(id))
            self.labTitulo.pack(side="left", anchor="ne")

            self.botApagar = Button(self.appContainer, text="Fechar", command=lambda: self.fechar(id))
            self.botApagar["width"] = 8
            self.botApagar["height"] = 1
            self.botApagar.pack(side="right", anchor="ne")
            
            self.botMinimizar = Button(self.appContainer, text="Minimizar", command=lambda: self.abrir_app(self.desktopContainer, id))
            self.botMinimizar["width"] = 8
            self.botMinimizar["height"] = 1
            self.botMinimizar.pack(side="right", anchor="ne")

            self.mem_gerenciador.alocar(5, 1)

            self.appContainer.pack(expand=False, side="left") #padx=10, 
            self.app_list.append([self.appContainer, id])

    def fechar(self, id):
        app = None

        for par in self.app_list:
            if id == par[1]:
                app = par

        if app:
            app[0].destroy()
            self.app_list.remove(app)
        else:
            print("Erro - App não encontrado para fechar")

root = Tk()
# root["width"] = 250
# root["height"] = 250
app = Application(root)
app.att_memoria()
root.mainloop()
