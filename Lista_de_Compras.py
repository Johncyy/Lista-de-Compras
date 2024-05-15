# Sistema de lista de compras

# Lista para armazenar os itens
itens = []

# Adicionando itens
def adicionando_itens():
    item = input("Adicione um novo item: ")
    itens.append({"item": item, "feito": False})
    print(f"Item {item} adicionado")

# Visualizando itens
def visualizando_itens():
    if itens:
        print("Lista de itens:")
        for idx, item in enumerate(itens, start=1):
            if item["feito"] == True:
                status = "Comprado"
            else:
                status = "Pendente"
            print(f"{idx}. {item['item']} [{status}]")

    else:
        print("Lista vazia")

# Marcando como comprado
def marcando_comprado():
    visualizando_itens()

    idx = int(input("Digite o número do item que deseja marcar como comprado: "))-1
    if 0<= idx < len(itens):
        itens[idx]["feito"] = True
        print("Item comprado ")
    else:
        print("Número não válido")


# Removendo itens
def removendo_itens():
    visualizando_itens()

    idx = int(input("Digite o número do item que deseja remover: "))-1
    if 0<= idx < len(itens):
        item_remov = itens.pop(idx)
        print(f"Item {item_remov['item']} removido com sucesso")
    else:
        print("Número não válido")

#Loop Principal

while True:
    try:
        print("\n###Sistema de Lista de Compras###")
        print("----------------------------------------")
        print("             Menu Principal             ")
        print("----------------------------------------")
        print("1. Adicionar Item")
        print("2. Visualizar Itens")
        print("3. Registrar Item Como Comprado")
        print("4. Remover Item")
        print("5. Sair do Programa")

        opcao = int(input("Escolha uma das opções acima: "))
        if opcao == 1:
            print("\n---- Adicionando Item ----")
            adicionando_itens()
            print("---- Voltando ao menu principal ----")
        elif opcao == 2:
            print("\n---- Visualizando Itens ----")
            visualizando_itens()
            print("---- Voltando ao menu principal ----")
        elif opcao == 3:
            print("\n---- Registrando Como Comprado ----")
            marcando_comprado()
            print("---- Voltando ao menu principal ----")
        elif opcao == 4:
            print("\n---- Removendo Itens ----")
            removendo_itens()
            print("---- Voltando ao menu principal ----")
        elif opcao == 5:
            print("\nSaindo do programa...")
            break
        else:
            print("Opção invalida. Tente novamente")
    except ValueError:
        print("Digite o número de uma das opões acima, por favor.")