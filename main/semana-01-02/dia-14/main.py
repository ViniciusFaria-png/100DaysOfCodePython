import random
print("Mini-projeto: combinando estruturas de controle")

print("Bem-vindo ao jogo de adivinhacao!")

while True:
    score = 0
    print("Qual o nivel de dificuldade?")
    print("1 - Facil")
    print("2 - Medio")
    print("3 - Dificil")

    nivel = int(input("Escolha o nivel: "))

    value = random.randint(1, 100)

    match nivel:
        case 1:
            tentativas = 20
            multiplier = 1
        case 2:
            tentativas = 10
            multiplier = 5
        case 3: 
            tentativas = 5
            multiplier = 10
        case _:
            print("Nível inválido!")
            continue

    print(f"Voce escolheu o nível {nivel}, voce tera {tentativas} tentativas com um multiplicador de {multiplier}, boa sorte!")
    
    while tentativas > 0:
        print(f"Voce tem {tentativas} tentativas restantes.")
        guess = int(input("Advinhe o número: "))
        tentativas -= 1

        if guess == value:
            score += tentativas * multiplier
            print(f"Parabens! Voce acertou! Seu score e {score}")
            break
        elif guess > value:
            print("O numero e Menor")
        else:
            print("O numero e Maior")
    
    if tentativas == 0:
        print(f"Voce perdeu! O numero era {value}")
    
    play_again = input("Desenha jogar novamente? (s/n): ")
    if play_again == "n":
        break
    else:
        continue

