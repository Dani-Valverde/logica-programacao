# -*- coding: utf-8 -*-
"""Meu_primeiro_algoritmo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kUc0Zxtl-CTJOJyS0t3yxwBBRL-GCtXt
"""

#Tela de boas vindas. O usuário escolhe um número para começar.
print("Bem-vindo(a) à calculadora do nosso sistema!")
num1 = int(input("Digite um número de 0-10: "))
print("Seu primeiro número é: ", num1)

#Segundo número a ser escolhido pelo usuário
print("Agora escolha um segundo número.")
num2 = int(input("Digite um número de 0-10: "))
print("Seu segundo número é: ", num2)

#Nessa seção, a calculadora irá comparar os dois números escolhidos.
print("Agora vamos comparar os dois números que você escolheu!")
if num1 > num2:
  print("O primeiro número é maior do que o segundo!")
elif num1 < num2:
  print("O segundo número é maior do que o primeiro!")
else:
  print("Os dois números têm o mesmo valor!")

#Nessa seção a calculadora realizará 4 operações matemáticas com os números escolhidos pelo usuário.
adicao = num1 + num2
subtracao = num1 - num2
multiplic = num1 * num2
potenciacao = num1 ** num2

print("Agora vamos realizar contas com os números que você escolheu!")
print ("A adição dos seus números resulta em: ", adicao)
print ("A subtração dos seus números resulta em: ", subtracao)
print ("A multiplicação dos seus números resulta em: ", multiplic)
print ("A potenciação dos seus números resulta em: ", potenciacao)

#Nessa última seção, será feito o laço de repetição com os números escolhidos.
print("Agora vamos usar um contador! Ele irá parar de contar quando chegar a marca da soma de seus dois números!")
for contador in range (100):
  print(contador)
  if contador == num1 + num2:
    break