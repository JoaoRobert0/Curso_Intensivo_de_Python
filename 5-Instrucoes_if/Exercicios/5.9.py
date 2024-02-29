# 5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir que a
# lista de usuários não esteja vazia.
# • Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
# usuários!
# • Remova todos os nomes de usuário de sua lista e certifique-se de que a
# mensagem correta seja exibida.
users_names = ["joao", "maria", "gilbert", "admin", "pedro"]
if users_names:
    for user in users_names:
        if (user == "admin"):
            print("Olá admin, gostaria de ver um relatório de status?")
        else:
            print("Olá " + user.title() + ", obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar alguns usuários!")