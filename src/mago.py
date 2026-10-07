try:
    from .personagem import Personagem
except ImportError:
    from personagem import Personagem

class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=80,
            ataque=30,
            defesa=5
        )

        self.mana = 100

    def atacar(self, alvo):
       alvo.receber_dano(self.ataque)
       print(f"{self.nome} atacou {alvo.nome}!")

    def usar_magia(self, alvo):
        # TODO: implementar magia

        if self.mana <= 0:
            print("O mago não possui mana suficiente.")
            return

        pass
