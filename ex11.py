#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   o produto do dobro do primeiro com metade do segundo .
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo.

n1 = int(input("Digite o primeiro número (INTEIRO): "))
n2 = int(input("Digite o segundo número (INTEIRO) : "))
n3 = float(input("Digite o terceiro número (REAL) : "))

print(f"={(n1*2)*(n2/2)}")
print(f"={(3*n1)+n3}")
print(f"={n3**3}")