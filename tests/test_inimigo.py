import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.guerreiro import Guerreiro
from src.inimigo import Inimigo


def test_inimigo_ataca_e_alvo_perde_vida():
    inimigo = Inimigo("Goblin", 50, 25, 0)  # nome, vida, ataque, defesa
    guerreiro = Guerreiro("Arthur")  # vida 120, defesa 15

    inimigo.atacar(guerreiro)

    assert guerreiro.vida == 110  # 25 - 15 = 10 de dano
    assert inimigo.vida == 50  # quem ataca não perde vida