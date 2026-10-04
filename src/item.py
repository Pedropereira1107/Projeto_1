class Item:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class PocaoVida(Item):
    def __init__(self):
        super().__init__(nome="Poção de Vida", valor=25)

    def usar(self, personagem):
        vida_antes = personagem.vida
        personagem.vida = min(personagem.vida + self.valor, personagem.vida_maxima)

        vida_recuperada = personagem.vida - vida_antes

        if vida_recuperada > 0:
            print(
                f"{personagem.nome} usou {self.nome} "
                f"e recuperou {vida_recuperada} de vida."
            )
        else:
            print(f"{personagem.nome} ja esta com a vida cheia.")


