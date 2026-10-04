try:
    from .personagem import Personagem
except ImportError:
    from personagem import Personagem


class Inimigo(Personagem):

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(
            nome=nome,
            vida=vida,
            ataque=ataque,
            defesa=defesa
        )

    def atacar(self, alvo):
        # TODO: implementar ataque
        alvo.receber_dano(self.ataque)
        print(f"{self.nome} atacou {alvo.nome} !")