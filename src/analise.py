import pandas as pd
import os

# Buscando os dados
base_dir = os.path.dirname(__file__)
# Função para salvar/buscar arquivos
def file_path (dir_name, file_name):
    return os.path.join(base_dir, "..", "data", dir_name, file_name)
df = pd.read_csv(file_path("processed", "produtos_tratados.csv"))

# Análise exploratória:
# Preço médio por produto
media_produtos = df.groupby("produto")["preco"].mean().reset_index().round(2)
media_produtos = media_produtos.sort_values(by="preco", ascending=False)

media_produtos.to_csv(file_path("analysis", "media_produtos.csv"), index=False)

# Preço médio por categoria
media_categorias = df.groupby("categoria")["preco"].mean().reset_index().round(2)
media_categorias = media_categorias.sort_values(by="preco",ascending=False)
media_categorias

media_categorias.to_csv(file_path("analysis", "media_categorias.csv"),index=False)

# Variação de preço entre os produtos
variacao = df.groupby('produto')['preco'].agg(['min', 'max']).reset_index()

variacao['variacao'] = variacao['max'] - variacao['min']
variacao['variacao_percentual'] = ((variacao['max'] - variacao['min']) / variacao['min']).round(2)
variacao = variacao.sort_values(by='variacao', ascending=False)

variacao.to_csv(file_path("analysis", "variacao_produtos.csv"), index=False)

# Vendas por loja
vendas_loja = df.groupby("loja")["preco"].sum().reset_index()
vendas_loja = vendas_loja.sort_values(by="preco", ascending=False)

vendas_loja.to_csv(file_path("analysis", "vendas_loja.csv"), index=False)

# Análise temporal
# Evoluçao de preços
df["data"] = pd.to_datetime(df["data"], errors="coerce")
evolucao = df.groupby(["data", "produto"])["preco"].mean()
evolucao = evolucao.reset_index().sort_values(by="data").round(2)

evolucao.to_csv(file_path("analysis", "evolucao_precos.csv"), index=False)

# Tendências (Queda ou Aumento)
tendencias = df.sort_values(by="data").groupby("produto")["preco"].agg(["first", "last"])
tendencias["tendencias"] = tendencias["last"] - tendencias["first"]
tendencias["tendencias"] = tendencias["tendencias"].round(2)
tendencias["direcao"] = tendencias["tendencias"].apply(
    lambda x: "alta" if x > 0 else "queda"
)

tendencias.to_csv(file_path("analysis", "tendencias_precos.csv"))

# Comparação entre lojas
comparacao = df.groupby(["data", "loja"])["preco"].sum().reset_index().round(2)

comparacao.to_csv(file_path("analysis", "comparacao_lojas.csv"))

