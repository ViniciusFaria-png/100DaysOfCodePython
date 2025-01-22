print("Criacao e acesso a listas")

# Criando uma lista vazia

lista = []

# Adicionando elementos a lista

lista.append(1)
lista.append(2)
lista.append(3)

print(lista)

# Acessando elementos da lista

lista[0] = 10
print(lista[0])

# Acessando elementos da lista com for

for i in lista:
    print(i)

# Acessando elementos da lista com for e range

for i in range(len(lista)):
    print(lista[i])

# Acessando elementos da lista com for e enumerate

for i, v in enumerate(lista):
    print(i, v)

lista.remove(2)
print(lista)

lista.sort()
print(lista)

lista.reverse()
print(lista)

lista.insert(1, 2)
print(lista)