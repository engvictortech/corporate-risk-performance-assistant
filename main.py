from src.data_loader import DataLoader
from src.performance_analyzer import PerformanceAnalyzer
from src.risk_scoring import RiskScoring

def main():
    file_path = "data/sample_data.csv"

    # Carregar dados
    loader = DataLoader(file_path)
    df = loader.load_data()
    loader.validate_data(df)
    df_clean = loader.clean_data(df)

    # Performance Analyzer
    analyzer = PerformanceAnalyzer(df_clean)
    print("\n📊 KPIs EXECUTIVOS")
    print("-" * 40)
    kpis = analyzer.calculate_kpis()
    for k, v in kpis.items():
        print(f"{k}: {v}")

    print("\n📈 Receita Média por Segmento")
    print("-" * 40)
    print(analyzer.receita_por_segmento())

    print("\n🧠 INSIGHTS ESTRATÉGICOS")
    print("-" * 40)
    for insight in analyzer.gerar_insights():
        print(insight)

    # Risk Scoring
    print("\n🚨 RISK SCORING ENGINE")
    print("-" * 40)
    scorer = RiskScoring(df_clean)
    df_scored = scorer.calculate_score()
    df_scored = scorer.classify_risk()
    print(df_scored[["cliente_id", "score", "categoria_risco"]])

    print("\n🔝 TOP 5 CLIENTES MAIS ARRISCADOS")
    print("-" * 40)
    print(scorer.top_risky_clients())

if __name__ == "__main__":
    main()
