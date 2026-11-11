#ESSE É O FRONT END FEITO POR IA (confome autorizado)
#!!!!!!!!!!!!!!!!!!
import tkinter as tk
from tkinter import messagebox, ttk


prompts = []


def classificar_prompt_manual(texto):
    """Classifica a cor do texto seguindo as regras do seu projeto"""
    numeros = ""
    for c in texto:
        if c in "0123456789":
            numeros = numeros + c

    cor = "verde"
    if any(p in texto for p in ["rua ", "Rua ", "avenida", "Avenida", "bairro", "Bairro", "@"]):
        cor = "amarelo"
    if any(p in texto for p in ["bomba", "Bomba", "hackear", "Hackear"]):
        cor = "amarelo"
    if len(numeros) >= 8:
        cor = "amarelo"
    if any(p in texto for p in ["cpf", "CPF", "senha", "Senha", "cartao", "cartão"]):
        cor = "vermelho"
    if len(numeros) == 11 and "." in texto:
        cor = "vermelho"
    if len(numeros) == 16:
        cor = "vermelho"

    return cor


def atualizar_tabela():
    for item in tree.get_children():
        tree.delete(item)
    for i, item in enumerate(prompts, start=1):
        tree.insert("", "end", values=(i, item[0], item[1]))


def btn_criar():
    texto = entry_prompt.get().strip()
    if not texto:
        messagebox.showwarning("Aviso", "Digite um prompt!")
        return
    cor = classificar_prompt_manual(texto)
    prompts.append([texto, cor])
    entry_prompt.delete(0, tk.END)
    atualizar_tabela()


def btn_atualizar():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um prompt na tabela para atualizar.")
        return
    valores = tree.item(item_selecionado[0], "values")
    indice = int(valores[0]) - 1

    novo_texto = entry_prompt.get().strip()
    if not novo_texto:
        messagebox.showwarning("Aviso", "Digite o novo texto no campo de texto!")
        return

    cor = classificar_prompt_manual(novo_texto)
    prompts[indice] = [novo_texto, cor]
    entry_prompt.delete(0, tk.END)
    atualizar_tabela()


def btn_deletar():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um prompt na tabela para apagar.")
        return
    valores = tree.item(item_selecionado[0], "values")
    indice = int(valores[0]) - 1

    prompts.pop(indice)
    atualizar_tabela()


# --- Janela Gráfica ---
root = tk.Tk()
root.title("Gerenciador de Prompts")
root.geometry("600x420")

frame_top = tk.Frame(root, padx=10, pady=10)
frame_top.pack(fill=tk.X)

tk.Label(frame_top, text="Prompt:").pack(side=tk.LEFT, padx=5)
entry_prompt = tk.Entry(frame_top, width=45)
entry_prompt.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

btn_add = tk.Button(frame_top, text="Criar", command=btn_criar)
btn_add.pack(side=tk.LEFT, padx=5)

# Tabela
frame_mid = tk.Frame(root, padx=10, pady=5)
frame_mid.pack(fill=tk.BOTH, expand=True)

colunas = ("#", "Prompt", "Cor")
tree = ttk.Treeview(frame_mid, columns=colunas, show="headings", selectmode="browse")
tree.heading("#", text="#")
tree.column("#", width=40, anchor=tk.CENTER)
tree.heading("Prompt", text="Prompt")
tree.column("Prompt", width=400)
tree.heading("Cor", text="Resultado")
tree.column("Cor", width=100, anchor=tk.CENTER)
tree.pack(fill=tk.BOTH, expand=True)

# Ações
frame_bottom = tk.Frame(root, padx=10, pady=10)
frame_bottom.pack(fill=tk.X)

tk.Button(frame_bottom, text="Atualizar Selecionado com Texto Acima", command=btn_atualizar).pack(side=tk.LEFT, padx=5)
tk.Button(frame_bottom, text="Deletar Selecionado", command=btn_deletar).pack(side=tk.RIGHT, padx=5)

atualizar_tabela()
root.mainloop()