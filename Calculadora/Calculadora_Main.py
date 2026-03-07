# Construir uma calculadora com todas as operações aritméticas.
#Thomas - alteração gráfica dos widgets (label, btn e entry)
#Gabriel - lógica

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

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





# --- FUNC AREA ---
def ac_btn():
    pass


def ce_btn():
    pass


def percentage_btn():
    pass


def division_btn():
    mirror_show('÷')


def seven_btn():
    mirror_show('7')


def eight_btn():
    mirror_show('8')


def nine_btn():
    mirror_show('9')


def multiply_btn():
    mirror_show('x')


def four_btn():
    mirror_show('4')


def five_btn():
    mirror_show('5')


def six_btn():
    mirror_show('6')


def minus_btn():
    mirror_show('-')


def one_btn():
    mirror_show('1')


def two_btn():
    mirror_show('2')


def three_btn():
    mirror_show('3')


def plus_btn():
    mirror_show('+')


def zero_btn():
    mirror_show('0')


def dot_btn():
    pass


def equal_btn():
    mirror_show('=', math_symbol)


def mirror_show(num):
    global math_symbol

    if num in ['+', '-', 'x', '÷']:
        mirror_list_stored = list(mirror_list)
        math_symbol = num
        mirror_list.clear()
        print(mirror_list_stored)
        print(mirror_list)
        print(math_symbol)

    if num == '=':
        math_operation(math_symbol)
        print(math_symbol)

    if len(mirror_list) < 14:
        if num in ['+', '-', 'x', '÷', '=']:
            pass
        else:
            mirror_list.append(num)
            mirror_var.set(mirror_list)
            print(f'num press{mirror_list}')


def math_operation(symbol):
    if symbol == '+':
        mirror_var.set(str(int(''.join(mirror_list_stored)) + int(''.join(mirror_list))))
    if symbol == '-':
        mirror_var.set(str(int(''.join(mirror_list_stored)) - int(''.join(mirror_list))))
    if symbol == 'x':
        mirror_var.set(str(int(''.join(mirror_list_stored)) * int(''.join(mirror_list))))
    if symbol == '÷':
        mirror_var.set(str(int(''.join(mirror_list_stored)) / int(''.join(mirror_list))))


# --- GENERAL VARIABLES ---
mirror_list = []
mirror_list_stored = []
math_symbol = ''
mirror_var = tk.StringVar()

pixel = tk.PhotoImage(width=1, height=1)
# Essa var está sendo utilizada como espaçador em pixeis ao inves de ser
# por caracter que é o padrão, ver o width e height dos Buttons
small_btn_sz = [23, 20]
small_btn_pd = [5]
plus_btn_sz = [23, 60]
# Como o pai é  C H A T O  na programação, eu acabei fazendo essas variáveis
# para controlar o padding e tamanho dos btns.
# "Ó, mas por qual motivo fazer assim?" você me perguntaria, simples:
# Dessa forma, caso queiramos alterar o tamanho de todos os btns
# simultaneamente, nós apenas modificamos uma vez dentro dessas variáveis e
# refletirá para todos os btns correspondentes!
# Sem a necessidade de ir botão por botão fazer as mods!


# --- WIDGETS ---
mirror = tk.Label(root, textvariable=mirror_var)
mirror.grid(row=0, column=0, columnspan=3)

ac = tk.Button(root, text='AC', command=ac_btn,
               image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
               compound='center')
ac.grid(row=1, column=0, padx=small_btn_pd[0], pady=small_btn_pd[0])

ce = tk.Button(root, text='CE', command=ce_btn,
               image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
               compound='center')
ce.grid(row=1, column=1, padx=small_btn_pd[0], pady=small_btn_pd[0])

percentage = tk.Button(root, text='%', command=percentage_btn,
                       image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                       compound='center')
percentage.grid(row=1, column=2, padx=small_btn_pd[0], pady=small_btn_pd[0])

division = tk.Button(root, text='÷', command=division_btn,
                     image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                     compound='center')
division.grid(row=1, column=3, padx=small_btn_pd[0], pady=small_btn_pd[0])


multiply = tk.Button(root, text='x', command=multiply_btn,
                     image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                     compound='center')
multiply.grid(row=2, column=3, padx=small_btn_pd[0], pady=small_btn_pd[0])

plus = tk.Button(root, text='+', command=plus_btn,
                 image=pixel, width=plus_btn_sz[0], height=plus_btn_sz[1],
                 compound='center')
plus.grid(row=4, column=3, rowspan=2, padx=small_btn_pd[0], pady=small_btn_pd[0])

dot = tk.Button(root, text='.', command=dot_btn,
                image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                compound='center')
dot.grid(row=5, column=1, padx=small_btn_pd[0], pady=small_btn_pd[0])

equal = tk.Button(root, text='=', command=equal_btn,
                  image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                  compound='center')
equal.grid(row=5, column=2, padx=small_btn_pd[0], pady=small_btn_pd[0])

