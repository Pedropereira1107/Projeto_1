import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.guerreiro import Guerreiro
from src.mago import Mago


def test_guerreiro_esta_vivo():
    guerreiro = Guerreiro("Arthur")

    assert guerreiro.esta_vivo() is True


def test_personagem_recebe_dano():
    guerreiro = Guerreiro("Arthur")

    guerreiro.receber_dano(30)

    assert guerreiro.vida == 105


def test_personagem_morre():
    guerreiro = Guerreiro("Arthur")

    guerreiro.receber_dano(200)

    assert guerreiro.vida <= 0
    assert guerreiro.esta_vivo() is False


def test_guerreiro_ataca():
    guerreiro = Guerreiro("Arthur")
    mago = Mago("Merlin")

    guerreiro.atacar(mago)

    assert mago.vida == 65