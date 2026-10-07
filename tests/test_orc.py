import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.guerreiro import Guerreiro
from src.inimigo import Inimigo
from src.orc import Orc


def test_orc_e_um_inimigo_com_atributos_proprios():
    orc = Orc()

    assert isinstance(orc, Inimigo)
    assert orc.nome == "Orc"
    assert orc.vida == 100
    assert orc.ataque == 20
    assert orc.defesa == 10


def test_orc_ataca_normalmente_com_vida_alta():
    orc = Orc()
    guerreiro = Guerreiro("Arthur")  # vida 120, defesa 15

    orc.atacar(guerreiro)

    assert guerreiro.vida == 113  # 22 - 15 = 7 de dano
    assert orc.vida == 150  # quem ataca não perde vida


def test_orc_entra_em_furia_com_vida_baixa():
    orc = Orc()
    orc.vida = 70  # abaixo de 50% da vida máxima (150)
    guerreiro = Guerreiro("Arthur")  # vida 120, defesa 15

    assert orc.em_furia() is True

    orc.atacar(guerreiro)

    assert guerreiro.vida == 102  # ataque 22 * 1.5 = 33; 33 - 15 = 18 de dano


def test_orc_com_exatamente_metade_da_vida_esta_em_furia():
    orc = Orc()
    orc.vida = 75

    assert orc.em_furia() is True


def test_orc_com_vida_acima_da_metade_nao_esta_em_furia():
    orc = Orc()
    orc.vida = 76

    assert orc.em_furia() is False
