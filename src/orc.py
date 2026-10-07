try:
    from .inimigo import Inimigo
except ImportError:
    from inimigo import Inimigo


class Orc(Inimigo):
    """Inimigo resistente que fica mais perigoso quando está ferido."""

    # Quando a vida cai até essa fração da vida máxima, o Orc entra em fúria.
    LIMITE_FURIA = 0.5
    # Multiplicador do ataque enquanto estiver em fúria.
    BONUS_FURIA = 1.5

    def __init__(self, nome="Orc"):
        super().__init__(
            nome=nome,
            vida=100,
            ataque=20,
            defesa=10
        )

    def em_furia(self):
        return self.vida <= self.vida_maxima * self.LIMITE_FURIA

    def atacar(self, alvo):
        dano = self.ataque

        if self.em_furia():
            dano = int(self.ataque * self.BONUS_FURIA)
            print(f"{self.nome} entrou em fúria!")

        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} !")
