print("Strings e formatação básica")

print("Strings com aspas simples")
'Hello, World!'
print("Strings com aspas duplas")
"Hello, World!"
print("Strings com aspas triplas(Multilinhas)")
"""Hello, World!""" 'ou' '''Hello, World!'''	
print("Concatenação de strings")
"Olá" + " " + "Mundo!"
print("Repetição de strings")
"Python" * 3
print("Tamanho de uma string")
len("Python")
print("Acessando elementos de uma string")
"Python"[0] # P - Primeiro Caractere da string
print("Fatiamento de strings")
"Python"[0:3] # Pyt - Fatiamento da string


texto = "Python programming language"

texto.upper() # PYTHON PROGRAMMING LANGUAGE
texto.lower() # python programming language
texto.capitalize() # Python programming language
texto.title() # Python Programming Language

texto.strip() # Remove espaços em branco do início e do fim da string
texto.lstrip() # Remove espaços em branco do início da string
texto.rstrip() # Remove espaços em branco do fim da string

texto.find("Python") # 0 - Retorna a posição da primeira ocorrência da string
texto.replace("Python", "Java") # Java programming language - Substitui uma string por outra


texto = "Python 3.8"

texto.isalpha() # False - Verifica se a string contém apenas letras
texto.isdigit() # False - Verifica se a string contém apenas números
texto.isalnum() # False - Verifica se a string contém apenas letras e números
texto.islower() # False - Verifica se a string contém apenas letras minúsculas
texto.isupper() # False - Verifica se a string contém apenas letras maiúsculas
texto.isspace() # False - Verifica se a string contém apenas espaços em branco

nome = "Python"
idade = 30


"Nome {} e Idade {}".format(nome, idade) # Nome Python e Idade 30
"Nome {n} e Idade {i}".format(n=nome, i=idade) # Nome Python e Idade 30


f"Nome {nome} e Idade {idade}" # Nome Python e Idade 30
f"idade {idade + 1}"

print("Linha 1\nLinha2") # Quebra de linha

print("Tabulação\tTabulação") # Tabulação

print("Ele disse: \"Olá!\"") # Aspas duplas dentro de aspas duplas

