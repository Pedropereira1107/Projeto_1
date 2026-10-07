from arqueiro import Arqueiro
from inimigo import Inimigo
from orc import Orc
from campanha import Campanha


def main():
    jogador = Arqueiro("Arthur")

    inimigos = [
        Inimigo("Goblin", vida=40, ataque=12, defesa=2),
        Inimigo("Goblin Veterano", vida=60, ataque=15, defesa=5),
        Orc("Gruk"),
    ]

    campanha = Campanha(jogador, inimigos)
    campanha.iniciar()


if __name__ == "__main__":
    main()
