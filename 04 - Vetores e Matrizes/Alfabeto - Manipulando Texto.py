#Operações com Texto - Manusear Letras do Alfabeto
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#Descobrindo a Letra 15
print("A Letra na posição 15 é a: " + alfabeto[14]) 
#O índice inicia com 0, por isso 14!

#Mostrando somente as Letras nas Posições Par 
for i in range(len(alfabeto)):
  if i % 2 == 0:
    print(alfabeto[i])