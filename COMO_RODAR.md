# Como rodar este projeto — instruções para a Yasmin

Esse projeto **não funciona no sandbox da conversa** (a Play Store não é
acessível de lá), então os passos abaixo são para rodar no **seu computador**.

## Passo 1 — Instalar Python (se ainda não tiver)

Baixe em https://www.python.org/downloads/ (marque a opção "Add Python to
PATH" durante a instalação, no Windows).

## Passo 2 — Instalar as dependências

Abra o terminal (cmd, PowerShell ou terminal do Mac) na pasta do projeto e
rode:

```bash
pip install -r requirements.txt
```

## Passo 3 — Rodar o coletor de reviews

```bash
python scraper.py
```

Isso vai gerar o arquivo `reviews_coletados.csv` na mesma pasta, com as
reviews do UOL Notícias, G1, Folha, Estadão e R7.

> Se algum app não retornar reviews, é normal — a Play Store às vezes limita
> a quantidade retornada por sessão. Rode de novo depois de alguns minutos
> se isso acontecer, ou reduza `REVIEWS_PER_APP` no script.

## Passo 4 — Analisar com IA

Abra `prompt_analise_ia.md` e siga as instruções para colar lotes do CSV em
uma conversa com o Claude (ou outro LLM). Você vai sair dessa etapa com
tabelas de temas, sentimento e implicações de produto.

## Passo 5 — Gerar o gráfico (opcional)

Depois de ter a tabela de temas consolidada (mesmo que só com 5-6 linhas),
volte para o Claude e cole a tabela pedindo um gráfico de barras dos temas
por frequência/sentimento — ou peça ajuda direto aqui na nossa conversa,
posso gerar pra você.

## Passo 6 — Escrever o case no GitHub

Use o `README_CASE_GITHUB.md` como template. Troque os placeholders pelos
seus achados reais.
