# ⚔️ Jogo de Batalha

Projeto desenvolvido na disciplina de Programação Orientada a Objetos.

## Executando o projeto

Na raiz do projeto:

```powershell
python -m pip install -r requirements.txt
python src/main.py
```

A interface gráfica utiliza Pygame Community Edition (`pygame-ce`, importado
como `pygame`). Exibe barras de vida, atributos e o registro da batalha.
Clique nos botões ou use as teclas 1 (atacar), 2 (poção de vida),
**3** (fugir) e **R** (reiniciar a campanha). **Esc** fecha a janela.
Cada ação de ataque ou poção permite o contra-ataque do inimigo, se estiver vivo.
As etapas avançam automaticamente após a vitória, mantendo a vida do jogador.

Para usar o ambiente virtual já existente no Windows:

```powershell
.\.venv-py314\Scripts\python.exe -m pip install -r requirements.txt
.\.venv-py314\Scripts\python.exe src/main.py
```

O modo terminal continua disponível com `python src/main.py --terminal`.
Também é possível iniciar com `python -m src.main`.

Para executar os testes: `python -m pytest -q`.

Fluxo de desenvolvimento:

Cada funcionalidade deve ser desenvolvida em uma branch própria.

Exemplo:

feature/ataque-guerreiro

Depois:

```bash
git add .
git commit -m "feat: implementa ataque do guerreiro"
git push
```

Após o push, abra um Pull Request no GitHub.

Regras:
- Não desenvolver diretamente na branch main.
- Cada funcionalidade deve possuir uma issue.
- Cada issue deve ser desenvolvida em uma branch.
- O Pull Request deve ser revisado por outro aluno.
- O código deve passar pelos testes antes do merge.
