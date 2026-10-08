"""Interface por turnos desenhada com Pygame, sem arquivos de imagens."""
from contextlib import redirect_stdout
from io import StringIO
from collections import deque

import pygame

try:
    from .batalha import Batalha
except ImportError:
    from batalha import Batalha


class InterfacePygame:
    LARGURA, ALTURA = 1000, 720
    FUNDO = (18, 24, 38)
    PAINEL = (30, 40, 58)
    TEXTO = (234, 239, 247)

    def __init__(self, criar_campanha):
        self.criar_campanha = criar_campanha
        self.botoes = [
            (pygame.Rect(40, 620, 215, 55), "1", "1 · Atacar"),
            (pygame.Rect(275, 620, 215, 55), "2", "2 · Poção +25"),
            (pygame.Rect(510, 620, 215, 55), "3", "3 · Fugir"),
            (pygame.Rect(745, 620, 215, 55), "r", "R · Reiniciar"),
        ]
        self.reiniciar()

    def reiniciar(self):
        self.campanha = self.criar_campanha()
        self.etapa = 0
        self.resultado = None
        self.registro = deque(maxlen=100)
        self.preparar_batalha()

    def preparar_batalha(self):
        self.batalha = Batalha(self.campanha.jogador, self.campanha.inimigos[self.etapa])
        self.registro.append(f"Etapa {self.etapa + 1}: {self.batalha.inimigo.nome}")

    def agir(self, acao):
        if acao == "r":
            self.reiniciar()
            return
        if self.resultado is not None:
            return
        saida = StringIO()
        with redirect_stdout(saida):
            resultado = self.batalha.executar_turno(acao)
        self.registro.extend(saida.getvalue().splitlines())
        if resultado == "vitoria":
            self.registro.append(f"Você venceu {self.batalha.inimigo.nome}!")
            if self.etapa + 1 < len(self.campanha.inimigos):
                self.etapa += 1
                self.preparar_batalha()
            else:
                self.resultado = "vitoria"
                self.registro.append("Parabéns! Você completou a campanha!")
        elif resultado in ("derrota", "fuga"):
            self.resultado = resultado
            self.registro.append("Campanha encerrada. Pressione R para tentar novamente.")

    def texto(self, valor, posicao, grande=False, cor=None):
        fonte = self.fonte_titulo if grande else self.fonte
        self.tela.blit(fonte.render(str(valor), True, cor or self.TEXTO), posicao)

    def personagem(self, personagem, x, cor, inimigo=False):
        pygame.draw.rect(self.tela, self.PAINEL, (x, 110, 440, 270), border_radius=16)
        self.texto(personagem.nome, (x + 20, 125))
        proporcao = max(0, min(1, personagem.vida / personagem.vida_maxima))
        pygame.draw.rect(self.tela, (55, 63, 78), (x + 20, 166, 400, 18), border_radius=6)
        if proporcao:
            pygame.draw.rect(self.tela, cor, (x + 20, 166, int(400 * proporcao), 18), border_radius=6)
        self.texto(f"Vida: {max(0, personagem.vida)}/{personagem.vida_maxima}", (x + 20, 195))
        centro = (x + 220, 267)
        pygame.draw.circle(self.tela, cor, centro, 26)
        pygame.draw.rect(self.tela, cor, (x + 195, 294, 50, 35), border_radius=8)
        if inimigo:
            pygame.draw.polygon(self.tela, cor, [(x + 194, 260), (x + 187, 230), (x + 211, 246)])
            pygame.draw.polygon(self.tela, cor, [(x + 246, 260), (x + 253, 230), (x + 229, 246)])
        self.texto(f"Ataque: {personagem.ataque}   Defesa: {personagem.defesa}", (x + 20, 342))

    def desenhar(self):
        self.tela.fill(self.FUNDO)
        self.texto("JOGO DE BATALHA", (40, 25), grande=True)
        mensagens = {"vitoria": "Campanha concluída!", "derrota": "Você foi derrotado", "fuga": "Você fugiu"}
        self.texto(mensagens.get(self.resultado, f"Etapa {self.etapa + 1}/{len(self.campanha.inimigos)} · Seu turno"), (40, 72))
        self.personagem(self.batalha.jogador, 40, (89, 194, 157))
        self.personagem(self.batalha.inimigo, 520, (229, 119, 105), inimigo=True)
        pygame.draw.rect(self.tela, self.PAINEL, (40, 400, 920, 200), border_radius=12)
        self.texto("Registro da batalha", (60, 412))
        linhas = []
        for mensagem in self.registro:
            linha = ""
            for palavra in mensagem.split():
                candidata = f"{linha} {palavra}".strip()
                if self.fonte.size(candidata)[0] > 880 and linha:
                    linhas.append(linha)
                    linha = palavra
                else:
                    linha = candidata
            linhas.append(linha)
        for indice, linha in enumerate(linhas[-5:]):
            self.texto(linha, (60, 447 + indice * 28))
        for rect, acao, rotulo in self.botoes:
            habilitado = self.resultado is None or acao == "r"
            cor = (51, 91, 115) if habilitado else (43, 48, 59)
            if habilitado and rect.collidepoint(pygame.mouse.get_pos()):
                cor = (66, 121, 146)
            pygame.draw.rect(self.tela, cor, rect, border_radius=10)
            self.texto(rotulo, (rect.x + 15, rect.y + 17))
        self.texto("Clique nos botões ou use 1, 2, 3 e R. Esc: sair.", (40, 689))

    def processar_evento(self, evento):
        if evento.type == pygame.QUIT:
            return False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return False
            atalhos = {pygame.K_1: "1", pygame.K_2: "2", pygame.K_3: "3", pygame.K_r: "r"}
            if evento.key in atalhos:
                self.agir(atalhos[evento.key])
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for rect, acao, _ in self.botoes:
                if rect.collidepoint(evento.pos):
                    self.agir(acao)
                    break
        return True

    def executar(self):
        pygame.display.init()
        pygame.font.init()
        try:
            self.tela = pygame.display.set_mode((self.LARGURA, self.ALTURA))
            pygame.display.set_caption("Jogo de Batalha")
            self.fonte = pygame.font.Font(None, 26)
            self.fonte_titulo = pygame.font.Font(None, 42)
            relogio = pygame.time.Clock()
            rodando = True
            while rodando:
                for evento in pygame.event.get():
                    if not self.processar_evento(evento):
                        rodando = False
                        break
                if rodando:
                    self.desenhar()
                    pygame.display.flip()
                    relogio.tick(60)
        finally:
            pygame.quit()
