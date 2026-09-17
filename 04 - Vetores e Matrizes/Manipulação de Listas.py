#Exemplo de Listas
numeros = [4, 1, 0, 2, 3]
opcoes = ["nao", "sim", "talvez"]
modelos = [2000, "XP", 7, 8, True]
listas = [numeros, opcoes]

print(modelos)
print(listas)
print(numeros[-1])
print(modelos[:3])

#Ordenação dos valores de uma Lista
numeros.sort()
print(numeros)

#Adição / Atribuição de Valores em uma Lista
modelos.append(10)
modelos[0] = "Primeiro Valor"
print(modelos)