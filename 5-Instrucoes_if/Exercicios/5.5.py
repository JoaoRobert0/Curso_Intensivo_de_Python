# 5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
# em uma cadeia if-elif-else.
# • Se o alienígena for verde, mostre uma mensagem informando que o jogador
# ganhou cinco pontos.
# • Se o alienígena for amarelo, mostre uma mensagem informando que o jogador
# ganhou dez pontos.
# • Se o alienígena for vermelho, mostre uma mensagem informando que o jogador
# ganhou quinze pontos.
# • Escreva três versões desse programa, garantindo que cada mensagem seja
# exibida para a cor apropriada do alienígena.
alien_color = "green"
if (alien_color == "green"):
    print("Jogador ganhou 5 pontos!")
elif (alien_color == "yellow"):
    print("Jogador ganhou 10 pontos!")
else:
    print("Jogador ganhou 15 pontos!")