"""
Corporate Risk & Performance Assistant
Strategic Performance Analysis Module

Responsável por:
- Calcular métricas executivas
- Gerar indicadores de risco
- Produzir insights estratégicos
"""

import pandas as pd


class PerformanceAnalyzer:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def calculate_kpis(self) -> dict:
        """
        Calcula principais indicadores executivos.
        """
        total_receita = self.df["receita"].sum()
        receita_media = self.df["receita"].mean()
        taxa_inadimplencia = self.df["inadimplente"].mean() * 100
        tempo_medio_contrato = self.df["tempo_contrato_meses"].mean()

        risco_alto_percentual = (
            (self.df["risco"] == "alto").mean() * 100
        )

        return {
            "Receita Total": total_receita,
            "Receita Média": receita_media,
            "Taxa de Inadimplência (%)": taxa_inadimplencia,
            "Tempo Médio de Contrato": tempo_medio_contrato,
            "Clientes Risco Alto (%)": risco_alto_percentual
        }

    def receita_por_segmento(self) -> pd.Series:
        """
        Retorna receita média por segmento.
        """
        return self.df.groupby("segmento")["receita"].mean()

    def gerar_insights(self) -> list:
        """
        Gera insights estratégicos automáticos.
        """
        insights = []

        if self.df["inadimplente"].mean() > 0.2:
            insights.append("⚠️ Taxa de inadimplência acima de 20%.")

        if self.df.groupby("segmento")["inadimplente"].mean().idxmax() == "pm e":
            insights.append("📉 Segmento PME apresenta maior risco de inadimplência.")

        if self.df["receita"].mean() > 20000:
            insights.append("💰 Receita média saudável acima de 20k.")

        return insights
