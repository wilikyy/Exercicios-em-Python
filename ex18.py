# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Digite o tamanho do arquivo a ser baixado: "))
tempo = int(input("Digite a velocidade da rede de internet: "))

total = tamanho/tempo
minutos = total/60

print(f"""- Tamanho do aquivo : {tamanho}MB 
- Tempo de Download (APROXIMADO) : {round(minutos,1)} minutos """)