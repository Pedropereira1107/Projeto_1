from guerreiro import Guerreiro
from inimigo import Inimigo
from batalha import Batalha
from arqueiro import Arqueiro
from orc import Orc
def main():

    jogador = Arqueiro("Arthur")

    inimigo = Orc(
        nome="Orc",
        vida=100,
        ataque=20,
        defesa=10
    )

    batalha = Batalha(jogador, inimigo)

    batalha.iniciar()


if __name__ == "__main__":
    main()
