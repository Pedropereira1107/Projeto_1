import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.guerreiro import Guerreiro
from src.mago import Mago


def test_mago_ataca_e_alvo_perde_vida():
    mago = Mago("Merlin")  # ataque 30
    guerreiro = Guerreiro("Arthur")  # vida 120, defesa 15

    mago.atacar(guerreiro)

    assert guerreiro.vida == 105  # 30 - 15 = 15 de dano
    assert mago.mana == 100  # ataque normal não gasta mana