prompts = []


def criar():
    texto = input("Digite o prompt: ")
    numeros = ""
    for c in texto:
        if c in "0123456789":
            numeros = numeros + c

    cor = "verde"
    if "rua " in texto or "Rua " in texto or "avenida" in texto or "Avenida" in texto or "bairro" in texto or "Bairro" in texto or "@" in texto:
        cor = "amarelo"
    if "bomba" in texto or "Bomba" in texto or "hackear" in texto or "Hackear" in texto:
        cor = "amarelo"
    if len(numeros) >= 8:
        cor = "amarelo"
    if "cpf" in texto or "CPF" in texto or "senha" in texto or "Senha" in texto or "cartao" in texto or "cartão" in texto:
        cor = "vermelho"
    if len(numeros) == 11 and "." in texto:
        cor = "vermelho"
    if len(numeros) == 16:
        cor = "vermelho"

    prompts.append([texto, cor])
    print("Resultado:", cor)


def listar():
    if len(prompts) == 0:
        print("Nenhum prompt")
    for i in range(len(prompts)):
        print(i + 1, "-", prompts[i][0], "-", prompts[i][1])


def atualizar():
    listar()
    n = int(input("Qual numero quer mudar? "))
    if n < 1 or n > len(prompts):
        print("Numero invalido")
        return
    texto = input("Digite o novo prompt: ")
    numeros = ""
    for c in texto:
        if c in "0123456789":
            numeros = numeros + c

    cor = "verde"
    if "rua " in texto or "Rua " in texto or "avenida" in texto or "Avenida" in texto or "bairro" in texto or "Bairro" in texto or "@" in texto:
        cor = "amarelo"
    if "bomba" in texto or "Bomba" in texto or "hackear" in texto or "Hackear" in texto:
        cor = "amarelo"
    if len(numeros) >= 8:
        cor = "amarelo"
    if "cpf" in texto or "CPF" in texto or "senha" in texto or "Senha" in texto or "cartao" in texto or "cartão" in texto:
        cor = "vermelho"
    if len(numeros) == 11 and "." in texto:
        cor = "vermelho"
    if len(numeros) == 16:
        cor = "vermelho"

    prompts[n - 1] = [texto, cor]
    print("Atualizado! Resultado:", cor)


def deletar():
    listar()
    n = int(input("Qual numero quer apagar? "))
    if n < 1 or n > len(prompts):
        print("Numero invalido")
        return
    prompts.pop(n - 1)
    print("Apagado!")


while True:
    print()
    print("Bem-vindo(a/e) ao Semáforo nome_do_semáforo!")
    print("Selecione a opção desejada:")
    print("1 - Analisar prompt")
    print("2 - Listar prompts salvos")
    print("3 - Atualizar prompt")
    print("4 - Deletar prompt")
    print("0 - Sair do programa")
    print("------------------------------------------------")
    op = input("Escolha: ")

    if op == "1":
        criar()
    elif op == "2":
        listar()
    elif op == "3":
        atualizar()
    elif op == "4":
        deletar()
    elif op == "0":
        break
    else:
        print("Opcao invalida")