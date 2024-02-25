# Concatenando elementos no final de uma lista
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)

# Inserindo elementos em uma lista
motorcycles.insert(1, "bmw")
print(motorcycles)

# Removendo um item usando a instrução del
del motorcycles[1]
print(motorcycles)

# Removendo um item com o método pop()
popped_motorcycle = motorcycles.pop()
print("Essa foi a moto removida: " + popped_motorcycle)

# Removendo um item de acordo com o valor
# Às vezes, você são saberá a posição do valor que quer remover de uma
# lista. Se conhecer apenas o valor do item que deseja remover, o método
# remove() poderá ser usado.
removed_motorcycle = "suzuki"
motorcycles.remove(removed_motorcycle)
print("Essa moto foi encontarda e essa é o seu nome:\n\t" + removed_motorcycle)
