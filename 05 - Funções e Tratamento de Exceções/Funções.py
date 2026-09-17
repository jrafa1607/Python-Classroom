n1 = float(input("Informe um valor: "))
n2 = float(input("Informe um valor: "))

def somar(valor1, valor2):
  res = n1 + n2
  print(f"Resultado da soma: {res}")
  return res

resultado = somar(n1,n2)
print(resultado)
