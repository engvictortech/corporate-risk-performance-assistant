📊 Análise e Previsão de Inadimplência
Projeto de Dados com foco em Fintech e Risco de Crédito
🎯 Contexto de Negócio

Instituições financeiras operam sob risco constante de inadimplência. Antecipar movimentos de deterioração do crédito é essencial para:

Reduzir perdas financeiras

Ajustar políticas de concessão

Melhorar provisionamento

Tomar decisões estratégicas baseadas em dados

Este projeto simula um cenário real de análise de risco em fintech, utilizando variáveis macroeconômicas para prever variações na inadimplência.

🧠 Problema

Como fatores macroeconômicos (juros e desemprego) influenciam a inadimplência?
É possível antecipar movimentos de alta no risco de crédito?

📂 Estrutura do Projeto

📁 data/
    ├── raw/
    └── processed/

📁 notebooks/
    ├── 01_coleta_dados.ipynb
    ├── 02_tratamento_dados.ipynb
    ├── 03_analise_exploratoria.ipynb
    ├── 04_modelagem_preditiva.ipynb

📁 outputs/
    ├── graficos/
    └── metricas/

README.md
requirements.txt

🔎 Etapas do Projeto
1️⃣ Coleta de Dados

Taxa de inadimplência

Taxa de juros

Taxa de desemprego

Série temporal organizada por período

2️⃣ Tratamento e Preparação

Conversão e padronização de datas

Tratamento de valores ausentes

Organização temporal

Engenharia básica de variáveis

3️⃣ Análise Exploratória (EDA)

Principais análises:

Evolução histórica da inadimplência

Correlação entre desemprego e inadimplência

Correlação entre juros e inadimplência

Identificação de tendências e ciclos

📌 Insight principal:
O desemprego apresenta forte relação positiva com a inadimplência, enquanto a taxa de juros demonstra impacto com possível efeito defasado.

4️⃣ Modelagem Preditiva

Foi aplicada modelagem respeitando a ordem temporal dos dados.

Boas práticas utilizadas:

Separação treino/teste cronológica

Avaliação por métricas de erro

Comparação entre valores reais e previstos

Objetivo do modelo:
Antecipar movimentos de alta no risco de crédito.

📊 Resultados Estratégicos

✔ O modelo conseguiu capturar tendência de crescimento da inadimplência
✔ Variáveis macroeconômicas demonstraram poder explicativo relevante
✔ O projeto simula aplicação prática em contexto de fintech

🛠️ Stack Tecnológica

Python

Pandas

NumPy

Matplotlib

Scikit-Learn

💼 Aplicação no Mundo Real

Em um cenário real de fintech, essa análise pode ser usada para:

Ajuste de score de crédito

Definição de política de concessão

Aumento ou redução de limites

Ajuste de taxa de juros por perfil de risco

🚀 Próximas Evoluções

Implementação de modelo de classificação (inadimplente vs adimplente)

Regressão Logística

Random Forest

Avaliação com ROC-AUC e Recall

Construção de dashboard executivo

👤 Autor

Victor Hugo Miranda Crispim
Bacharel em Análise de Dados
Experiência em Crédito B2B e B2C
Foco em análise de risco e tomada de decisão baseada em dados

📌 Diferencial do Projeto

Este projeto une:

📊 Análise estatística

🤖 Modelagem preditiva

🏦 Visão de negócio em crédito

📈 Interpretação estratégica dos dados

