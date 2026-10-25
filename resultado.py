from aleatoria import randoom, escolha_player

esc = {"PEDRA": 0, "PAPEL": 1, "TESOURA": 2 }

player = escolha_player()
pc = randoom()

if pc == player:
    print(f"Empate, o computador deu {pc} e você deu {player}.")
elif pc == "PEDRA" and player == "PAPEL":
    print(f"Você vençeu, o computador deu {pc} e você deu {player}.")
elif pc == "PEDRA" and player == "TESOURA":
    print(f"Você perdeu, o computador deu {pc} e você deu {player}.")
elif pc == "PAPEL" and player == "PEDRA":
    print(f"Você perdeu, o computador deu {pc} e você deu {player}.")
elif pc == "PAPEL" and player == "TESOURA":
    print(f"Você vençeu, o computador deu {pc} e você deu {player}.")
elif pc == "TESOURA" and player == "PAPEL":
    print(f"Você perdeu, o computador deu {pc} e você deu {player}.")
elif pc == "TESOURA" and player == "PEDRA":
    print(f"Você vençeu, o computador deu {pc} e você deu {player}.")