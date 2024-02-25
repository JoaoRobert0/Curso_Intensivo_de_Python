# 3.9 – Convidados para o jantar: Trabalhando com um dos programas dos
# Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma mensagem
# informando o número de pessoas que você está convidando para o jantar.
names = ["kobe", "tesla", "turing"]
names.insert(0, "inicio")
names.insert(2, "meio")
names.append("final")
print("Essa é quantidade de pessoas que participarão do jantar: " + str(len(names)))