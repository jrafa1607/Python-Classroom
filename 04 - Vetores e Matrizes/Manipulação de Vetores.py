#Mostrar o somatório de todos os números digitados
valores = []
total = 0
num = int(input("Quantos Numeros você quer Somar: "))

for i in range(num):
  res = float(input("Informe o valor: "))
  valores.append(res)
  total = total + res

print("\n")
print("Somatório dos Valores: " + str(total))
print("Lista dos Valores Digitados: " + str(valores))