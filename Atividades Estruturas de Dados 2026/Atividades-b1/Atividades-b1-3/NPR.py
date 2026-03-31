# Calculadora RPN com 4 registradores: X, Y, Z, T

# 1. Ler a expressão do usuário
expressao = input("Digite a expressão RPN (ex: 3 4 + 2 *): ")

# 2. Separar a expressão em partes (tokens)
tokens = expressao.split()

# 3. Inicializar os registradores
X = 0
Y = 0
Z = 0
T = 0

print("\nEstado inicial:")
print("X =", X, "| Y =", Y, "| Z =", Z, "| T =", T)

# 4. Percorrer cada token
for token in tokens:
    
    print("\nProcessando:", token)
    
    # Verifica se é número
    if token.isdigit():
        numero = int(token)
        
        # Faz o deslocamento (shift)
        T = Z
        Z = Y
        Y = X
        X = numero

    # Verifica se é operador
    elif token in ["+", "-", "*", "/"]:
        
        # Realiza a operação: X = Y operador X
        if token == "+":
            X = Y + X
        elif token == "-":
            X = Y - X
        elif token == "*":
            X = Y * X
        elif token == "/":
            # Evita divisão por zero
            if X != 0:
                X = Y / X
            else:
                print("Erro: divisão por zero")
                break
        
        # Ajusta os registradores após operação
        Y = Z
        Z = T
        T = 0

    else:
        print("Token inválido:", token)
        break

    # 5. Mostrar estado atual dos registradores
    print("X =", X, "| Y =", Y, "| Z =", Z, "| T =", T)

# 6. Mostrar resultado final
print("\nResultado final:", X)