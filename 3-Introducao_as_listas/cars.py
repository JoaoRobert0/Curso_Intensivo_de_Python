# Ordenando uma lista de forma permanente com o método sort()
cars = ["honda", "ford", "bmw", "toyota"]
print(cars)
# Ordena em ordem alfabetica
cars.sort()
print(cars)
# Ordena em ordem alfabetica inversa
cars.sort(reverse=True)
print(str(cars) + "\n")

# Ordenando uma lista temporariamente com a função sorted()
others_cars = ["audi", "mercedez", "chevrolet", "gurgel"]
print(sorted(others_cars))
print(others_cars)
print(sorted(others_cars, reverse=True))
print(str(others_cars) + "\n")

# Exibindo uma lista em ordem inversa
print(cars)
cars.reverse()
print(str(cars) + "\n")

# Descobrindo o tamanho de uma lista
print(len(cars))