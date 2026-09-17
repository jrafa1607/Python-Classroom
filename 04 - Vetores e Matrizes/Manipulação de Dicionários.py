#Criando um Dicionário
refeicoes = {"café": "pão e café com leite", "almoço:": "Macarronada", "jantar": "sopa"}
print(refeicoes["café"])
print("\n")

#Visualização dos dados de um dicionário
print(refeicoes.keys())
print(refeicoes.values())
print(refeicoes.items())
print("\n")

#Adição de novos itens em um dicionário
refeicoes.update({"Sobremesa": "Chocolate"})
print(refeicoes)