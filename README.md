# 🏢 Corporate Risk & Performance Assistant

📊 Projeto de análise de risco e performance corporativa focado em inadimplência, receita e segmentação de clientes.

## 🔹 Visão Geral

Este projeto ajuda empresas a entender o risco de seus clientes e tomar decisões estratégicas com base em dados.
Funcionalidades principais:

* 📥 Carregamento e tratamento de dados

* 📊 Cálculo de KPIs e indicadores estratégicos

* 🚨 Score e classificação de risco de clientes

* 📈 Visualizações interativas

* 💾 Exportação de relatórios

O dataset possui as seguintes colunas:

Coluna	                 Descrição
cliente_id	            Identificador único do cliente
receita	                Receita anual/mensal do cliente 💰
risco	                Classificação de risco (baixo, médio, alto) ⚠️
segmento	            Segmento do cliente (corporativo, PME, enterprise) 🏷️
tempo_contrato_meses	  Duração do contrato em meses ⏳
inadimplente	          Indicador de inadimplência (0 = não, 1 = sim) ❌

Exemplo de dados:

cliente_id,receita,risco,segmento,tempo_contrato_meses,inadimplente
1,10000,baixo,corporativo,24,0
2,20000,medio,corporativo,36,0
3,,alto,pm e,12,1
...
20,7000,alto,pm e,9,1

## 🔹 Estrutura do Projeto
project-root/
│
├── data/

│   └── sample_data.csv           # 📄 Dados de clientes

│

├── src/

│   ├── data_loader.py            # 🧹 Carregamento e limpeza de dados

│   ├── performance_analyzer.py   # 📊 KPIs e insights estratégicos

│   ├── risk_scoring.py           # 🚨 Score e classificação de risco

│   └── visualizer.py             # 📈 Visualizações (receita, score, etc.)

│

├── main.py                       # ▶️ Script principal

└── README.md

# 🔹 Funcionalidades
## 1️⃣ Carregamento e Tratamento de Dados

🔍 Validação da estrutura e consistência

🧹 Tratamento de valores nulos

## 2️⃣ Análise de Performance

📊 KPIs executivos: receita total, média, inadimplência, tempo médio de contrato

💹 Receita média por segmento

🧠 Insights estratégicos automáticos

3️⃣ Risk Scoring

⚖️ Cálculo de score individual baseado em regras de negócio:

💰 Receita (quanto menor, maior o risco)

⏳ Tempo de contrato (contratos curtos = mais risco)

⚠️ Classificação declarada de risco

🚦 Classificação: ALTO RISCO, RISCO MÉDIO, BAIXO RISCO

🔝 Top 5 clientes mais arriscados

4️⃣ Visualizações

📊 Receita por segmento (gráfico de barras)

📉 Distribuição de score de risco (histograma com KDE)

5️⃣ Exportação

💾 Relatório final com score de risco:

data/clientes_scored.csv

🔹 Como Executar

Instale dependências:

pip install pandas matplotlib seaborn


Execute o script principal:

python main.py


Confira os resultados:

📈 KPIs e insights no console

💾 Arquivo clientes_scored.csv em data/

📊 Gráficos interativos exibidos

🔹 Insights Estratégicos Exemplo

⚠️ Taxa de inadimplência acima de 20%

📉 Segmento PME apresenta maior risco de inadimplência

💰 Receita média saudável acima de 20k

🔹 Tecnologias

🐍 Python 3.10+

📊 Pandas

📈 Matplotlib

🎨 Seaborn

🔹 Contribuição

Projeto open-source para análise de risco corporativo.
Você pode:

🔄 Testar com outros datasets

⚙️ Ajustar regras de scoring

📊 Expandir KPIs e visualizações

🔹 Autor
* Victor Hugo Miranda Crispim

* Bacharel em Análise de Dados

* Experiência em Crédito B2B e B2C

