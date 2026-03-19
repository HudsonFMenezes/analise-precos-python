import pandas as pd
import os

# Buscando os dados
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "data", "processed", "produtos_tratados.csv")
df = pd.read_csv(file_path)

# Análise exploratória:
# Preço médio por produto
media_produtos = df.groupby("produto")["preco"].mean().reset_index().round(2)
media_produtos = media_produtos.sort_values(by="preco", ascending=False)

save_file_path = os.path.join(base_dir, "..", "data", "analysis", "media_produtos.csv")
media_produtos.to_csv(save_file_path, index=False)

# Preço médio por categoria
media_categorias = df.groupby("categoria")["preco"].mean().reset_index().round(2)
media_categorias = media_categorias.sort_values(by="preco",ascending=False)
media_categorias

save_file_path = os.path.join(base_dir, "..", "data", "analysis", "media_categorias.csv")
media_categorias.to_csv(save_file_path,index=False)

# Variação de preço entre os produtos
variacao = df.groupby('produto')['preco'].agg(['min', 'max']).reset_index()

variacao['variacao'] = variacao['max'] - variacao['min']
variacao['variacao_percentual'] = ((variacao['max'] - variacao['min']) / variacao['min']).round(2)

variacao = variacao.sort_values(by='variacao', ascending=False)

save_file_path = os.path.join(base_dir, "..", "data", "analysis", "variacao_produtos.csv")
variacao.to_csv(save_file_path, index=False)

# Vendas por loja
vendas_loja = df.groupby("loja")["preco"].sum().reset_index()
vendas_loja = vendas_loja.sort_values(by="preco", ascending=False)

save_file_path = os.path.join(base_dir, "..", "data", "analysis", "vendas_loja.csv")
vendas_loja.to_csv(save_file_path, index=False)

# TODO: Análise temporal
