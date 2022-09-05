from tkinter import *
from tkinter import ttk
import requests
import time
import json


#
janela = Tk()
janela.title('')
janela.geometry('350x350')
janela.configure(background='red')
janela.iconbitmap('bitcoin_icon-icons.com_60538.ico')


################# Frames ####################


janela.wm_attributes('-transparentcolor' , 'red')  




def info():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,AOA,BRL"

    # -- HTTP request
    r=requests.get(api_link)
    
    # -- converter os dados em dicionario
    dados=r.json()
    
    # -- USD
    valor_usd = float(dados["USD"])
    valor_formatado_usd = "${:,.3f}".format(valor_usd)
    l_preco_usd["text"] = valor_formatado_usd
    
    
   
    # -- Reais
    valor_reais = float(dados["BRL"])
    valor_formatado_reais = "{:,.3f}".format(valor_reais)
    l_preco_reais["text"] = "Em reais é : R$ " + valor_formatado_reais
 
        
    janela.after(1000, info)
    



l_nome = Label(janela, text="monitor de preço\n BITICOIN\n EM TEMPO REAL",bg='red',fg='yellow', height=5, padx=0, relief="flat", anchor="center", font=('Arial 20 '))
l_nome.pack()

l_preco_usd = Label(janela, text="",bg='red',fg='white' ,width=14, height=1, padx=0, relief="flat", anchor="center", font=('Arial 30 '))
l_preco_usd.pack()




l_preco_reais = Label(janela, text="",fg='orange',bg='red',height=1, padx=0, relief="flat", anchor="center", font=('Arial 12 '))
l_preco_reais.pack()


info()


janela.mainloop()
