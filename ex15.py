# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#
#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
#
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$
#
#     Obs.: Salário Bruto - Descontos = Salário Líquido.

salario = float(input('Digite quando você ganha por hora: '))
horas = float(input('Digite quantas horas você trabalhou: '))

salarioB = salario*horas

ir = salarioB*0.11
inss = salarioB*0.08
sindicato = salarioB*0.05
descontos = ir + inss + sindicato
salarioL = salarioB - descontos

print(f"""\n+ Salário Bruto : R${salarioB}
- IR (11%) : R${ir}
- INSS (8%) : R${inss}
- Sindicato (5%) : R${sindicato}
= Salário Líquido : R${salarioL}""")

print("=-"*30)
