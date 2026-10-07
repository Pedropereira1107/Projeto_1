try:
    from .inimigo import Inimigo
except ImportError:
    from inimigo import Inimigo


class ChefeFinal(Inimigo):
    """Chefe final com atributos elevados e um ataque especial."""

    def __init__(self, nome="Chefe Final"):
        super().__init__(
            nome=nome,
            vida=250,
            ataque=30,
            defesa=15
        )

    def ataque_especial(self, alvo):
        dano = self.ataque * 2

        alvo.receber_dano(dano)

        print(
            f"{self.nome} usou seu ataque especial "
            f"contra {alvo.nome}!"
        )