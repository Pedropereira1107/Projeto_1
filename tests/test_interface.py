import os
import sys
from pathlib import Path

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pygame

from src.campanha import Campanha
from src.arqueiro import Arqueiro
from src.inimigo import Inimigo
from src.interface import InterfacePygame


def criar_campanha():
    return Campanha(Arqueiro("Arthur"), [
        Inimigo("Primeiro", 10, 12, 0),
        Inimigo("Segundo", 10, 12, 0),
    ])


def test_vitoria_avanca_e_encerra_campanha_sem_contra_ataque():
    interface = InterfacePygame(criar_campanha)
    interface.agir("1")
    assert interface.etapa == 1
    assert interface.batalha.jogador.vida == 110
    interface.agir("1")
    assert interface.resultado == "vitoria"
    interface.agir("2")
    assert interface.resultado == "vitoria"


def test_pocao_e_contra_ataque():
    interface = InterfacePygame(criar_campanha)
    interface.batalha.jogador.vida = 60
    interface.agir("2")
    assert interface.batalha.jogador.vida == 83
    assert any("recuperou 25" in linha for linha in interface.registro)


def test_fuga_bloqueia_acoes_e_reinicio_recria_personagens():
    interface = InterfacePygame(criar_campanha)
    jogador = interface.batalha.jogador
    interface.agir("3")
    interface.agir("1")
    assert interface.resultado == "fuga"
    assert interface.batalha.inimigo.vida == 10
    interface.agir("r")
    assert interface.resultado is None
    assert interface.etapa == 0
    assert interface.batalha.jogador is not jogador


def test_derrota_encerra_campanha():
    interface = InterfacePygame(criar_campanha)
    interface.batalha.jogador.vida = 1
    interface.batalha.inimigo.vida = 100
    interface.agir("1")
    assert interface.resultado == "derrota"
    assert interface.etapa == 0


def test_eventos_mouse_teclado_renderizacao_e_fechamento():
    interface = InterfacePygame(criar_campanha)
    pygame.display.init()
    pygame.font.init()
    try:
        interface.tela = pygame.display.set_mode((1000, 720))
        interface.fonte = pygame.font.Font(None, 26)
        interface.fonte_titulo = pygame.font.Font(None, 42)
        interface.desenhar()
        interface.processar_evento(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(60, 640)))
        assert interface.etapa == 1
        interface.processar_evento(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_3))
        assert interface.resultado == "fuga"
        interface.desenhar()
        assert interface.processar_evento(pygame.event.Event(pygame.QUIT)) is False
        assert interface.processar_evento(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)) is False
    finally:
        pygame.quit()
