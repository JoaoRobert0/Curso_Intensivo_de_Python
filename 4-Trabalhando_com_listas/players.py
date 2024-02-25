# Fatiando uma lista
# Para criar uma fatia, especifique o índice do primeiro e do último elemento
# com os quais você quer trabalhar. Como ocorre na função range(), Python
# para em um item antes do segundo índice que você especificar. Para exibir
# os três primeiros elementos de uma lista, solicite os índices de 0 a 3; os
# elementos 0, 1 e 2 serão devolvidos.
players = ["joao", "maria", "marta", "carolina", "pedro"]
print(players[0:3])
print(players[:4])
print(players[2:])

# Percorrendo uma fatia com um laço
print("Os primeiros tres jogadores da minha equipe são:")
for player in players[:3]:
    print(player)