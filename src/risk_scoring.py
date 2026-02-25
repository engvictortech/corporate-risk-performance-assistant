"""
Corporate Risk & Performance Assistant
Risk Scoring Module

Responsável por:
- Gerar score individual por cliente
- Classificar nível de risco
- Identificar clientes críticos
"""

import pandas as pd


class RiskScoring:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def calculate_score(self) -> pd.DataFrame:
        """
        Gera score baseado em regras de negócio.
        """

        score = 0

        # Regra 1: Receita
        # Quanto menor a receita, maior o risco
        self.df["score"] = 0
        self.df.loc[self.df["receita"] < 15000, "score"] += 30
        self.df.loc[self.df["receita"] >= 15000, "score"] += 10

        # Regra 2: Tempo de contrato
        # Contratos curtos são mais arriscados
        self.df.loc[self.df["tempo_contrato_meses"] < 12, "score"] += 30
        self.df.loc[self.df["tempo_contrato_meses"] >= 12, "score"] += 10

        # Regra 3: Classificação de risco declarada
        self.df.loc[self.df["risco"] == "alto", "score"] += 40
        self.df.loc[self.df["risco"] == "medio", "score"] += 20
        self.df.loc[self.df["risco"] == "baixo", "score"] += 5

        return self.df

    def classify_risk(self) -> pd.DataFrame:
        """
        Classifica cliente com base no score final.
        """

        def categoria(score):
            if score >= 80:
                return "ALTO RISCO"
            elif score >= 50:
                return "RISCO MÉDIO"
            else:
                return "BAIXO RISCO"

        self.df["categoria_risco"] = self.df["score"].apply(categoria)

        return self.df

    def top_risky_clients(self, top_n=5) -> pd.DataFrame:
        """
        Retorna os clientes mais arriscados.
        """
        return self.df.sort_values(by="score", ascending=False).head(top_n)
