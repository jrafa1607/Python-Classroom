#Programa Casa de Câmbio
dolar = float(input("Informe a cotação do Dólar hj: "))
compra = float(input("Informe quantos Dólares deseja adquirir: "))

total = dolar * compra
print("O valor total da compra de " + str(compra) + " dólares ficou: R$" + str(total))
