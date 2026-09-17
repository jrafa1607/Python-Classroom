#Programa para Calcular a Média de um Aluno
#Com imcremento de If e Else
name = input("Informe o nome do Aluno: ")
av1 = int(input("Informe a AV1: "))
av2 = int(input("Informe a AV2: "))
nota = (av1 + av2) / 2

if nota >= 7:
  resultado = "Aprovado!"
elif nota > 4 and nota < 7:
  resultado = "Recuperação!"
else:
  resultado = "Reprovado!"

print("Nome do Aluno: " + name)
print("Nota final: " + str(nota))
print("Situação do Aluno: " + resultado)