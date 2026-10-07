import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.batalha import Batalha
from src.guerreiro import Guerreiro
from src.inimigo import Inimigo
from src.mago import Mago


def test_batalha_vitoria(monkeypatch, capsys):
    jogador = Guerreiro("Arthur")
    inimigo = Inimigo("Goblin", 10, 1, 0)

    monkeypatch.setattr("builtins.input", lambda _: "1")

    Batalha(jogador, inimigo).iniciar()

    assert inimigo.esta_vivo() is False
    assert jogador.esta_vivo() is True

    assert "venceu a batalha" in capsys.readouterr().out


def test_batalha_derrota(monkeypatch, capsys):
    jogador = Mago("Merlin")
    inimigo = Inimigo("Goblin", 100, 100, 0)

    monkeypatch.setattr("builtins.input", lambda _: "1")

    Batalha(jogador, inimigo).iniciar()

    assert jogador.esta_vivo() is False

    assert "venceu a batalha" in capsys.readouterr().out


def test_batalha_fuga(monkeypatch, capsys):
    jogador = Guerreiro("Arthur")
    inimigo = Inimigo("Goblin", 100, 20, 0)

    monkeypatch.setattr("builtins.input", lambda _: "3")

    Batalha(jogador, inimigo).iniciar()

    assert jogador.vida == 120
    assert inimigo.vida == 100

    assert "fugiu da batalha" in capsys.readouterr().out


def test_batalha_opcao_invalida(monkeypatch, capsys):
    jogador = Guerreiro("Arthur")
    inimigo = Inimigo("Goblin", 10, 1, 0)

    opcoes = iter(["9", "1"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(opcoes)
    )

    Batalha(jogador, inimigo).iniciar()

    saida = capsys.readouterr().out

    assert "Opção inválida." in saida
    assert inimigo.esta_vivo() is False


def test_batalha_uso_de_item(monkeypatch):
    jogador = Guerreiro("Arthur")

    jogador.vida = 80

    inimigo = Inimigo("Goblin", 10, 20, 0)

    opcoes = iter(["2", "1"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(opcoes)
    )

    Batalha(jogador, inimigo).iniciar()

    assert jogador.vida == 100
    assert inimigo.esta_vivo() is False