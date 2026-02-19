# 📊 Análise e Previsão de Inadimplência

### Projeto de Data Science aplicado a **Risco de Crédito em Fintech**

---

## 🎯 Visão Executiva

Este projeto simula um cenário real de uma **fintech de crédito** que precisa antecipar movimentos de deterioração da carteira.

O objetivo é transformar **dados macroeconômicos** em **insights estratégicos acionáveis**, permitindo decisões como:

* Ajuste de políticas de concessão
* Revisão de limites de crédito
* Reprecificação de taxas
* Reforço de provisionamento

A proposta vai além da análise técnica — o foco está em **impacto no negócio**.

---

## 🧠 Problema de Negócio

Instituições financeiras operam sob risco constante de inadimplência.
Movimentos macroeconômicos, como aumento do desemprego ou da taxa de juros, podem afetar diretamente a qualidade da carteira.

**Pergunta central:**

> É possível antecipar movimentos de alta na inadimplência utilizando variáveis macroeconômicas?

---

## 📂 Estrutura do Projeto

```
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
```

---

## 🔎 Abordagem Analítica

### 1️⃣ Coleta de Dados

* Taxa de inadimplência
* Taxa de juros
* Taxa de desemprego
* Série temporal estruturada por período

---

### 2️⃣ Tratamento e Engenharia de Dados

* Padronização temporal
* Tratamento de valores ausentes
* Organização cronológica
* Criação de variáveis explicativas

Aplicação de boas práticas para manter consistência e evitar vazamento de dados.

---

### 3️⃣ Análise Exploratória (EDA)

Principais análises realizadas:

* Evolução histórica da inadimplência
* Correlação entre desemprego e inadimplência
* Impacto da taxa de juros
* Identificação de tendências e ciclos

📌 **Insight Estratégico:**
O desemprego apresenta forte relação positiva com a inadimplência, enquanto juros indicam possível impacto com efeito defasado.

Isso reforça a importância de monitoramento macroeconômico na gestão de risco.

---

### 4️⃣ Modelagem Preditiva

Modelo desenvolvido respeitando a ordem temporal dos dados.

Boas práticas aplicadas:

* Separação treino/teste cronológica
* Avaliação por métricas de erro
* Comparação entre valores reais e previstos

🎯 **Objetivo:**
Antecipar movimentos de alta no risco de crédito para suportar decisões estratégicas.

---

## 📊 Resultados Relevantes

✔ Captura consistente da tendência de crescimento da inadimplência
✔ Evidência de poder explicativo das variáveis macroeconômicas
✔ Aplicabilidade direta em contexto de fintech

O projeto demonstra como transformar variáveis econômicas em sinal preditivo para gestão de risco.

---

## 🛠 Stack Tecnológica

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn

---

## 💼 Aplicação em Ambiente Real

Em uma fintech ou banco digital, este modelo pode apoiar:

* Ajuste de score de crédito
* Segmentação de clientes por risco
* Revisão de política de concessão
* Definição de limites
* Estratégia de precificação

---

## 🚀 Próximos Passos (Roadmap Técnico)

* Implementação de modelo de classificação (inadimplente vs adimplente)
* Regressão Logística
* Random Forest
* Avaliação com ROC-AUC e Recall
* Backtesting de performance
* Construção de dashboard executivo

---

## 👤 Autor

**Victor Hugo Miranda Crispim**

* Bacharel em Análise de Dados

* Experiência em Crédito B2B e B2C

* Foco em análise de risco e tomada de decisão baseada em dados

---

## ⭐ Diferencial

Este projeto integra:

* Análise estatística
* Modelagem preditiva
* Visão estratégica de crédito
* Interpretação orientada a negócio

Mais do que um exercício técnico, é uma simulação prática de gestão de risco em fintech.

