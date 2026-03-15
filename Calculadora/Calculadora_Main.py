# Construir uma calculadora com todas as operações aritméticas.
# Thomas - alteração gráfica dos widgets (label, btn e entry)
# Gabriel - lógica

# Construir uma calculadora com todas as operações aritméticas.

import tkinter as tk
from PIL import Image, ImageTk


# --- FUNC AREA ---
def zero_btn():
    mirror_show('0')


def one_btn():
    mirror_show('1')


def two_btn():
    mirror_show('2')


def three_btn():
    mirror_show('3')


def four_btn():
    mirror_show('4')


def five_btn():
    mirror_show('5')


def six_btn():
    mirror_show('6')


def seven_btn():
    mirror_show('7')


def eight_btn():
    mirror_show('8')


def nine_btn():
    mirror_show('9')


def ac_btn():
    mirror_list_stored.set('')
    mirror_list.clear()


def ce_btn():
    mirror_list.clear()


def percentage_btn():
    # if not mirror_list_stored.get():
    #     ac_btn()
    # else:
    #     if math_symbol.get() == '+':
    #         result = int(mirror_list_stored.get()) + int(''.join(mirror_list))
    #         mirror_var.set(result)
    #     if math_symbol.get() == '-':
    #         result = int(mirror_list_stored.get()) - int(''.join(mirror_list))
    #         mirror_var.set(result)
    #     if math_symbol.get() == 'x':
    #         result = int(mirror_list_stored.get()) * int(''.join(mirror_list))
    #         mirror_var.set(result)
    #     if math_symbol.get() == '÷':
    #         result = int(mirror_list_stored.get()) / int(''.join(mirror_list))
    #         mirror_var.set(result)
    #     else:
    #         print('ERROR ON "percentage_btn" FUNC')
    pass


def division_btn():
    mirror_list_stored.set(''.join(mirror_list))
    mirror_list.clear()
    math_symbol.set('÷')


def multiply_btn():
    mirror_list_stored.set(''.join(mirror_list))
    mirror_list.clear()
    math_symbol.set('x')


def minus_btn():
    mirror_list_stored.set(''.join(mirror_list))
    mirror_list.clear()
    math_symbol.set('-')


def plus_btn():
    mirror_list_stored.set(''.join(mirror_list))
    mirror_list.clear()
    math_symbol.set('+')


def dot_btn():
    mirror_show('.')


def equal_btn():
    math_operation(math_symbol.get())


def mirror_show(num):
    if len(mirror_list) < 14:
        mirror_list.append(num)
        mirror_var.set(mirror_list)
        print(f'num pressed{mirror_list}')


def math_operation(symbol):
    if symbol == '+':
        result = int(mirror_list_stored.get()) + int(''.join(mirror_list))
        mirror_var.set(result)
    if symbol == '-':
        result = int(mirror_list_stored.get()) - int(''.join(mirror_list))
        mirror_var.set(result)
    if symbol == 'x':
        result = int(mirror_list_stored.get()) * int(''.join(mirror_list))
        mirror_var.set(result)
    if symbol == '÷':
        result = int(mirror_list_stored.get()) / int(''.join(mirror_list))
        mirror_var.set(result)
    else:
        print('ERROR ON "math_operation" FUNC')


# --- ROOT/HEAD ---
root = tk.Tk()
root.title('Calculadora')
root.geometry('300x470')

# --- GENERAL VARIABLES ---
mirror_list = []
mirror_list_stored = tk.StringVar()
math_symbol = tk.StringVar()
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

multiply = tk.Button(root, text='x', command=multiply_btn,
                     image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                     compound='center')
multiply.grid(row=2, column=3, padx=small_btn_pd[0], pady=small_btn_pd[0])

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

minus = tk.Button(root, text='-', command=minus_btn,
                  image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                  compound='center')
minus.grid(row=3, column=3, padx=small_btn_pd[0], pady=small_btn_pd[0])

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

plus = tk.Button(root, text='+', command=plus_btn,
                 image=pixel, width=plus_btn_sz[0], height=plus_btn_sz[1],
                 compound='center')
plus.grid(row=4, column=3, rowspan=2, padx=small_btn_pd[0], pady=small_btn_pd[0])

zero = tk.Button(root, text='0', command=zero_btn,
                 image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                 compound='center')
zero.grid(row=5, column=0, padx=small_btn_pd[0], pady=small_btn_pd[0])

dot = tk.Button(root, text='.', command=dot_btn,
                image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                compound='center')
dot.grid(row=5, column=1, padx=small_btn_pd[0], pady=small_btn_pd[0])

equal = tk.Button(root, text='=', command=equal_btn,
                  image=pixel, width=small_btn_sz[0], height=small_btn_sz[1],
                  compound='center')
equal.grid(row=5, column=2, padx=small_btn_pd[0], pady=small_btn_pd[0])

root.mainloop()
