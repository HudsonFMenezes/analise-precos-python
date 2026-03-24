# Análise de Preços de Produtos

## Objetivo

Este projeto tem como objetivo analisar a variação de preços de produtos ao longo do tempo, identificar tendências, comparar lojas e avaliar oportunidades de compra com base em dados históricos.

---

## Estrutura do Projeto

```
analise-precos-python/
│
├── data/
│   ├── raw/           # Dados brutos
│   ├── processed/     # Dados tratados
│   └── analysis/      # Dados agregados para análise
│
├── src/
│   ├── limpeza.py
│   ├── analise.py
│   └── visualizacao.py
│
├── img/               # Gráficos gerados
└── README.md
```

---

## Etapas do Projeto

### 1. Limpeza de Dados

* Preenchimento de preços vazios pela média de produtos iguais
* Configuração de datas
* Mudança no padrão de exibição de lojas
* Substituição da avaliação
* Manutenção na coluna de desconto

### 2. Análise Exploratória

* Preço médio por produto
* Preço médio por categoria
* Variação de preço entre os produtos
* Vendas por loja

### 3. Análise Temporal

* Evoluçao de preços
* Tendências (Queda ou Aumento)
* Comparação entre lojas

### 4. Análise por Loja

* Qual loja com menor média de preço
* Qual loja oferta mais desconto
* Relação entre avaliação e preço de uma loja
* Regras de recomendacao
* Oportunidade de desconto
* Avaliações ruins (<4.4)

### 5. Visualização de Dados

* Gráficos para interpretação dos padrões
* Comparações entre produtos e lojas
* Identificação visual de tendências

---

## Visualizações

### Evolução de preços ao longo do tempo

Mostra como os preços variam ao longo do tempo para cada produto.

![Evolução de preços](img/evolucao_precos.png)

**Insight:**

* Notebooks apresentam maior variação de preço
* Tendência geral de queda até março, com leve recuperação posterior

---

### Preço médio por produto

Comparação direta entre os preços médios.

![Preço médio por produto](img/media_produtos.png)

**Insight:**

* Notebook é o produto mais caro
* Mouse apresenta menor custo médio
* Monitor ocupa posição intermediária

---

### Preço médio por loja

Comparação de preços entre lojas.

![Preço médio por loja](img/media_loja.png)

**Insight:**

* Diferença significativa de preços entre lojas
* Algumas lojas apresentam vantagem competitiva em determinados produtos

---

### Avaliação vs Preço

Relação entre qualidade percebida e preço.

![Avaliação vs preço](img/relacao_avaliacao_preco.png)

**Insight:**

* Não há correlação direta forte entre preço e avaliação
* Produtos mais caros nem sempre são melhor avaliados

---

## Principais Insights

* Produtos apresentam comportamentos distintos de preço ao longo do tempo
* Notebooks possuem maior volatilidade
* Algumas lojas oferecem melhores preços de forma consistente
* Avaliação do produto não está diretamente ligada ao preço
* É possível identificar oportunidades de compra comparando preço atual com histórico

---

## Tecnologias Utilizadas

* Python
* Pandas
* Matplotlib

---

## Habilidades Desenvolvidas

* Limpeza e tratamento de dados reais
* Manipulação de dados com Pandas
* Análise exploratória de dados (EDA)
* Criação de métricas e indicadores
* Visualização de dados
* Estruturação de pipeline de dados

---

## Conclusão

Este projeto demonstra a aplicação prática de técnicas de análise de dados para extração de insights relevantes, permitindo identificar padrões, tendências e oportunidades de decisão baseadas em dados.

---

## Possíveis melhorias

* Implementação de dashboard interativo
* Uso de bibliotecas como Seaborn ou Plotly
* Aplicação de modelos de previsão de preços
* Integração com APIs para coleta de dados em tempo real

---
