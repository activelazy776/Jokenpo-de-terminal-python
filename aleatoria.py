import random

def randoom():
    opc = ["PEDRA", "PAPEL", "TESOURA"]
    pc = random.choice(opc)
    
    return pc

def escolha_player():
    print("------- Pedra, Papel e Tesoura -------")
    player = input("Escolha: ").strip().upper()

    return player