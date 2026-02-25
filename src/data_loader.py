"""
Corporate Risk & Performance Assistant
Data Loading Module

Responsável por:
- Carregar dados
- Validar estrutura
- Tratar inconsistências
- Retornar DataFrame pronto para análise
"""

import pandas as pd
import os


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        """
        Carrega os dados de um arquivo CSV.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")

        print("📥 Carregando dados...")
        df = pd.read_csv(self.file_path)

        print("✅ Dados carregados com sucesso!")
        return df

    def validate_data(self, df: pd.DataFrame) -> None:
        """
        Valida estrutura básica do dataset.
        """
        print("🔎 Validando estrutura dos dados...")

        if df.empty:
            raise ValueError("O dataset está vazio!")

        print(f"📊 Linhas: {df.shape[0]}")
        print(f"📊 Colunas: {df.shape[1]}")
        print("✅ Validação concluída!")

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Tratamento inicial de dados.
        """
        print("🧹 Tratando valores nulos...")

        df = df.dropna()

        print("✅ Dados tratados com sucesso!")
        return df
