# 5.6 – Estágios da vida: Escreva uma cadeia if-elif-else que determine o
# estágio da vida de uma pessoa. Defina um valor para a variável age e então:
# • Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo
# que ela é um bebê.
# • Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem
# dizendo que ela é uma criança.
# • Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensagem
# dizendo que ela é um(a) garoto(a).
# • Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma
# mensagem dizendo que ela é um(a) adolescente.
# • Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma
# mensagem dizendo que ela é adulto.
# • Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa
# pessoa é idoso.
age = 19
if (age < 2):
    print("Bebe")
elif (age < 4):
    print("Criança")
elif (age < 13):
    print("Garoto(a)")
elif (age < 20):
    print("Adolescente")
elif (age < 65):
    print("Adulto")
else:
    print("Idoso")