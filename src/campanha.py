try:
    from .batalha import Batalha
except ImportError:
    from batalha import Batalha


class Campanha:
    def __init__(self, jogador, inimigos):
        self.jogador = jogador
        self.inimigos = inimigos

    def iniciar(self):
        for etapa, inimigo in enumerate(self.inimigos, start=1):
            print(f"\n---Etapa {etapa}: {inimigo.nome} ---")

            batalha = Batalha(self.jogador, inimigo)
            resultado = batalha.iniciar()

            if resultado != "vitoria":
                print("A campanha terminou.")
                return resultado

        print("\nParabéns! Você completou a campanha!")
        return "vitoria"
