# Verificador de maioridade
# Pede a idade e responde: menor, maior ou idoso. Serve para fixar if, elif e comparação.

idade = int(input("Digite a idade: "))

if idade <= 17:
    print("Menor de idade.")
elif idade >= 18:
    print("Maior de idade.")
elif idade >= 65:
    print("Idoso(a)")