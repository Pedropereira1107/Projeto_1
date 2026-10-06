import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.guerreiro import Guerreiro
from src.mago import Mago


def test_guerreiro_ataca_e_alvo_perde_vida():
    guerreiro = Guerreiro("Arthur")  # ataque 20
    mago = Mago("Merlin")  # vida 80, defesa 5

    guerreiro.atacar(mago)

    assert mago.vida == 65  # 20 - 5 = 15 de dano
    assert guerreiro.vida == 120  # quem ataca não perde vida