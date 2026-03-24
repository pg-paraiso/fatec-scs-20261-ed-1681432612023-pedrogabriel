'''
---------------------------------------------------------
* Fatec São Caetano do Sul                                *
* Exemplo de Manipulação de Lista ligada                  *
* Autor: Veríssimo (Refatorado)                           *
* Objetivo: Mostrar manipulação de lista ligada em python *
* Data: 09/03/2026                                        *
---------------------------------------------------------
'''

def valorExiste(listaCabeca, valorEntrada):
    atual = listaCabeca
    while atual is not None:
        if atual["valor"] == valorEntrada:
            return True
        atual = atual["proximo"]
    return False


def inserirInicio(listaEntrada):
    valor = input("Digite o valor para inserir no início: ")

    if valorExiste(listaEntrada, valor):
        print("Erro: Código de produto duplicado!")
        return listaEntrada

    novoNo = {"valor": valor, "proximo": listaEntrada}
    print("Inserido com sucesso!")
    return novoNo


def inserirFim(listaEntrada):
    valor = input("Digite o valor para inserir no fim: ")

    if valorExiste(listaEntrada, valor):
        print("Erro: Código de produto duplicado!")
        return listaEntrada

    novoNo = {"valor": valor, "proximo": None}

    if listaEntrada is None:
        print("Inserido com sucesso!")
        return novoNo

    atual = listaEntrada
    while atual["proximo"] is not None:
        atual = atual["proximo"]

    atual["proximo"] = novoNo
    print("Inserido com sucesso!")
    return listaEntrada


def inserirMeio(listaEntrada):
    if listaEntrada is None:
        print("Lista vazia, inserindo no início...")
        return inserirInicio(listaEntrada)

    alvo = input("Inserir após qual valor existente? ")
    atual = listaEntrada

    while atual is not None and atual["valor"] != alvo:
        atual = atual["proximo"]

    if atual is None:
        print("Valor de referência não encontrado! Nenhuma inserção feita.")
        return listaEntrada

    valor = input(f"Digite o novo valor para inserir após {alvo}: ")

    if valorExiste(listaEntrada, valor):
        print("Erro: Código duplicado!")
        return listaEntrada

    novoNo = {"valor": valor, "proximo": atual["proximo"]}
    atual["proximo"] = novoNo
    print("Inserido com sucesso!")

    return listaEntrada


def listar(listaRecebida):
    if listaRecebida is None:
        print("Lista vazia")
        return

    print("\nConteúdo da Lista:")
    listaAtual = listaRecebida

    while listaAtual:
        print(listaAtual["valor"], end=" -> ")
        listaAtual = listaAtual["proximo"]

    print("None")


def buscar(listaRecebida):
    argumentoPesquisa = input("Informe o argumento de pesquisa: ")
    listaAtual = listaRecebida
    posicao = 1

    while listaAtual:
        if listaAtual["valor"] == argumentoPesquisa:
            print(f"Valor encontrado na posição {posicao}")
            return
        listaAtual = listaAtual["proximo"]
        posicao += 1

    print("Valor não encontrado")


def remover(listaEntrada):
    if listaEntrada is None:
        print("Lista vazia, nada para remover.")
        return None

    valor = input("Informe o valor que deseja remover: ")

    # Remover o primeiro elemento
    if listaEntrada["valor"] == valor:
        print("Removido com sucesso!")
        return listaEntrada["proximo"]

    atual = listaEntrada

    while atual["proximo"] is not None:
        if atual["proximo"]["valor"] == valor:
            atual["proximo"] = atual["proximo"]["proximo"]
            print("Removido com sucesso!")
            return listaEntrada
        atual = atual["proximo"]

    print("Valor não encontrado para remoção.")
    return listaEntrada


def menu():
    lista = None

    while True:
        print("\n" + "="*25)
        print("1 - Inserir no Início")
        print("2 - Inserir no Fim")
        print("3 - Inserir no Meio")
        print("4 - Listar")
        print("5 - Remover")
        print("6 - Buscar")
        print("0 - Sair")
        print("="*25)

        opcao = input("Escolha uma operação: ")

        if opcao == '1':
            lista = inserirInicio(lista)
        elif opcao == '2':
            lista = inserirFim(lista)
        elif opcao == '3':
            lista = inserirMeio(lista)
        elif opcao == '4':
            listar(lista)
        elif opcao == '5':
            lista = remover(lista)
        elif opcao == '6':
            buscar(lista)
        elif opcao == '0':
            print("Obrigado por usar o sistema")
            break
        else:
            print("* Opção inválida *")


# INÍCIO CORRETO DO PROGRAMA
if __name__ == "__main__":
    print("* Bem-vindo ao programa de Lista Ligada *")
    menu()