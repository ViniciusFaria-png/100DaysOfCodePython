print("Métodos de lista")

# Métodos de lista

# Adicionando elementos a lista
lista = []
lista.append(1)
lista.append(2)
lista.append(3)

print(lista)

# Acessando elementos da lista
lista[0] = 10
print(lista[0])
print(lista)

# Acessando elementos da lista com for
for i in lista:
    print(i)

# Acessando elementos da lista com for e range
for i in range(len(lista)):
    print(lista[i])

# Acessando elementos da lista com for e enumerate
for i, v in enumerate(lista):
    print(i, v)

# Removendo elementos da lista
lista.remove(2)
print(lista)

# Insert
lista.insert(1, 2)
print(lista)
