from tkinter import *
from PIL import Image, ImageTk
from matplotlib.pyplot import text

janela = Tk()
janela.title('Visualiza Imagem')
#janela.iconbitmap('abelha.ico')

def direita(numeroImagem):
  global meuLabel
  global botaoEsquerda
  global botaoDireita

  meuLabel.grid_forget()
  meuLabel = Label(image=listaImagem[numeroImagem-1])
  botaoDireita  = Button(janela, text='>>', command=lambda: direita(numeroImagem+1))
  botaoEsquerda = Button(janela, text='<<', command=lambda: esquerda(numeroImagem-1))

  if numeroImagem == 5:
    botaoDireita  = Button(janela, text='>>', state=DISABLED)

  meuLabel.grid(row=0, column=0, columnspan=3)
  botaoEsquerda.grid(row=1, column=0)
  botaoDireita.grid(row=1, column=2)

  progresso = Label(janela, text='Imagem ' + str(numeroImagem) + ' de ' + str(len(listaImagem)), bd=1, relief=SUNKEN, anchor=W)
  progresso.grid(row=2, column=0, columnspan=3, sticky=W+E)

def esquerda(numeroImagem):
  global meuLabel
  global botaoEsquerda
  global botaoDireita

  meuLabel.grid_forget()
  meuLabel = Label(image=listaImagem[numeroImagem-1])
  botaoDireita  = Button(janela, text='>>', command=lambda: direita(numeroImagem+1))
  botaoEsquerda = Button(janela, text='<<', command=lambda: esquerda(numeroImagem-1))

  if numeroImagem == 1:
    botaoEsquerda  = Button(janela, text='<<', state=DISABLED)

  meuLabel.grid(row=0, column=0, columnspan=3)
  botaoEsquerda.grid(row=1, column=0)
  botaoDireita.grid(row=1, column=2)

  progresso = Label(janela, text='Imagem ' + str(numeroImagem) + ' de ' + str(len(listaImagem)), bd=1, relief=SUNKEN, anchor=W)
  progresso.grid(row=2, column=0, columnspan=3, sticky=W+E)

minhaImagem1 = ImageTk.PhotoImage(Image.open('D:\caminho'))
minhaImagem2 = ImageTk.PhotoImage(Image.open('D:\caminho'))
minhaImagem3 = ImageTk.PhotoImage(Image.open('D:\caminho'))
minhaImagem4 = ImageTk.PhotoImage(Image.open('D:\caminho'))
minhaImagem5 = ImageTk.PhotoImage(Image.open('D:\caminho'))

listaImagem = [minhaImagem1, minhaImagem2, minhaImagem3, minhaImagem4, minhaImagem5]

progresso = Label(janela, text='Imagem 1 de ' + str(len(listaImagem)), bd=1, relief=SUNKEN, anchor=W)

meuLabel = Label(image=minhaImagem1)
botaoEsquerda = Button(janela, text='<<', command=esquerda, state=DISABLED)
botaoSair = Button(janela, text='Sair', command=janela.quit)
botaoDireita  = Button(janela, text='>>', command=lambda: direita(2))

meuLabel.grid(row=0, column=0, columnspan=3)
botaoEsquerda.grid(row=1, column=0)
botaoSair.grid(row=1, column=1)
botaoDireita.grid(row=1, column=2, pady=10)
progresso.grid(row=2, column=0, columnspan=3, sticky=W+E)

janela.mainloop()