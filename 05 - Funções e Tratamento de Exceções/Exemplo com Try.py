cont = [0, 1, 2, 3]
try:
  print(cont[5])
except IndexError:
  print("O vetor nao possui esta posição")