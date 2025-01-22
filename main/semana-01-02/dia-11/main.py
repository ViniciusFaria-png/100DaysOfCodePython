print("Match-case")

# Match-case é uma nova estrutura de controle que foi introduzida no Python 3.10
# Ela é uma alternativa ao switch-case que é comum em outras linguagens de programação
# A diferença é que o match-case é mais poderoso e flexível que o switch-case
# O match-case é uma expressão que permite comparar um valor com várias expressões
# e executar um bloco de código dependendo do resultado da comparação

# Exemplo 1: match-case com valores simples
# Neste exemplo, vamos comparar um valor com várias expressões

# Definimos um valor
value = 2
match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case 3:
        print("Value is 3")
    case _:
        print("Value is not 1, 2 or 3")

# Exemplo 2: match-case com valores de tipos diferentes

# Definimos um valor
value = 2
match value:
    case 1:
        print("Value is 1")
    case "2":
        print("Value is '2'")
    case 3:
        print("Value is 3")
    case _:
        print("Value is not 1, '2' or 3")