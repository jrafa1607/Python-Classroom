arquivo = open("teste.txt", "r")
print(arquivo)

with open("teste.txt", "r", encoding="utf-8") as f:
    texto = f.read()
print(texto)