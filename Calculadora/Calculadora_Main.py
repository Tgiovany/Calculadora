# Construir uma calculadora com todas as operações aritméticas.
#Thomas - alteração gráfica dos widgets (label, btn e entry)
#Gabriel - lógica

from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

#background config
root = tk.Tk()
root.geometry ('470x300')
root.title('Calculadora')
image_path = 'Images/Base-white.png' #caminho do png (arquivo bruto).
image_original = Image.open(image_path) #carrega os dados do png.
image_tk = None

def redimensionar_fundo(event):
    global image_tk
    image_tk = ImageTk.PhotoImage(image_original)

imagem_tk = ImageTk.PhotoImage(image_original) #pega o bruto e converte para o formato TKinter.
label_bg = tk.Label(root, image=imagem_tk, text='Calculadora', compound='center')
label_bg.grid(row=0, column=0, )





plus_btn = 0
minus_btn = 0
multiplication_btn = 0
equal_btn = 0


clear_btn = False

