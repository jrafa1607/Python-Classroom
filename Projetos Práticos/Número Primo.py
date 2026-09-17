#Variáveis do Còdigo
num = int(input("Digite um numero inteiro: "))
primo = True

#Criando o Laço de Validação
for i in range(2, num):
  if num % i == 0:
    primo = False
    print(f"O número {num} não é um número primo!")
    break
if primo == True:
  print(f"O número {num} é um número primo!") 