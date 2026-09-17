class Pessoa:
  def __init__(self, nome: str, idade: int, altura: float):
    self.nome = nome
    self.idade = idade
    self.altura = altura

  def dizer_ola(self):
    print(f"Olá, meu nome é {self.nome}. Tenho {self.idade} anos e minha altura é {self.altura}m.")

# Instancia de um objeto da Classe "Pessoa"
name = str(input("Informe seu Nome: "))
age = int(input("Informe sua Idade: "))
height = float(input("Informe sua altura: "))

pessoa = Pessoa(nome=name, idade=age, altura=height)

# Execução dos Métodos de "Pessoa"
pessoa.dizer_ola()