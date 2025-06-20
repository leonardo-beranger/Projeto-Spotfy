# Bibliotecas utilizadas
import pandas as pd
import numpy as np
import os
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Obtém o diretório de trabalho atual
current_dir = os.getcwd()

# Constrói o caminho completo para o arquivo CSV
csv_path1 = os.path.join(current_dir, 'base_de_dados', 'Spotify.csv')

# Ignora todas as mensagens de aviso
warnings.filterwarnings("ignore")

df = pd.read_csv(csv_path1, delimiter=',', encoding='latin1')

# Substituir valores nulos
df["key"] = df["key"].fillna("unknown")
df["in_shazam_charts"] = df["in_shazam_charts"].fillna(0)

# Converter colunas numéricas para float
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].astype(float)

# Converter colunas categóricas para string
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
df[categorical_cols] = df[categorical_cols].astype(str)

# Selecionar as colunas que serão usadas no clustering
features = ["bpm", "danceability_%", "energy_%", "valence_%", "liveness_%", "speechiness_%"]

# Remover linhas com valores ausentes nas colunas selecionadas
df_cluster = df[features].dropna()

# Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_cluster)

# Exibir as primeiras 5 linhas normalizadas como DataFrame
df_scaled = pd.DataFrame(X_scaled, columns=features)

n_clusters = 4  # Clusters definidos pela unidade de negócio

# Aplicando KMeans
kmeans_final = KMeans(n_clusters=n_clusters, random_state=42)
df_scaled["cluster"] = kmeans_final.fit_predict(X_scaled)

# Juntar com colunas originais para visualizar nomes de faixas e artistas
df_with_clusters = df.loc[df_scaled.index].copy()
df_with_clusters["cluster"] = df_scaled["cluster"].values

sample_clusters = df_with_clusters[["track_name", "artist(s)_name", "cluster"]].sort_values("cluster").reset_index(drop=True)

# Acrescentar coluna com categorias de playlists
cat = []

for i in df_with_clusters["cluster"]:
    if i == 0:
        cat.append("Trilha das Estrelas")
    elif i == 1:
        cat.append("Calmamente Pop")
    elif i == 2:
        cat.append("Entre razões e emoções")
    else:
        cat.append("Flow Pesadão")

df_with_clusters["playlist_category"] = cat

save_cam = os.path.join(current_dir, 'base_de_dados', 'Spotify clusters.xlsx')

df_with_clusters.reset_index(drop=True)

try:
    df_with_clusters.to_excel(save_cam, index=False, engine='openpyxl')
    print(f"Arquivo salvo em: {save_cam}")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")