zero = tk.Button(root, text='0', command=zero_btn,
                 image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                 compound='center')
zero.grid(row=5, column=0, padx=small_btn_pd[0], pady=small_btn_pd[0])

one = tk.Button(root, text='1', command=one_btn,
                image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                compound='center')
one.grid(row=4, column=0, padx=small_btn_pd[0], pady=small_btn_pd[0])

two = tk.Button(root, text='2', command=two_btn,
                image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                compound='center')
two.grid(row=4, column=1, padx=small_btn_pd[0], pady=small_btn_pd[0])

three = tk. Button(root, text='3', command=three_btn,
                   image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                   compound='center')
three.grid(row=4, column=2, padx=small_btn_pd[0], pady=small_btn_pd[0])

four = tk.Button(root, text='4', command=four_btn,
                 image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                 compound='center')
four.grid(row=3, column=0, padx=small_btn_pd[0], pady=small_btn_pd[0])

five = tk.Button(root, text='5', command=five_btn,
                 image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                 compound='center')
five.grid(row=3, column=1, padx=small_btn_pd[0], pady=small_btn_pd[0])

six = tk.Button(root, text='6', command=six_btn,
                image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                compound='center')
six.grid(row=3, column=2, padx=small_btn_pd[0], pady=small_btn_pd[0])

seven = tk.Button(root, text='7', command=seven_btn,
                  image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                  compound='center')
seven.grid(row=2, column=0, padx=small_btn_pd[0], pady=small_btn_pd[0])

eight = tk.Button(root, text='8', command=eight_btn,
                  image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                  compound='center')
eight.grid(row=2, column=1, padx=small_btn_pd[0], pady=small_btn_pd[0])

nine = tk.Button(root, text='9', command=nine_btn,
                 image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                 compound='center')
nine.grid(row=2, column=2, padx=small_btn_pd[0], pady=small_btn_pd[0])

minus = tk.Button(root, text='-', command=minus_btn,
                  image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                  compound='center')
minus.grid(row=3, column=3, padx=small_btn_pd[0], pady=small_btn_pd[0])


#--VISOR--
png_visor = Image.open('assets/Png/Visor-white.png')
conv_visor = png_visor.resize((380, 120), Image.Resampling.LANCZOS)
foto_visor = ImageTk.PhotoImage(conv_visor)
visor_label = tk.Label(
    root,
    image = foto_visor,
    textvariable=mirror_var,
    compound='center',
    font=('NotoSansMono', 20, 'bold'),
    fg='#4a5840',
    bg='#D1D1D1',
    borderwidth=0,
    highlightthickness=0,)
visor_label.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=(20, 10),)

# --- CARREGANDO OS PNGS DOS BUTTONS ---

fotos_botoes = {}

def carregar_icone(nome_ficheiro):
    caminho = f'assets/Png/{nome_ficheiro}'
    img = Image.open(caminho)
    if nome_ficheiro == 'plus_btn.png':
            img = img.resize((85, 180), Image.Resampling.LANCZOS)
    else:
        img = img.resize((85, 85), Image.Resampling.LANCZOS)

    return ImageTk.PhotoImage(img)

lista_botoes = [
    ('AC', 'AC-btn.png', 1, 0), ('CE', 'CE-btn.png', 1, 1),
    ('%', 'percentage-btn.png', 1, 2), ('÷', 'division-btn.png', 1, 3),
    ('7', 'number-7-btn.png', 2, 0), ('8', 'number-8-btn.png', 2, 1),
    ('9', 'number-9-btn.png', 2, 2), ('x', 'multiply-btn.png', 2, 3),
    ('4', 'number-4-btn.png', 3, 0), ('5', 'number-5-btn.png', 3, 1),
    ('6', 'number-6-btn.png', 3, 2), ('-', 'minus-btn.png', 3, 3),
    ('1', 'number-1-btn.png', 4, 0), ('2', 'number-2-btn.png', 4, 1),
    ('3', 'number-3-btn.png', 4, 2), ('+', 'plus-btn.png', 4, 3),
    ('0', 'number-0-btn.png', 5, 0), ('.', 'dot-btn.png', 5, 1),
    ('=', 'equal-btn.png', 5, 2)]

for texto, arquivo, linha, col in lista_botoes:
    fotos_botoes[texto] = carregar_icone(arquivo)

    r_span = 2 if texto == '+' else 1

    btn = tk.Button(
        root,
        image=fotos_botoes[texto],
        borderwidth=0,
        highlightthickness=0,
        bg='#D1D1D1',
        activebackground='#D1D1D1',
        # --- AQUI ESTÁ A CONEXÃO ---
        command=lambda t=texto: equal_btn() if t == '=' else mirror_show(t)
    )
    btn.grid(row=linha, column=col, rowspan=r_span, sticky='nsew', padx=2, pady=2)

    for i in range(4):
        root.columnconfigure(i, weight=1)

    for i in range(6):
        root.rowconfigure(i, weight=1)




root.mainloop()
