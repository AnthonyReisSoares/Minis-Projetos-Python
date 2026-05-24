# Calculadora de média escolar
# Use input, conversão de tipo e condicionais. O programa pede 3 notas,
# calcula a média e diz se o aluno foi aprovado, reprovado ou ficou de recuperação.

print("Digite 3 notas: ")
nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))

soma = nota_1 + nota_2 + nota_3
media = soma / 3

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado")
