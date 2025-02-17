def print_heart(s):
    n = len(s)
    
    # Parte superior do coração
    for i in range(n // 2, n + 1, 2):
        # Espaços à esquerda
        for j in range(1, n - i, 2):
            print(" ", end="")
        
        # Primeira metade do coração
        for j in range(1, i + 1):
            print(s[j % n], end="")
        
        # Espaços entre as duas metades
        for j in range(1, n - i + 1):
            print(" ", end="")
        
        # Segunda metade do coração
        for j in range(1, i + 1):
            print(s[j % n], end="")
        
        print()
    
    # Parte inferior do coração
    for i in range(n, 0, -1):
        # Espaços à esquerda
        for j in range(i, n):
            print(" ", end="")
        
        # Parte inferior do coração (formato invertido)
        for j in range(1, (i * 2) - 1 + 1):
            print(s[j % n], end="")
        
        print()

# String a ser exibida no coração
str = " i love cybersecurity"
print_heart(str)
