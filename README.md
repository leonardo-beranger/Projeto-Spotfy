# Projeto Spotify - Clusterização de Músicas

Este repositório apresenta um estudo de clustering em faixas musicais extraídas do Spotify. O objetivo é sugerir novas playlists para a empresa **MozartBee**, um aplicativo de streaming musical que busca concorrer com o Spotify.

![Logo](visuais/logo.png)

## Visão geral

O projeto utiliza um conjunto de dados contendo informações de 953 músicas populares do Spotify. A partir das características de cada faixa (BPM, energia, dançabilidade, etc.) é aplicado o algoritmo **K-Means** para agrupar canções semelhantes. Cada cluster recebeu um nome representando uma possível categoria de playlist.

As etapas principais do projeto estão documentadas na pasta `scripts` e ilustradas na apresentação em PDF.

## Estrutura do repositório

```
├── base_de_dados
│   ├── Spotify.csv              # Base original com 953 registros
│   └── Spotify clusters.xlsx    # Resultado gerado após a clusterização
├── scripts
│   ├── Desenv_Projeto.ipynb     # Notebook de desenvolvimento
│   └── modelo_consolidado.py    # Script principal para gerar os clusters
├── visuais
│   ├── logo.png                 # Logo do projeto
│   ├── capa.jpg                 # Imagem de capa
│   ├── describe.png             # Exemplo de análise descritiva
│   ├── partners.png             # Parcerias
│   └── process.png              # Fluxo de processo
└── Apresentação.pdf            # Slides resumindo o projeto
```

## Dependências

Para reproduzir a análise é necessário ter Python 3.8+ e as bibliotecas abaixo instaladas:

- `pandas`
- `numpy`
- `scikit-learn`
- `openpyxl`

Você pode instalá-las com:

```bash
pip install pandas numpy scikit-learn openpyxl
```

## Como executar

1. Certifique-se de que o arquivo `base_de_dados/Spotify.csv` está no diretório atual.
2. Execute o script de clusterização:

```bash
python scripts/modelo_consolidado.py
```

O script irá ler o CSV, aplicar o K-Means com quatro clusters e salvar o resultado em `base_de_dados/Spotify clusters.xlsx`. Cada registro receberá a coluna `playlist_category` indicando a qual grupo pertence.

## Resultados

As categorias definidas após a análise foram:

- **Trilha das Estrelas** (cluster 0)
- **Calmamente Pop** (cluster 1)
- **Entre razões e emoções** (cluster 2)
- **Flow Pesadão** (cluster 3)


Consulte o arquivo `Apresentação.pdf` para detalhes completos da metodologia utilizada.
