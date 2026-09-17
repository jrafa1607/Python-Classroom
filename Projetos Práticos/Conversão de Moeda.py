#Declaração das notas
valor = int(input("Informe o valor para saque: "))

#Variáveis de controle de Notas
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
moeda1 = 0
resto = 0

#Processamento
nota100 = (valor // 100)
resto = valor % 100

if resto > 0:
  nota50 = resto // 50
  resto = resto % 50
if resto > 0:
  nota20 = resto // 20
  resto = resto % 20
if resto > 0:
  nota10 = resto // 10
  resto = resto % 10
if resto > 0:
  nota5 = resto // 5
  resto = resto % 5
if resto > 0:
  nota2 = resto // 2
  resto = resto % 2
if resto > 0:
  moeda1 = resto // 1
  resto = resto % 1

#Impressão dos Resultados
print("\nPara o valor: " + str(valor) + " reais, será disponibilizado: ")

print("Total de " + str(nota100) + " notas de R$100,00 reais")
print("Total de " + str(nota50) + " notas de R$50,00 reais")
print("Total de " + str(nota20) + " notas de R$20,00 reais")
print("Total de " + str(nota10) + " notas de R$10,00 reais")
print("Total de " + str(nota5) + " notas de R$5,00 reais")
print("Total de " + str(nota2) + " notas de R$2,00 reais")
print("Total de " + str(moeda1) + " moedas de R$1,00 reais")