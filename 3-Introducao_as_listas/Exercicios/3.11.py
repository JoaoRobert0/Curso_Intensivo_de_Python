# 3.11 – Erro proposital: Se você ainda não recebeu um erro de índice em um de
# seus programas, tente fazer um erro desse tipo acontecer. Altere um índice em um
# de seus programas de modo a gerar um erro de índice. Não se esqueça de corrigir
# o erro antes de fechar o programa
cars = ["civic", "gol", "golf", "hylux"]
cars[4] = "fiat"
# IndexError: list assignment index out of range
print(cars)