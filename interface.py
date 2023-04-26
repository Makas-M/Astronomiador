from tkinter import*
from tkinter import messagebox

def abrir_arquivo():
    print("Arquivo aberto")
    
def sair():
    janela.quit()

def Info():
    messagebox.showinfo("Info", "Desenvolvido por: Antonio Fernando Macaringue")

def Impdados():
    grau = int(latG.get())
    minuto = int(latM.get())
    segundo = int(latS.get())
    lat = grau + minuto/60 + segundo/3600

    # circumpolaridade no hemisfeiro sul
    if ( lat < 0) :
        declinacao = - (90 + lat)
        Label(janela, text="A Estrela esta visivel para declinacao menor ou igual a: " + str(declinacao), 
      background="#dde", foreground="#009", anchor=N).place(x=10, y=120, width=500, height=40)  
    if (lat < 0):
        declinacao = (90 + lat)
        Label(janela, text="e invisivel para a declinacao maior ou igual a: " + str(declinacao), 
      background="#dde", foreground="#009", anchor=N).place(x=10, y=140, width=500, height=40)
    if ( lat > 0) :
        declinacao = (90 - lat)
        Label(janela, text="A Estrela esta visivel para declinacao maior ou igual a: " + str(declinacao), 
      background="#dde", foreground="#009", anchor=N).place(x=10, y=120, width=500, height=40)
    if (lat > 0):
        declinacao = -(90 - lat)
        Label(janela, text="e invisivel para a declinacao menor ou igual a: " + str(declinacao), 
      background="#dde", foreground="#009", anchor=N).place(x=10, y=140, width=500, height=40)
        
        
janela = Tk()
janela.geometry("500x300")
janela.title("Astronomiador")
janela.config(bg="#dde")

Label(janela, text="Exemplo da Latitude: GG:MM:SS", 
      background="#dde", foreground="#009", anchor=N).place(x=10, y=10, width=500, height=40)

# Digitar os valores da latitude
Label(janela, text="Latitude do Observador: ", 
      background="#dde", foreground="#009", anchor=W).place(x=10, y=40, width=150, height=20)
# Graus
latG = Entry(janela)
latG.pack()
latG.place(x= 150, y=40, width=40, height=20)
# Minutos
latM = Entry(janela)
latM.pack()
latM.place(x= 200, y=40, width=40, height=20)

# Segundos
latS = Entry(janela)
latS.pack()
latS.place(x= 250, y=40, width=40, height=20)



Button(janela, text="Verificar", command=Impdados).place(x=200, y=80, width=100, height=40)
janela.resizable(0,0)



barra_menu = Menu(janela)
janela.config(menu=barra_menu)

menu_arquivo = Menu(barra_menu)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Sair", command=sair)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_ajuda = Menu(barra_menu)
menu_ajuda.add_command(label="Info", command=Info)
barra_menu.add_cascade(label="Info", menu=menu_ajuda)


janela.mainloop()







