# Construir uma calculadora com todas as operações aritméticas.
#Thomas - alteração gráfica dos widgets (label, btn e entry)
#Gabriel - lógica

##fonte: NotoSansMono_Condensed-Regular
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


label_bg = tk.Label(root)

label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# --- CONTROLE DO REDIMENSIONAMENTO ---
timer_redimensionar = None

def agendar_redimensionamento(event):
    global timer_redimensionar

    if timer_redimensionar:
        root.after_cancel(timer_redimensionar)

    # ao redimensionar a tela, depois de 100 milisegundos ele processa a posição escolhida
    timer_redimensionar = root.after(100, lambda: redimensionar_fundo(event))

def redimensionar_fundo(event): #lógica do redimensionamento
    global image_tk
    largura = event.width
    altura = event.height
    img_redimensionada = image_original.resize((largura, altura), 1)
    image_tk = ImageTk.PhotoImage(img_redimensionada)
    label_bg.config(image=image_tk)

root.bind('<Configure>', agendar_redimensionamento)

png_n_1 = Image.open('assets/Png/number-1-btn.png') #lê o bruto
conv_n_1 = ImageTk.PhotoImage(png_n_1)
one = tk.Button(root, text='1', command=one_btn, compound='center', image=conv_n_1, borderwidth=0, highlightthickness=0)

one.grid(row=4, column=0, padx=small_btn_pd[0], pady=small_btn_pd[0])

# --- CARREGANDO OS PNGS DOS BUTTONS ---
#--1--
#png_n_1 = Image.open('assets/Png/number-1-btn.png') #lê o bruto
#conv_n_1 = ImageTk.PhotoImage(png_n_1) #converte para o Python
#btn_1 = tk.Button(root,
                  #text='1',
                  #image=conv_n_1,                           #png convertido para python
                  #compound='center',                        #Coloca o texto no centro da imagem
                  #borderwidth=0,                            #tira a borda padrão
                  #highlightthickness=0,                     #Remove o contorno de seleção
                  #command=one_btn)                          #mantem a função do Gabriel
#--2--
png_n_2 = Image.open('assets/Png/number-2-btn.png')
conv_n_2 = ImageTk.PhotoImage(png_n_2)
btn_2 = tk.Button(root,
                  text='2',
                  image=conv_n_2,
                  compound='center',
                  borderwidth=0,
                  highlightthickness=0,
                  command=two_btn)
#--3--
png_n_3 = Image.open('assets/Png/number-3-btn.png')
conv_n_3 = ImageTk.PhotoImage(png_n_3)
btn_3 = tk.Button(root,
                  text='3',
                  image=conv_n_3,
                  compound='center',
                  borderwidth=0,
                  highlightthickness=0,
                  command=three_btn)
#--4--
png_n_4 = Image.open('assets/Png/number-4-btn.png')
conv_n_4 = ImageTk.PhotoImage(png_n_4)
btn_4 = tk.Button(root,
                  text='4',
                  image=conv_n_4,
                  compound='center',
                  borderwidth=0,
                  highlightthickness=0,
                  command=four_btn)
#--5--
png_n_5 = Image.open('assets/Png/number-5-btn.png')
conv_n_5 = ImageTk.PhotoImage(png_n_5)
btn_5 = tk.Button(root,
                  text='5',
                  image=conv_n_5,
                  compound='center',
                  borderwidth=0,
                  highlightthickness=0,
                  command=five_btn)
#--6--
png_n_6 = Image.open('assets/Png/number-6-btn.png')
conv_n_6 = ImageTk.PhotoImage(png_n_6)
btn_6 = tk.Button(root,
                  text='6',
                  image=conv_n_6,
                  compound='center',
                  borderwidth=0,
                  highlightthickness=0,
                  command=six_btn)
#--7--
png_n_7 = Image.open('assets/Png/number-7-btn.png')
conv_n_7 = ImageTk.PhotoImage(png_n_7)
btn_7 = tk.Button(root,
                  text='7',
                  image=conv_n_7,
                  compound='center',
                  borderwidth=0,
                  highlightthickness=0,
                  command=seven_btn)
