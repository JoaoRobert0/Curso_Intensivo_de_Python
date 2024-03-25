# 6.3 – Glossário: Um dicionário Python pode ser usado para modelar um dicionário
# de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
# • Pense em cinco palavras relacionadas à programação que você conheceu nos
# capítulos anteriores. Use essas palavras como chaves em seu glossário e
# armazene seus significados como valores.
# • Mostre cada palavra e seu significado em uma saída formatada de modo
# elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
# significado, ou apresentar a palavra em uma linha e então exibir seu significado
# indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n)
# para inserir uma linha em branco entre cada par palavra-significado em sua
# saída.
glossary = {
    "byte": "Um conjuto de 8 bits",
    "int": "Um tipo de dado que armazena numeros inteiros",
    "python": "Uma linguagem de programção de alto nivel",
    "assembly": "Uma linguagem que antecede a etapa de compilação",
    "dicionario": "Uma estrutura de dados capaz de armazena inumeros objetos",
    }
print("Byte:\n\t" + glossary["byte"], end= 2*"\n")
print("Int:\n\t" + glossary["int"], end= 2*"\n")
print("Python:\n\t" + glossary["python"], end= 2*"\n")
print("Assembly:\n\t" + glossary["assembly"], end= 2*"\n")
print("Dicionario:\n\t" + glossary["dicionario"])