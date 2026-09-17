names = []
tamanhos = []

for i in range(3):
  names.append(input("Informe o nome: "))
  tamanhos.append(len(names[i]))

tamanhos.sort()
names = sorted(names, key=len)

print("\nO menor nome (" + str(names[0]) + ") possui um total de " + str(tamanhos[0]) + " letras")
print("O maior nome (" + str(names[-1]) + ") possui um total de " + str(tamanhos[-1]) + " letras")