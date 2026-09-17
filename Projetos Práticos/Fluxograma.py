#Declaração das notas
n1 = int(input("Informe a nota do aluno: "))
n2 = int(input("Informe a nota do aluno: "))
n3 = int(input("Informe a nota do aluno: "))
n4 = int(input("Informe a nota do aluno: "))
media = (n1 + n2 + n3 + n4) / 4

if media < 6:
  print("Reprovado")
elif media < 8:
  print("Recuperação")
else:
  print("Aprovado")