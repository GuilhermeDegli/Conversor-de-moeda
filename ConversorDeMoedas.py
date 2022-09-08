from cgitb import text
from email.mime import image
from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk, ImageOps, ImageDraw
import requests
import json
import string
#cores

cor0 = '#FFFFFF'  #branca
cor1 = '#333333'  #preta
cor2 = '#5f7dba'  #cor teste

#configuracao janela

janela = Tk()
janela.geometry('650x475')
janela.title("")
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# divisao janela

parte_cima = Frame(janela,
                   width=650,
                   height=130,
                   padx=0,
                   pady=0,
                   bg=cor2,
                   relief='flat')

parte_cima.grid(row=0, column=0, columnspan=2)

parte_baixo = Frame(janela,
                    width=650,
                    height=470,
                    padx=0,
                    pady=0,
                    bg=cor1,
                    relief='flat')

parte_baixo.grid(row=1, column=0, sticky=NSEW)

ExemplosDeMoeda = Label(
    parte_baixo,
    text=
    'Escolha uma moeda para ser convertida e depois\nescolha para qual outra moeda deseja converte-lá.\nE Então coloque o valor que deseja converter.\n\n Opções de Conversão:',
    height=200,
    width=40,
    relief='flat',
    anchor=NW,
    font=('Ivy 10 bold'),
    bg=cor1,
    fg=cor0,
)

ExemplosDeMoeda.place(x=22, y=20)

icon2 = Image.open('images/exemplo.jpg')
icon2 = icon2.resize((247, 205), Image.ANTIALIAS)
icon2 = ImageTk.PhotoImage(icon2)

exemplos = Label(parte_baixo,
                 image=icon2,
                 compound=CENTER,
                 height=200,
                 width=242,
                 pady=0,
                 padx=0,
                 relief='flat',
                 anchor='center')

exemplos.place(x=60, y=120)

# Função Converter


def FunçãoConverter():

    moedaDe = combo_conv.get()
    moedaPara = combo_conver.get()
    valorr = valor.get()

    response = requests.get(
        'https://api.exchangerate-api.com/v4/latest/{}'.format(moedaDe))
    dados = json.loads(response.text)
    cambio = (dados['rates'][moedaPara])

    results = float(valorr) * float(cambio)

    if moedaPara == 'USD':
        simbolo = '$'
        x = '\nDólares americano'

    elif moedaPara == 'EUR':
        simbolo = '€'
        x = '\nEuros'

    elif moedaPara == 'BRL':
        simbolo = 'R$'
        x = '\nReais'

    elif moedaPara == 'INR':
        simbolo = '₹'
        x = '\nRupia Indiana'

    else:
        simbolo = 'Kz'
        x = 'Kwanzas'

    moedaEquivalente = simbolo + '{:,.2f}'.format(results) + x
    print(moedaEquivalente)

    painel['text'] = moedaEquivalente


#configuracao parte cima

icon = Image.open('images/ed.jpg')
icon = icon.resize((650, 140), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)

header = Label(parte_cima,
               image=icon,
               compound=CENTER,
               height=126,
               width=645,
               pady=0,
               padx=0,
               relief='flat',
               anchor='center')

header.place(x=0, y=0)

#configuracao parte baixo

painel = Label(parte_baixo,
               text='',
               height=2,
               width=16,
               relief='solid',
               anchor=CENTER,
               font=('Ivy 16 bold'),
               bg=cor0,
               fg=cor1)

painel.place(x=395, y=30)

# Marcador "De"

convers1 = Label(
    parte_baixo,
    text='De',
    height=1,
    width=8,
    relief='flat',
    anchor=NW,
    font=('Ivy 14 bold'),
    bg=cor1,
    fg=cor0,
)

moeda = ['BRL', 'USD', 'EUR', 'INR', 'AOA']

convers1.place(x=382, y=120)

combo_conv = ttk.Combobox(parte_baixo,
                          width=8,
                          justify=CENTER,
                          font='Ivy 16 bold')
combo_conv.place(x=380, y=150)
combo_conv['values'] = (moeda)

# Marcador "Para"

convertido = Label(
    parte_baixo,
    text='Para',
    height=1,
    width=8,
    relief='flat',
    anchor=NW,
    font=('Ivy 14 bold'),
    bg=cor1,
    fg=cor0,
)

convertido.place(x=502, y=120)

combo_conver = ttk.Combobox(parte_baixo,
                            width=8,
                            justify=CENTER,
                            font='Ivy 16 bold')
combo_conver.place(x=505, y=150)
combo_conver['values'] = (moeda)

# input

valor = Entry(parte_baixo,
              width=27,
              justify=CENTER,
              font=('Ivy 12 bold'),
              relief=SOLID)
valor.place(x=377, y=215)

# Butão para converter

botao = Button(parte_baixo,
               command=FunçãoConverter,
               text='Converter',
               width=18,
               padx=5,
               height=1,
               bg=cor2,
               fg=cor0,
               font=('Ivy 16 bold'),
               relief='raised',
               overrelief=RIDGE)
botao.place(x=376, y=260)

janela.mainloop()