#--8--
png_n_8 = Image.open('assets/Png/number-8-btn.png')
conv_n_8 = ImageTk.PhotoImage(png_n_8)
btn_8 = tk.Button(root,
                  text='8',
                  image=conv_n_8,
                  compound='center',
                  borderwidth=0,
                  highlightthickness=0,
                  command=eight_btn)
#--9--
png_n_9 = Image.open('assets/Png/number-9-btn.png')
conv_n_9 = ImageTk.PhotoImage(png_n_9)
btn_9 = tk.Button(root,
                  text='9',
                  image=conv_n_9,
                  compound='center',
                  borderwidth=0,
                  highlightthickness=0,
                  command=nine_btn)
#--0--
png_n_0 = Image.open('assets/Png/number-0-btn.png')
conv_n_0 = ImageTk.PhotoImage(png_n_0)
btn_0 = tk.Button(root,
                  text='0',
                  image=conv_n_0,
                  compound='center',
                  borderwidth=0,
                  highlightthickness=0,
                  command=zero_btn)
#--Plus--
png_plus = Image.open('assets/Png/plus-btn.png')
conv_plus = ImageTk.PhotoImage(png_plus)
btn_plus = tk.Button(root,
                     text='+',
                     image=conv_plus,
                     compound='center',
                     borderwidth=0,
                     highlightthickness=0,
                     command=plus_btn)
#--Minus--
png_minus = Image.open('assets/Png/minus-btn.png')
conv_minus = ImageTk.PhotoImage(png_minus)
btn_minus = tk.Button(root,
                      text='-',
                      image=conv_minus,
                      compound='center',
                      borderwidth=0,
                      highlightthickness=0,
                      command=minus_btn)
#--AC--
png_ac = Image.open('assets/Png/AC-btn.png')
conv_ac = ImageTk.PhotoImage(png_ac)
btn_ac = tk.Button(root,
                   text='AC',
                   image=conv_ac,
                   compound='center',
                   borderwidth=0,
                   highlightthickness=0,
                   command=ac_btn)
#--CE--
png_ce = Image.open('assets/Png/CE-btn.png')
conv_ce = ImageTk.PhotoImage(png_ce)
btn_ce = tk.Button(root,
                   text='CE',
                   image=conv_ce,
                   compound='center',
                   borderwidth=0,
                   highlightthickness=0,
                   command=ce_btn)
#--Percentage--
png_percentage = Image.open('assets/Png/percentage-btn.png')
conv_percentage = ImageTk.PhotoImage(png_percentage)
btn_percentage = tk.Button(root,
                           text='%',
                           image=conv_percentage,
                           compound='center',
                           borderwidth=0,
                           highlightthickness=0,
                           command=percentage_btn)
#--Division--
png_division = Image.open('assets/Png/division-btn.png')
conv_division = ImageTk.PhotoImage(png_division)
btn_division = tk.Button(root,
                         text='÷',
                         image=conv_division,
                         compound='center',
                         borderwidth=0,
                         highlightthickness=0,
                         command=division_btn)
#--Multiply--
png_multiply = Image.open('assets/Png/multiply-btn.png')
conv_multiply = ImageTk.PhotoImage(png_multiply)
btn_multiply = tk.Button(root,
                         text='x',
                         image=conv_multiply,
                         compound='center',
                         borderwidth=0,
                         highlightthickness=0,
                         command=multiply_btn)
#--Dot--
png_dot = Image.open('assets/Png/dot-btn.png')
conv_dot = ImageTk.PhotoImage(png_dot)
btn_dot = tk.Button(root,
                    text='.',
                    image=conv_dot,
                    compound='center',
                    borderwidth=0,
                    highlightthickness=0,
                    command=dot_btn)
#--Equal--
png_equal = Image.open('assets/Png/equal-btn.png')
conv_equal = ImageTk.PhotoImage(png_equal)
btn_equal = tk.Button(root,
                      text='=',
                      image=conv_equal,
                      compound='center',
                      borderwidth=0,
                      highlightthickness=0,
                      command=equal_btn)
root.mainloop()
