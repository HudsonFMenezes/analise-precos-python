import pandas as pd
import os

# Buscando os dados
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "data", "raw", "produtos.csv")
df = pd.read_csv(file_path)

# Preenchimento de preços vazios pela média de produtos iguais
df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
media_produtos = df.groupby("produto")["preco"].transform("mean").round(2)
df["preco"] = df["preco"].fillna(media_produtos)

# Configuração de datas
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df["data"] = df["data"].dt.strftime("%d/%m/%Y")

# Mudança no padrão de exibição de lojas
df["loja"] = df["loja"].str.replace("Loja ", "", regex=False)

# Substituição da avaliação
df["avaliacao"] = df["avaliacao"].replace({
    "quatro": 4.0
})
df["avaliacao"] = pd.to_numeric(df["avaliacao"], errors="coerce")

# Manutenção na coluna de desconto
df["desconto"] = df["desconto"].astype(str).str.replace("%","",regex=False)
df["desconto"] = pd.to_numeric(df["desconto"],errors="coerce")

media_descontos = df.groupby("produto")["desconto"].transform("mean").round(1)
df["desconto"] = df["desconto"].fillna(media_descontos)
df["desconto"] = df["desconto"]/100
df["desconto"] = df["desconto"].round(2)

# Salvando os dados
save_file_path = os.path.join(base_dir, "..", "data", "processed", "produtos_tratados.csv")
df.to_csv(save_file_path, index=False)
