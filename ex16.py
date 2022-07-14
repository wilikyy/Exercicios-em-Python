# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
# e o preço total.

tamanho = float(input('Digite o tamanho da área a ser pintada em metros quadrados: '))


total = tamanho/54
total2 = 0

while total >= 1:
    total -= 1
    total2 += 1

if total < 1 and total != 0:
    total2 += 1

valor = total2 * 80.00

print(f'''\n- Tamanho da parede : {tamanho}
- Quantidade de tinta : {total2} latas;
- Valor : R${valor}.''')
print('=-'*30)