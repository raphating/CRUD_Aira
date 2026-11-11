
def criar(prompts):
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


def listar(prompts):
    if len(prompts) == 0:
        print("Nenhum prompt")
    for i in range(len(prompts)):
        print(i + 1, "-", prompts[i][0], "-", prompts[i][1])


def atualizar(prompts):
    listar(prompts)
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


def deletar(prompts):
    listar(prompts)
    n = int(input("Qual numero quer apagar? "))
    if n < 1 or n > len(prompts):
        print("Numero invalido")
        return
    prompts.pop(n - 1)
    print("Apagado!")