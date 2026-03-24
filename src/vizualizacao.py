import pandas as pd
import os
import matplotlib.pyplot as plt

# Buscando os dados
base_dir = os.path.dirname(__file__)
# Função genérica para salvar/buscar arquivos
def file_path (dir_name, file_name):
    return os.path.join(base_dir, "..", "data", dir_name, file_name)

# Função especializada para salvar aquivos
def save_file(file_name):
    return plt.savefig(file_path("img", file_name))

# Evolução de preços por produto
def plot_evolucao():
    df = pd.read_csv(file_path("analysis", "evolucao_precos.csv"))
    for produto in df["produto"].unique():
        dados = df[df["produto"] == produto]
        plt.plot(dados["data"], dados["preco"], label=produto)

    plt.legend()
    plt.title("Evolucao de preços por produto")
    plt.xlabel("data")
    plt.ylabel("Preço")
    plt.xticks(rotation=45)
    plt.savefig(file_path("img", "evolucao_precos.png"), bbox_inches="tight")
    plt.close()
    
# Média dos produtos
def plot_media_produtos():
    df = pd.read_csv(file_path("analysis", "media_produtos.csv"))

    plt.bar(df["produto"], df["preco"])
    plt.title("Preço médio por produto")
    plt.xlabel("Produto")
    plt.ylabel("Preço")
    plt.savefig(file_path("img", "media_produtos.png.png"), bbox_inches="tight")
    plt.close()

# Variação de preço por produto
def plot_variacao():
    df = pd.read_csv(file_path("analysis", "variacao.csv"))

    plt.bar(df["produto"], df["variacao"])
    plt.title("Variação de preço por produto")
    plt.ylabel("Variação")
    plt.savefig(file_path("img", "variacao.png"), bbox_inches="tight")
    plt.close()

# Preço médio por loja
def plot_lojas():
    df = pd.read_csv(file_path("analysis", "media_loja.csv"))

    plt.bar(df["loja"], df["preco"])
    plt.title("Preço médio por loja")
    plt.ylabel("Preço")
    plt.savefig(file_path("img", "media_loja.png"), bbox_inches="tight")
    plt.close()

# Avaliação vs preço
def plot_avaliacao_preco():
    df = pd.read_csv(file_path("analysis", "relacao_avaliacao_preco.csv"))

    plt.scatter(df["avaliacao"], df["preco"])
    plt.title("Avaliação vs Preço")
    plt.xlabel("Avaliação")
    plt.ylabel("Preço")
    plt.savefig(file_path("img", "relacao_avaliacao_preco.png"))
    plt.close()
    
plot_evolucao()
plot_media_produtos()
plot_variacao()
plot_lojas()
plot_avaliacao_preco()