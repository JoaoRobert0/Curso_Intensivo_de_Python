# 3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
# lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
# cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie
# uma lista contendo esses itens e então utilize cada função apresentada neste
# capítulo pelo menos uma vez.
list = ["0"]
list.insert(1, "1")
list.append("2")
list.append("3")

popped_element = list.pop()
print("O elemento que foi 'popado' da lista: " + popped_element)
del list[2]
print(list)

list.sort()
print(list)
list.sort(reverse=True)
print(list)

list.append("5")
list.append("4")
print(list)
list.reverse()
print(list)

print(len(list))