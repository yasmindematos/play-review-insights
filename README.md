# Análise de Reviews de Apps de Notícias com IA

> Mini-estudo de produto: extraindo temas e insights acionáveis de reviews
> públicas da Play Store, com apoio de IA generativa, comparando o APP Not. a 4 concorrentes diretos.

## O problema

Apps de notícias recebem milhares de reviews públicas, mas poucas equipes de
produto têm tempo de ler review por review para identificar padrões. Este
projeto testa um fluxo leve — coleta + IA — para transformar feedback não
estruturado em insights priorizáveis, comparando o app **Notícias** a 4
concorrentes diretos: **G1, Folha de S.Paulo, Estadão e R7**.

## Hipótese

Reviews públicas, mesmo sem estrutura, concentram sinais recorrentes
(reclamações sobre anúncios, performance, paywall) que podem ser extraídos
com apoio de IA generativa mais rápido do que com leitura manual — e ainda
assim com qualidade suficiente para embasar decisões de priorização.

## Método

1. **Coleta:** script Python (`scraper.py`) usando a biblioteca
   `google-play-scraper` para extrair ~60 reviews públicas recentes de cada
   um dos 5 apps de notícias.
2. **Extração de temas e sentimento com IA:** as reviews coletadas foram
   processadas por um LLM (Claude), usando um prompt estruturado
   (`prompt_analise_ia.md`) para identificar temas recorrentes, sentimento
   predominante, frequência e implicações de produto.
3. **Consolidação e visualização:** os temas extraídos foram agregados e
   visualizados por frequência entre os 5 apps.

## Achado principal: performance é o maior risco competitivo

O **Estadão concentra 67% das reviews citando lentidão, travamento ou falha
ao carregar** — disparado o maior da categoria nesta amostra. O app Notícias
(17%) está em linha com Folha (18%).

## Implicação mais relevante

1. **Modo escuro ausente é o pedido mais repetido e específico** —
   aparece em múltiplas reviews ao longo de meses, sempre como crítica
   direta. Provavelmente o quick win de maior relação esforço/impacto
   identificado nesta análise.

## Limitações

- Amostra de ~45-60 reviews por app, ordenadas pelas mais recentes — não é
  estatisticamente representativa
- Reviews têm viés de seleção (usuários muito insatisfeitos ou muito
  engajados tendem a escrever mais)
- R7 mistura reviews sobre o app de notícias com funcionalidades de TV/reality
  show, o que dilui a comparabilidade direta nesse caso específico
- Classificação de tema/sentimento via IA generativa é uma aproximação útil
  para priorização exploratória, não substitui análise qualitativa profunda

## Possiveis próximos passos

- Aumentar o volume de reviews e repetir a coleta periodicamente para
  observar tendência ao longo do tempo
- Cruzar os temas extraídos com dados internos de produto para validar se
  os sinais públicos refletem o uso real
- Automatizar a etapa de extração via API, eliminando o processo manual de
  colar lotes

## Stack

`Python` · `google-play-scraper` · `pandas` · `matplotlib` · `Claude (Anthropic)` para extração de temas/sentimento

---

📫 Yasmin De Matos · [LinkedIn](https://www.linkedin.com/in/yasmindematos/)
