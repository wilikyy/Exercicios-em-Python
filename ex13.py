#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:

# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input("Qual sua altura?: "))
sexo = input("Qual seu sexo?(M/F): ")

if sexo.upper() == "M":
    print(f"== Seu peso ideal deve ser de {(72.7*h)-58}Kg.")
elif sexo.upper() == "F":
    print(f"== Seu peso ideasl deve ser de {(62.1*h)-44.7}Kg.")

