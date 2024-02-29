# 5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
# criar em dez. Se quiser testar mais comparações, escreva outros testes e acrescenteos em conditional_tests.py. Tenha pelo menos um resultado True e um False para
# cada um dos casos a seguir:
# • testes de igualdade e de não igualdade com strings;
# • testes usando a função lower();
# • testes numéricos que envolvam igualdade e não igualdade, maior e menor que,
# maior ou igual a e menor ou igual a;
# • testes usando as palavras reservadas and e or;
# • testes para verificar se um item está em uma lista;
# • testes para verificar se um item não está em uma lista.
name = "Joao"
print(name == "Joao")
print(name != "Joao")
print(name.lower() == "joao")
number = 12
print(number == 12)
print(number != 15)
print(number > 8)
print(number < 29)
print(number >= 12)
print(number <= 12)
print(number == 12 and name == "Maria")
print(number == 12 or name == "Maria")
foods = ["pizza", "hambuguer"]
print("pizza" in foods)
print("picole" not in foods)