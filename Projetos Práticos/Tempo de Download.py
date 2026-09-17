tamanho = int(input("Tamanho do Arquivo em GB: "))
tamanho = tamanho * 1024

internet = int(input("Informe a velocidade do Link de Internet: "))
segundos = tamanho / internet
minutos = segundos / 60

print("\nO arquivo de tamanho " + str(tamanho) + "Mb irá no mínimo " + str(round(minutos,2)) + " minutos para ser feito")