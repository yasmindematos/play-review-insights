"""
Play Store Review Miner — Coleta de reviews públicos para análise de produto
================================================================================
Coleta reviews públicos de apps de notícias (UOL Notícias + concorrentes)
para análise de temas e sentimento com apoio de IA.

Uso:
    python scraper.py

Saída:
    reviews_coletados.csv — todas as reviews coletadas, prontas para análise
"""

from google_play_scraper import reviews, Sort
import pandas as pd
import time

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO: apps a analisar (package name = ID do app na Play Store,
# visível na URL: play.google.com/store/apps/details?id=AQUI)
# -----------------------------------------------------------------------------
APPS = {
    "UOL Notícias":      "br.uol.noticias",
    "G1":                "com.globo.g1.app",
    "Folha de S.Paulo":  "br.com.folha.app",
    "Estadão":           "com.fett.android.estadao",
    "R7":                "com.r7.r7",
}

REVIEWS_PER_APP = 60          # quantidade de reviews por app
LANG = "pt"
COUNTRY = "br"


def coletar_reviews():
    todas_reviews = []

    for nome_app, package_id in APPS.items():
        print(f"Coletando reviews de {nome_app} ({package_id})...")
        try:
            result, _ = reviews(
                package_id,
                lang=LANG,
                country=COUNTRY,
                sort=Sort.NEWEST,
                count=REVIEWS_PER_APP,
            )
        except Exception as e:
            print(f"  ⚠️  Erro ao coletar {nome_app}: {e}")
            continue

        print(f"  ✅ {len(result)} reviews coletadas")

        for r in result:
            todas_reviews.append({
                "app": nome_app,
                "package_id": package_id,
                "data": r["at"],
                "nota": r["score"],
                "texto": r["content"],
                "curtidas": r.get("thumbsUpCount", 0),
            })

        time.sleep(1)  # gentileza com a API pública

    df = pd.DataFrame(todas_reviews)
    df.to_csv("reviews_coletados.csv", index=False, encoding="utf-8-sig")
    print(f"\n🎉 Total: {len(df)} reviews salvas em reviews_coletados.csv")
    return df


if __name__ == "__main__":
    coletar_reviews()
