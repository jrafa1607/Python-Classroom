#Sequência de Fibonacci
n = int(input("Informe a quantidade de itens desejados da sequência de Fibonacci: "))

n = n - 2
anterior = 1
proximo = 1
controle = 0

vetor = [anterior, proximo]

for i in range(n):
  controle = anterior
  anterior = proximo
  proximo = proximo + controle
  vetor.append(proximo)

print(vetor)  

