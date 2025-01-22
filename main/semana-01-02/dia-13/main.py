print("Operador ternário")

# O operador ternário é uma forma concisa de escrever um if-else em uma única linha
# Ele é muito útil quando você precisa fazer uma verificação simples
# Sintaxe: valor_se_verdadeiro if condição else valor_se_falso

# Exemplo 1: verificar se um número é par ou ímpar
number = 10
result = "par" if number % 2 == 0 else "ímpar"
print(result)

# Exemplo 2: verificar se um número é positivo, negativo ou zero
number = -5
result = "positivo" if number > 0 else "negativo" if number < 0 else "zero"