#Comissão de Vendas
vetor = []
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"] 
total = 0

for i in range(7):
  res = float(input("Informe o valor das vendas de " + str(semana[i]) + ": "))
  total = total + res
  vetor.append(res)

if total <= 300:
  comissao = total / 100 * 5
elif total <= 700:
  comissao = total / 100 * 10
elif total > 700:
  comissao = total / 100 * 15
else:
  print("Erro no Software")
  
print("\nCom o total de vendas de R$" + str(round(total,2)) + " reais, sua comissão será de R$" + str(round(comissao,2)) + " reais")