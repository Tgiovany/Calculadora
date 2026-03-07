# Construir uma calculadora com todas as operações aritméticas.
#Thomas - alteração gráfica dos widgets (label, btn e entry)
#Gabriel - lógica

from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

# --- ROOT/HEAD ---
root = tk.Tk()
root.geometry('470x300')
root.title('Calculadora')

# --- BACKGROUND CONFIG ---
image_path = 'assets/Png/Base-white.png' #caminho do png (arquivo bruto).
image_original = Image.open(image_path) #carrega os dados do png.
image_tk = None

# --- FUNÇÃO DE REDIMENSIONAMENTO ---
def redimensionar_fundo(event):
    global image_tk #Pro python não apagar a imagem da memória

    #pega o tamanho atual da janela
    largura = event.width
    altura = event.height

    #Redimensiona o png usando a qualidade máxima
    img_redimensionada = image_original.resize((largura, altura), 1)
    image_tk = ImageTk.PhotoImage(img_redimensionada)

    #Aplica a imagem no label
    label_bg.config(image=image_tk)

# --- WIDGET DE FUNDO ---
label_bg = tk.Label(root)

label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# --- CONTROLE DO REDIMENSIONAMENTO ---
timer_redimensionar = None

def agendar_redimensionamento(event):
    global timer_redimensionar

    if timer_redimensionar:
        root.after_cancel(timer_redimensionar)

    timer_redimensionar = root.after(100, lambda: redimensionar_fundo(event)) #ao redimensionar a tela, depois de 100 milisegundos ele processa a posição escolhida

def redimensionar_fundo(event): #lógica do redimensionamento
    global image_tk
    largura = event.width
    altura = event.height
    img_redimensionada = image_original.resize((largura, altura), 1)
    image_tk = ImageTk.PhotoImage(img_redimensionada)
    label_bg.config(image=image_tk)

root.bind('<Configure>', agendar_redimensionamento)
root.mainloop()

