'''
---------------------------------------------------------
                Fatec São Caetano do Sul 
                    Atividade B1-1 
               Autor: Pedro Gabriel Paraiso da Silva Gomes
                Objetivo: Trabalhar Python 
                    Data: 24/02/2026 
---------------------------------------------------------
'''

# --- Estrutura Global: Dicionário de Dicionários ---
catalogo = {}

def adicionar_filme(id_filme, titulo, diretor):
    """Insere um novo filme se o ID não existir."""
    
    if id_filme in catalogo:
        print("Erro: Já existe um filme com esse ID.")
    else:
        catalogo[id_filme] = {
            "titulo": titulo,
            "diretor": diretor
        }
        print("Filme adicionado com sucesso!")


def buscar_filme(id_filme):
    """Consulta um filme usando o método seguro .get()."""
    
    filme = catalogo.get(id_filme)
    
    if filme:
        print(f"ID: {id_filme}")
        print(f"Título: {filme['titulo']}")
        print(f"Diretor: {filme['diretor']}")
    else:
        print("Filme não encontrado.")


def remover_filme(id_filme):
    """Remove um filme do dicionário usando .pop()."""
    
    removido = catalogo.pop(id_filme, None)
    
    if removido:
        print("Filme removido com sucesso!")
    else:
        print("Filme não encontrado.")


def listar_todos():
    """Lista todos os filmes do catálogo."""
    
    if not catalogo:
        print("O catálogo está vazio.")
    else:
        print("\n--- Listagem de Filmes ---")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Título: {dados['titulo']} | Diretor: {dados['diretor']}")


# --- Testes de Funcionamento ---

adicionar_filme(1, "Interestelar", "Christopher Nolan")
adicionar_filme(2, "Matrix", "Wachowski")

listar_todos()

buscar_filme(1)

remover_filme(2)

listar_todos()