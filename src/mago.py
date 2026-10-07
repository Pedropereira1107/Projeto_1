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
        custo_mana = 20
        dano_magia = self.ataque * 2

        if self.mana < custo_mana:
            print("O mago não possui mana suficiente.")
            return

        self.mana -= custo_mana
        alvo.receber_dano(dano_magia)
        print(f"{self.nome} lançou uma magia em {alvo.nome}! (mana restante: {self.mana})")