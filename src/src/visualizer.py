from src.visualizer import Visualizer
import matplotlib.pyplot as plt
import seaborn as sns

# Visualizações
Visualizer.receita_por_segmento(df_clean)
Visualizer.score_distribution(df_scored)


class Visualizer:

    @staticmethod
    def receita_por_segmento(df):
        plt.figure(figsize=(8,5))
        sns.barplot(x="segmento", y="receita", data=df, ci=None)
        plt.title("Receita por Segmento")
        plt.ylabel("Receita")
        plt.xlabel("Segmento")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def score_distribution(df):
        plt.figure(figsize=(8,5))
        sns.histplot(df["score"], bins=10, kde=True)
        plt.title("Distribuição de Score de Risco")
        plt.xlabel("Score")
        plt.ylabel("Quantidade de Clientes")
        plt.tight_layout()
        plt.show()

# Exportar dados de clientes com score
df_scored.to_csv("data/clientes_scored.csv", index=False)
print("\n✅ Relatório exportado para data/clientes_scored.csv")
