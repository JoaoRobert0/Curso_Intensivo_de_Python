# Mudando para letras maiúsculas e minúsculas em uma string usando
# métodos
name = "grace hooper"
print(name.title())
print(name.upper())
print(name.lower())
# Output
# Grace Hooper
# GRACE HOOPER
# grace hooper

# O método title() transforma a inicial de cada palavra em maiuscula

# O método lower() é particularmente útil para armazenar dados. Muitas
# vezes, você não vai querer confiar no fato de seus usuários fornecerem
# letras maiúsculas ou minúsculas

# Combinando ou concatenando strings
first_name = "Maria"
last_name = "Leite"
full_name = first_name + " " + last_name
print(full_name)

# Acrescentando espaços em branco em strings com tabulações ou quebras
# delinha
# \t - tabulação
# \n - quebra de linha
print("Linguagens de Programação:\n\tPython\n\tJavaScript\n\tC#")

# Removendo espaços em branco
# Possivel remover espaços na direita e esquerda das strings
message = "   Passei na faculdade   "
print("'" + message + "'")
print("'" + message.rstrip() + "'")
print("'" + message.lstrip() + "'")
print("'" + message.strip() + "'")