# Usando range() para criar uma lista de números
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

squares = []
print(squares)

# List comprehensions
# Uma list comprehension combina o laço for e a criação de novos elementos em uma
# linha, e concatena cada novo elemento automaticamente
squares = [i**2 for i in range(1, 11)]
print(squares)