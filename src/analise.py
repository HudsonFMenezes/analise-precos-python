import pandas as pd
import os

# Buscando os dados
base_dir = os.path.dirname(__file__)
# Função genérica para salvar/buscar arquivos
def file_path (dir_name, file_name):
    return os.path.join(base_dir, "..", "data", dir_name, file_name)
df = pd.read_csv(file_path("processed", "produtos_tratados.csv"))

# Função especializada para salvar aquivos
def save_file(content ,file_name):
    return content.to_csv(file_path("analysis", file_name), index=False)

# Análise exploratória:
# Preço médio por produto
media_produtos = df.groupby("produto")["preco"].mean().reset_index().round(2)
media_produtos = media_produtos.sort_values(by="preco", ascending=False)

save_file(media_produtos, "media_produtos.csv")

# Preço médio por categoria
media_categorias = df.groupby("categoria")["preco"].mean().reset_index().round(2)
media_categorias = media_categorias.sort_values(by="preco",ascending=False)
media_categorias

save_file(media_categorias, "media_categorias.csv")

# Variação de preço entre os produtos
variacao = df.groupby('produto')['preco'].agg(['min', 'max']).reset_index()

variacao['variacao'] = variacao['max'] - variacao['min']
variacao['variacao_percentual'] = ((variacao['max'] - variacao['min']) / variacao['min']).round(2)
variacao = variacao.sort_values(by='variacao', ascending=False)

save_file(variacao, "variacao.csv")

# Vendas por loja
vendas_loja = df.groupby("loja")["preco"].sum().reset_index()
vendas_loja = vendas_loja.sort_values(by="preco", ascending=False)

save_file(vendas_loja, "vendas_loja.csv")

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
tendencias["direcao"] = tendencias["tendencias"].apply(lambda x: "alta" if x > 0 else "queda")

save_file(tendencias, "tendencias.csv")

# Comparação entre lojas
comparacao = df.groupby(["data", "loja"])["preco"].sum().reset_index().round(2)

save_file(comparacao, "comparacao.csv")

# Análise por loja
# Qual loja com menor média de preço
media_loja = df.groupby("loja")["preco"].mean().round(2)
media_loja = media_loja.reset_index().sort_values(by="preco",ascending=True)

save_file(media_loja, "media_loja.csv")

# Qual loja oferta mais desconto
desconto_loja = df.groupby("loja")["desconto"].mean().round(2)
desconto_loja = desconto_loja.reset_index().sort_values(by="desconto", ascending=False)

save_file(desconto_loja, "desconto_loja.csv")

# Relação entre avaliação e preço de uma loja
relacao_avaliacao_preco = pd.DataFrame()
relacao_avaliacao_preco["preco"] = df.groupby("loja")["preco"].mean().round(2)
relacao_avaliacao_preco["avaliacao"] = df.groupby("loja")["avaliacao"].mean().round(2)
relacao_avaliacao_preco = relacao_avaliacao_preco.reset_index()
relacao_avaliacao_preco["relacao"] = (relacao_avaliacao_preco["preco"] / relacao_avaliacao_preco["avaliacao"]).round(2)
relacao_avaliacao_preco = relacao_avaliacao_preco.sort_values(by="relacao", ascending=True)

save_file(relacao_avaliacao_preco, "relacao_avaliacao_preco.csv")

# Regras de recomendacao
recomendacao = pd.DataFrame()
recomendacao["preco_medio"] = df.groupby("produto")["preco"].mean().round(2)
recomendacao["preco_atual"] = df.sort_values(by="data",ascending=True).groupby("produto").last()["preco"]
recomendacao["recomendacao"] = recomendacao.apply(lambda x: "Comprar" if x["preco_atual"] < x["preco_medio"] else "Não Comprar", axis=1)
recomendacao = recomendacao.reset_index()

save_file(recomendacao, "recomendacao.csv")

# Oportunidade de desconto
oportunidade = pd.DataFrame()
oportunidade["desconto_medio"] = df.groupby("produto")["desconto"].mean().round(2)
oportunidade["desconto_atual"] = df.sort_values(by="data",ascending=True).groupby("produto").last()["desconto"]
oportunidade["oportunidade"] = oportunidade.apply(lambda x: "Boa" if x["desconto_atual"] > x["desconto_medio"] else "Ruim", axis=1)
oportunidade = oportunidade.reset_index()

save_file(oportunidade, "oportunidade.csv")

# Avaliações ruins (<4.4)
avaliacoes = pd.DataFrame()
avaliacoes["avaliacao_media"] = df.groupby("produto")["avaliacao"].mean().round(2)
avaliacoes["avaliacao"] = avaliacoes.apply(lambda x: "Boa" if x["avaliacao_media"] > 4.4 else "Ruim", axis=1)
avaliacoes = avaliacoes.reset_index()

save_file(avaliacoes, "avaliacoes.csv")

