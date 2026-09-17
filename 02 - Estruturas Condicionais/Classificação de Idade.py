idade = int(input("Informe a idade: "))

if idade < 13:
  print("Criança")
elif idade > 12 and idade < 18:
  print("Adolescente")
elif idade >= 18:
  print("Adulto")
else:
  print("Problema nos dados inseridos")

#Até 12 Anos = Criança
#13 à 17 anos = Adolescente
#Maior que 18 Anos = Adulto

