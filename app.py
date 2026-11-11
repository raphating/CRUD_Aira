import funcoes as f

prompts = []

while True:
    print()
    print("1 - Criar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Sair")
    op = input("Escolha: ")

    if op == "1":
        f.criar(prompts)
    elif op == "2":
        f.listar(prompts)
    elif op == "3":
        f.atualizar(prompts)
    elif op == "4":
        f.deletar(prompts)
    elif op == "0":
        break
    else:
        print("Opcao invalida")