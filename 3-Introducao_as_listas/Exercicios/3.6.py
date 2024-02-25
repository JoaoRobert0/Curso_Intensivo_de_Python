# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
# portanto agora tem mais espaço disponível. Pense em mais três convidados para o
# jantar.
# • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
# uma instrução print no final de seu programa informando às pessoas que você
# encontrou uma mesa de jantar maior.
# • Utilize insert() para adicionar um novo convidado no início de sua lista.
# • Utilize insert() para adicionar um novo convidado no meio de sua lista.
# • Utilize append() para adicionar um novo convidado no final de sua lista.
# • Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que
# está em sua lista.
names = ["kobe", "tesla", "turing"]
print("Você está no jantar: " + names[0].upper())
print("Você está no jantar: " + names[1].upper())
print("Você está no jantar: " + names[2].upper() + "\n")
names.insert(0, "inicio")
names.insert(2, "meio")
names.append("final")
print("Você está no jantar: " + names[0].upper())
print("Você está no jantar: " + names[1].upper())
print("Você está no jantar: " + names[2].upper())
print("Você está no jantar: " + names[3].upper())
print("Você está no jantar: " + names[4].upper())
print("Você está no jantar: " + names[5].upper())