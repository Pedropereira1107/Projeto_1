from guerreiro import Guerreiro
from inimigo import Inimigo
from batalha import Batalha
from arqueiro import Arqueiro

def main():

    jogador = Arqueiro("Arthur")

    inimigo = Inimigo(
        nome="Goblin",
        vida=100,
        ataque=25,
        defesa=5
    )

    batalha = Batalha(jogador, inimigo)

    batalha.iniciar()


if __name__ == "__main__":
    main()
