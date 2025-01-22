print("List comprehension")

# List comprehension é uma forma concisa de criar listas em Python
# É uma forma mais elegante e legível de criar listas

# Exemplo 1: criar uma lista com os números de 1 a 10
# Usando um loop for
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

# Usando list comprehension
numbers = [i for i in range(1, 11)]
print(numbers)

# Exemplo 2: criar uma lista com os números pares de 1 a 10
# Usando um loop for
even_numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

# Usando list comprehension
even_numbers = [i for i in range(1, 11) if i % 2 == 0]