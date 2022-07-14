area = float(input("Digite a área em metros quadrados : "))
litros = area/6

ml = (litros - int(litros)) * 1000 #Mililitros

#- LATAS
latas = int(litros/18)
if ((litros/18) - int(litros/18)) != 0:
    latas += 1


#- GALÕES
galoes = int(litros/3.6)
if ((litros/3.6) - int(litros/3.6)) != 0:
    galoes += 1


#- MISTURA
litros10  = (area/6) + (area/6)*0.1 #Acrescimo de 10%
acrescimo = (area/6)*0.1

latas01 = litros10/18 #Quantidade de latas nescessárias.
latas02 = int(litros10/18) #Parte inteira da quantidade de latas nescessárias.
latas03 = (litros10/18)-int(litros10/18) #Partes decimal da quantidade de latas nescessárias.

galoes01 = (latas03 * 18)/3.6 #Quantidade de galões nescessários para completar oque falta.
galoes02 = int((latas03 * 18)/3.6) #Parte inteira da quantidade de galões nescessários para completar oque falta.

if (latas03 * 18)/3.6 - int(latas03 * 18)/3.6 != 0: #Verificar se há parte decimal na quantidade de galões
    galoes02 += 1                                   #nescessários para completar oque falta.


#- PREÇOES
Lpreco = latas * 80.00
Gpreco = galoes * 25.00
preco_mistura = (latas02 * 80.00) + (galoes02 * 25.00)


print(f"\n= TINTA NESCESSÁRIA: {litros: .0f}L e {ml: .0f}ml")
print(f"= Lata de 18L:  {latas} Unid. | Valor: R${Lpreco: .2f}")
print(f"= Galão de 3,6L: {galoes} Unid. | Valor: R${Gpreco: .2f}")
print(f"""= MISTURA (Lata e Galão) | Valor: R${preco_mistura}
  * Latas: {latas02} Unid.
  * Galões: {galoes02} Unid. 
  * Acrescimo de 10% de tinta: {acrescimo: .2f}L""")

