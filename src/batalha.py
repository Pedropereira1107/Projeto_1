try:
    from .item import PocaoVida
except ImportError:
    from item import PocaoVida

class Batalha:

    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

    def executar_turno(self, opcao):
        """Resolve uma ação sem bloquear a interface com input()."""
        if not self.jogador.esta_vivo():
            return "derrota"
        if not self.inimigo.esta_vivo():
            return "vitoria"
        if opcao == "1":
            self.jogador.atacar(self.inimigo)
        elif opcao == "2":
            PocaoVida().usar(self.jogador)
        elif opcao == "3":
            print("Você fugiu da batalha!")
            return "fuga"
        else:
            print("Opção inválida.")
            return None
        if self.inimigo.esta_vivo():
            self.inimigo.atacar(self.jogador)
        if not self.jogador.esta_vivo():
            return "derrota"
        if not self.inimigo.esta_vivo():
            return "vitoria"
        return None

    def iniciar(self):

        print("=" * 40)
        print("        INÍCIO DA BATALHA")
        print("=" * 40)

        while self.jogador.esta_vivo() and self.inimigo.esta_vivo():

            print("\n--- STATUS ---")
            self.jogador.mostrar_status()
            self.inimigo.mostrar_status()

            print("\n--- AÇÕES ---")
            print("1 - Atacar")
            print("2 - Usar item")
            print("3 - Fugir")

            opcao = input("Escolha uma opção: ")

            resultado = self.executar_turno(opcao)
            if resultado == "fuga":
                return resultado

        # TODO: verificar quem venceu
        if self.jogador.esta_vivo():
            print(f"{self.jogador.nome} venceu a batalha !")
            return "vitoria"
        else:
            print(f"{self.inimigo.nome} venceu a batalha !")
            return "derrota"
