try:
    from .personagem import Personagem
except ImportError:
    from personagem import Personagem

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome = nome, vida = 110, ataque = 15, defesa = 10)
    def atacar(self, alvo):
        alvo.receber_dano(self.ataque)
        print(f"{self.personagem.nome} atacou {self.alvo.nome}")
