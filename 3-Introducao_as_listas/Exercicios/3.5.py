# 3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
# convidados não poderá comparecer ao jantar, portanto será necessário enviar um
# novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.
# • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
# no final de seu programa, especificando o nome do convidado que não poderá
# comparecer.
# • Modifique sua lista, substituindo o nome do convidado que não poderá
# comparecer pelo nome da nova pessoa que você está convidando.
# • Exiba um segundo conjunto de mensagens com o convite, uma para cada
# pessoa que continua presente em sua lista.
names = ["kobe", "tesla", "turing"]
print("To com saudades meu colega: " + names[0].upper())
print("To com saudades meu colega: " + names[1].upper())
print("To com saudades meu colega: " + names[2].upper())
print("Que pena " + names[1] + " não comparecer no nosso jantar!")
names[1] = "pedrin do grau"
print("Você está convidado para o jantar: " + names[0].upper())
print("Você está convidado para o jantar: " + names[1].upper())
print("Você está convidado para o jantar: " + names[2].upper())