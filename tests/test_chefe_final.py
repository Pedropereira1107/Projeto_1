import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.chefe_final import ChefeFinal
from src.guerreiro import Guerreiro


def test_chefe_final_tem_atributos_elevados():
    chefe = ChefeFinal()

    assert chefe.vida == 250
    assert chefe.vida_maxima == 250
    assert chefe.ataque == 30
    assert chefe.defesa == 15


def test_chefe_final_e_um_inimigo():
    chefe = ChefeFinal()

    assert chefe.esta_vivo() is True
    assert hasattr(chefe, "atacar")


def test_chefe_final_usa_ataque_especial():
    chefe = ChefeFinal()
    guerreiro = Guerreiro("Arthur")

    chefe.ataque_especial(guerreiro)

    assert guerreiro.vida == 75