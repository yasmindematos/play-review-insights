# Prompt de Análise — Temas e Sentimento via IA

Este é o prompt usado para a etapa de IA do projeto: pegar as reviews coletadas
pelo `scraper.py` e transformá-las em insights de produto estruturados.

## Como usar

1. Rode `scraper.py` e gere o `reviews_coletados.csv`
2. Abra o CSV e copie as colunas `app`, `nota`, `texto` (em lotes de ~30-40
   reviews por vez, para não exceder o limite de contexto)
3. Cole o prompt abaixo + o lote de reviews em uma conversa com o Claude
   (claude.ai) ou outro LLM de sua preferência
4. Repita para cada app/lote
5. Consolide os resultados na planilha final de insights

---

## PROMPT (copie a partir daqui)

Você é um analista de produto especializado em síntese de feedback de usuários.

Abaixo está uma lista de reviews públicas de um aplicativo de notícias,
extraídas da Google Play Store. Cada review tem: nome do app, nota (1-5) e texto.

**Sua tarefa:**

1. Identifique os 5-8 principais TEMAS recorrentes nas reviews (ex: "anúncios
   excessivos", "notificações em excesso", "paywall/assinatura", "performance/
   travamentos", "qualidade do conteúdo", "navegação/UX", "atendimento ao
   cliente").

2. Para cada tema, classifique o SENTIMENTO predominante (positivo, negativo
   ou misto) e estime a FREQUÊNCIA (quantas reviews tocam nesse tema, em
   números absolutos e %).

3. Para cada tema, selecione 1-2 trechos REAIS e CURTOS (até 15 palavras) que
   ilustrem o ponto — sempre entre aspas e citando que é uma citação direta de
   usuário.

4. Para cada tema, sugira uma IMPLICAÇÃO DE PRODUTO: o que esse padrão sugere
   que a equipe de produto deveria investigar, testar ou priorizar.

**Formato de saída (markdown, tabela):**

| Tema | Sentimento | Frequência | Exemplo de review | Implicação de produto |
|---|---|---|---|---|
| ... | ... | ... | "..." | ... |

Ao final, escreva um parágrafo de síntese geral comparando os apps (se houver
mais de um no lote), destacando o que o app do UOL Notícias faz melhor ou pior
que os concorrentes nesses temas.

**Reviews para análise:**

[COLE AQUI AS LINHAS DO CSV: app, nota, texto]

---

## Dica de produto

Esse processo manual de "rodar o prompt em lotes" é proposital: faz parte da
documentação do case mostrar que você testou, iterou e validou o prompt — não
é "rodar um script e aceitar o que sair". Guarde 2-3 exemplos de output desse
prompt (prints ou trechos) para usar no README do GitHub como evidência do
método.
