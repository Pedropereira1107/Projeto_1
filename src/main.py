import argparse

try:
    from .arqueiro import Arqueiro
    from .inimigo import Inimigo
    from .orc import Orc
    from .campanha import Campanha
    from .chefe_final import ChefeFinal
except ImportError:
    from arqueiro import Arqueiro
    from inimigo import Inimigo
    from orc import Orc
    from campanha import Campanha
    from chefe_final import ChefeFinal

def criar_campanha():
    jogador = Arqueiro("Arthur")

    inimigos = [
        Inimigo("Goblin", vida=40, ataque=12, defesa=2),
        Inimigo("Goblin Veterano", vida=60, ataque=15, defesa=5),
        Orc("Gruk"),
        ChefeFinal("Donkey Kong, Chefe Final")
    ]

    return Campanha(jogador, inimigos)


def main():
    parser = argparse.ArgumentParser(description="Jogo de batalha por turnos")
    parser.add_argument("--terminal", action="store_true", help="Jogar pelo terminal")
    args = parser.parse_args()
    if args.terminal:
        criar_campanha().iniciar()
    else:
        try:
            if __package__:
                from .interface import InterfacePygame
            else:
                from interface import InterfacePygame
        except ModuleNotFoundError as erro:
            if erro.name != "pygame":
                raise
            parser.exit(1, "Instale as dependências: python -m pip install -r requirements.txt\n")
        InterfacePygame(criar_campanha).executar()


if __name__ == "__main__":
    main()
