# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:51:24 2018

@author: bobfelix
"""
import datetime
#ADICIONAR ARQUIVO TEXTO PARA SER TRATADO ABAIXO
arq = open("B:\Downloads\simplestest.txt", 'r')
readArq = arq.read()
arq.close()
#separa os dados por linhas
linha = readArq.split("{")
def ajeitaData(data):
    data = datetime.datetime.fromtimestamp(int(data)).strftime('%Y-%m-%d %H')
    return data

for item in linha:
    #separa usando virgula
    x = item.split(",")
    tamanho=len(x)
    if tamanho>1:
        #pega data
        y = x[0]
        z=y.split(":")
        #pega preco
        k=x[1]
        z = ajeitaData(z[1])
        #z = ajeitaData(z)
       # print(z)
        l=k.split(":")
        #concatena data + preço
        texto = z + "h," + l[1]
        print(texto)
        #escreve
        arq2 = open('result.txt', 'a')
        arq2.write(texto)
        arq2.write('\n')
        arq2.close()
