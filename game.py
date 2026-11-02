import random

def randoom():
    opc = ["PEDRA", "PAPEL", "TESOURA"]
    return random.choice(opc)

def escolha_player():
    print("------- Pedra, Papel e Tesoura -------")
    player = input("Escolha: ").strip().upper()

    return player

esc = {"PEDRA": 0, "PAPEL": 1, "TESOURA": 2}

player = escolha_player()
pc = randoom()

if player not in esc:
    print("Escolha invalida! Digite PEDRA, PAPEL ou TESOURA.")

else:
    jogador = esc[player]
    computador = esc[pc]

    print(f"\nO computador escolheu: {pc}")
    print(f"Voce escolheu: {player}")

    if jogador == computador:
        print("Deu empate!")

    elif (jogador - computador) % 3 == 1:
        print("Voce venceu!")

    else:
        print("Voce perdeu!")
