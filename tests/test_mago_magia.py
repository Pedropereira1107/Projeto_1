import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.guerreiro import Guerreiro
from src.mago import Mago


def test_magia_causa_dano_e_gasta_mana():
    mago = Mago("Merlin")  # ataque 30, mana 100
    guerreiro = Guerreiro("Arthur")  # vida 120, defesa 15
    mago.usar_magia(guerreiro)
    assert guerreiro.vida == 75  # magia = 60; 60 - 15 = 45 de dano
    assert mago.mana == 80  # custo de 20


def test_magia_sem_mana_suficiente_nao_faz_nada():
    mago = Mago("Merlin")
    guerreiro = Guerreiro("Arthur")
    mago.mana = 10
    mago.usar_magia(guerreiro)
    assert guerreiro.vida == 120
    assert mago.mana == 10


def test_mana_nunca_fica_negativa():
    mago = Mago("Merlin")
    guerreiro = Guerreiro("Arthur")
    for _ in range(6):  # 100 de mana = 5 magias; a sexta deve falhar
        mago.usar_magia(guerreiro)
    assert mago.mana == 0