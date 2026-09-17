#Import da Biblioteca
import math;

#Declaração / Iniciação das variáveis das Variáveis
n1 = 0
n2 = 0

#Função para ler os números
def lernum():
  n1 = float(input("Informe o primeiro número: "))
  n2 = float(input("Informe o segundo número: "))
  return(n1, n2)

#Função para somar os números
def adicao():
  n1, n2 = lernum()
  res = n1 + n2
  return(res)

#Função para subtrair os números
def subtracao():
  n1, n2 = lernum()
  res = n1 - n2
  return(res)

#Função para Multiplicar os números
def multiplicacao():
  n1, n2 = lernum()
  res = n1 * n2
  return(res)

#Função para Dividir (Resto da Divisão)
def restodadivisao():
  n1, n2 = lernum()
  res = n1 % n2
  return(res)

#Função para Dividir
def dividir():
  n1, n2 = lernum()
  res = n1 / n2
  return(res)

#Função para Raiz Quadrada
def raiz():
  n1 = float(input("Informe o Valor: "))
  res = math.sqrt(n1)
  return(res)

#Função para Exponenciação
def potencia():
  n1, n2 = lernum()
  res = n1 ** n2
  return(res)

#Mensagem Completa - Uninove
op = str(input("Calculadora Uninove – Para seguir, informe a opção desejada:\n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Resto de Divisão \n5 - Divisão \n6 - Raíz Quadrada \n7 - Exponenciação \n\nDigite sua opção: "))

try:
  if op == "1":
    res = adicao()
    print("Resultado da Adição: " + str(res))
  elif op == "2":
    res = subtracao()
    print("Resultado da Subtração: " + str(res))
  elif op == "3":
    res = multiplicacao()
    print("Resultado da Multiplicação: " + str(res))
  elif op == "4":
    res = restodadivisao()
    print("Resultado do Resto da Divisão: " + str(res))
  elif op == "5":
    res = dividir()
    print("Resultado da Divisão: " + str(res))
  elif op == "6":
    res = raiz()
    print("Resultado da Raíz Quadrada: " + str(res))
  elif op == "7":
    res = potencia()
    print("Resultado da Exponenciação: " + str(res))
  else:
    print("Dados Inválidos!")
except:
  print("Dados Inválidos")