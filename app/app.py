# ==========================================================
# APP STREAMLIT - PREVISÃO DE PREÇO DE IMÓVEIS
# MODELO RANDOM FOREST
# ==========================================================

import streamlit as st
import pandas as pd
from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="Previsão de Preços de Imóveis",
    page_icon="🏠",
    layout="centered"
)

# ==========================================================
# ESTILO DA PÁGINA
# ==========================================================

st.markdown(
    """
    <style>
    .titulo {
        text-align: center;
        color: #1f4e79;
        font-size: 38px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitulo {
        text-align: center;
        color: #555555;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .caixa-info {
        background-color: #f1f6fb;
        padding: 18px;
        border-left: 5px solid #1f4e79;
        border-radius: 8px;
        margin-bottom: 25px;
        font-size: 16px;
    }

    .card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0px 3px 14px rgba(0,0,0,0.12);
        margin-top: 22px;
        margin-bottom: 25px;
        border-top: 5px solid #1f4e79;
    }

    .resultado {
        text-align: center;
        font-size: 42px;
        color: #1f4e79;
        font-weight: bold;
    }

    .texto-card {
        text-align: center;
        font-size: 20px;
        color: #555555;
        margin-bottom: 8px;
    }

    .rodape {
        text-align: center;
        color: #666666;
        font-size: 14px;
        margin-top: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# BARRA LATERAL
# ==========================================================

st.sidebar.title("🏠 Consultoria Imobiliária")

st.sidebar.info(
    """
    **Projeto:** Consultoria Estatística  
    **Modelo:** Random Forest  
    **Base:** House Prices - Kaggle  
    **Instituição:** UEPB
    """
)

st.sidebar.markdown("---")

st.sidebar.write(
    """
    Este aplicativo estima o preço de venda de imóveis com base em
    características estruturais informadas pelo usuário.
    """
)

# ==========================================================
# CABEÇALHO
# ==========================================================

st.markdown(
    """
    <div class="titulo">🏠 Sistema de Previsão de Preços de Imóveis</div>
    <div class="subtitulo">
    Produto de dados desenvolvido com o modelo Random Forest
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="caixa-info">
    <b>Como utilizar:</b><br>
    1. Informe as características estruturais do imóvel.<br>
    2. Confira o resumo do imóvel informado.<br>
    3. Clique no botão <b>Estimar preço do imóvel</b>.<br>
    4. O sistema exibirá uma estimativa do preço de venda com base no modelo preditivo.
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# CARREGAMENTO DOS DADOS
# ==========================================================

@st.cache_data
def carregar_dados():
    caminho = Path(__file__).resolve().parents[1] / "dados" / "train.csv"
    return pd.read_csv(caminho)

dados = carregar_dados()

# ==========================================================
# PREPARAÇÃO DOS DADOS
# ==========================================================

@st.cache_data
def preparar_dados(dados):
    modelo = dados[
        [
            "SalePrice",
            "GrLivArea",
            "OverallQual",
            "GarageCars",
            "BedroomAbvGr",
            "LotArea",
            "YearBuilt",
            "FullBath"
        ]
    ].copy()

    return modelo

modelo = preparar_dados(dados)

# ==========================================================
# AJUSTE E AVALIAÇÃO DO MODELO RANDOM FOREST
# ==========================================================

@st.cache_resource
def ajustar_modelo(modelo):

    # Variáveis explicativas
    X = modelo[
        [
            "GrLivArea",
            "OverallQual",
            "GarageCars",
            "BedroomAbvGr",
            "LotArea",
            "YearBuilt",
            "FullBath"
        ]
    ]

    # Variável resposta
    y = modelo["SalePrice"]

    # Divisão da base em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # Modelo utilizado na validação preditiva
    modelo_validacao = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    modelo_validacao.fit(X_train, y_train)

    # Previsões na base de teste
    y_pred_test = modelo_validacao.predict(X_test)

    # Métricas de desempenho na base de teste
    rmse = mean_squared_error(y_test, y_pred_test) ** 0.5
    mae = mean_absolute_error(y_test, y_pred_test)
    r2 = r2_score(y_test, y_pred_test)

    # Modelo final ajustado com toda a base
    modelo_rf_final = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    modelo_rf_final.fit(X, y)

    return modelo_rf_final, rmse, mae, r2


modelo_rf_final, rmse, mae, r2 = ajustar_modelo(modelo)

# ==========================================================
# FORMULÁRIO
# ==========================================================

st.subheader("📋 Características do imóvel")

st.write(
    """
    Preencha os campos abaixo com as informações do imóvel que será avaliado.
    """
)

GrLivArea = st.number_input(
    "📐 Área construída do imóvel (pés²)",
    min_value=300,
    max_value=6000,
    value=1800,
    step=50,
    help="Área construída acima do nível do solo, medida em pés quadrados na base original."
)

OverallQual = st.slider(
    "⭐ Qualidade geral do imóvel",
    min_value=1,
    max_value=10,
    value=8,
    help="Nota de qualidade geral da construção e do acabamento, variando de 1 a 10."
)

GarageCars = st.number_input(
    "🚗 Número de vagas na garagem",
    min_value=0,
    max_value=5,
    value=2,
    step=1,
    help="Quantidade de carros que cabem na garagem."
)

BedroomAbvGr = st.number_input(
    "🛏 Número de quartos",
    min_value=0,
    max_value=10,
    value=3,
    step=1,
    help="Quantidade de quartos acima do nível do solo."
)

LotArea = st.number_input(
    "🌳 Área total do terreno (pés²)",
    min_value=1000,
    max_value=50000,
    value=9000,
    step=500,
    help="Área total do terreno, medida em pés quadrados na base original."
)

YearBuilt = st.number_input(
    "🏗 Ano de construção",
    min_value=1870,
    max_value=2026,
    value=2015,
    step=1,
    help="Ano em que o imóvel foi construído."
)

FullBath = st.number_input(
    "🚿 Número de banheiros completos",
    min_value=0,
    max_value=5,
    value=2,
    step=1,
    help="Quantidade de banheiros completos no imóvel."
)

# ==========================================================
# RESUMO DO IMÓVEL
# ==========================================================

st.markdown("---")

st.subheader("📌 Resumo do imóvel informado")

resumo = pd.DataFrame({
    "Característica": [
        "Área construída (pés²)",
        "Qualidade geral",
        "Vagas na garagem",
        "Número de quartos",
        "Área do terreno (pés²)",
        "Ano de construção",
        "Banheiros completos"
    ],
    "Valor informado": [
        GrLivArea,
        OverallQual,
        GarageCars,
        BedroomAbvGr,
        LotArea,
        YearBuilt,
        FullBath
    ]
})

st.dataframe(
    resumo,
    width="stretch",
    hide_index=True
)

# ==========================================================
# PREVISÃO
# ==========================================================

novo_imovel = pd.DataFrame({
    "GrLivArea": [GrLivArea],
    "OverallQual": [OverallQual],
    "GarageCars": [GarageCars],
    "BedroomAbvGr": [BedroomAbvGr],
    "LotArea": [LotArea],
    "YearBuilt": [YearBuilt],
    "FullBath": [FullBath]
})

st.markdown("---")

if st.button(
    "🔎 Estimar preço do imóvel",
    width="stretch"
):
    preco_previsto = modelo_rf_final.predict(novo_imovel)[0]

    valor = f"{preco_previsto:,.2f}"
    valor = valor.replace(",", "X").replace(".", ",").replace("X", ".")

    st.markdown(
        f"""
        <div class="card">
            <p class="texto-card">💰 Preço estimado de venda</p>
            <div class="resultado">US$ {valor}</div>
            <p class="texto-card">
            Estimativa gerada pelo modelo Random Forest
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(
        "Estimativa concluída com sucesso. O valor apresentado corresponde ao preço de venda estimado "
        "em dólares americanos (USD), conforme a base de dados utilizada."
    )

# ==========================================================
# MÉTRICAS DO MODELO
# ==========================================================

st.markdown("---")

st.subheader("📊 Desempenho do modelo na base de teste")

col_m1, col_m2, col_m3 = st.columns(3)

with col_m1:
    st.metric(
        "RMSE",
        f"{rmse:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col_m2:
    st.metric(
        "MAE",
        f"{mae:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col_m3:
    st.metric(
        "R²",
        f"{r2:.4f}".replace(".", ",")
    )

st.caption(
    "As métricas foram calculadas no conjunto de teste, composto por 20% das observações "
    "e não utilizado no treinamento do modelo de validação."
)

# ==========================================================
# INFORMAÇÕES COMPLEMENTARES
# ==========================================================

st.markdown("---")

with st.expander("ℹ️ Como interpretar as variáveis?"):
    st.write(
        """
        - **Área construída:** representa o tamanho da área construída acima do nível do solo, em pés quadrados.
        - **Qualidade geral:** nota da qualidade da construção e do acabamento.
        - **Vagas na garagem:** capacidade da garagem em número de veículos.
        - **Número de quartos:** quantidade de dormitórios acima do nível do solo.
        - **Área do terreno:** tamanho total do lote, em pés quadrados.
        - **Ano de construção:** ano em que o imóvel foi construído.
        - **Banheiros completos:** quantidade de banheiros completos disponíveis.
        """
    )

with st.expander("📊 Sobre o modelo utilizado"):
    st.write(
        """
        O modelo utilizado nesta aplicação é o **Random Forest Regressor**.

        Esse método combina diversas árvores de decisão e calcula a previsão final
        pela média das estimativas produzidas por essas árvores. Por isso, é capaz de
        capturar relações lineares e não lineares entre as características dos imóveis
        e o preço de venda.

        Durante a etapa de validação preditiva, o Random Forest apresentou menores
        valores de EQM, RMSE e MAE, além de maior coeficiente de determinação (R²)
        na base de teste, quando comparado ao Modelo Linear Generalizado com
        distribuição Gamma.

        O modelo foi desenvolvido utilizando a base de dados
        **House Prices: Advanced Regression Techniques**, disponibilizada na
        plataforma Kaggle.

        A variável resposta **SalePrice** representa o preço de venda dos imóveis em
        **dólares americanos (USD)**, conforme definido na base de dados utilizada.
        """
    )

st.markdown(
    """
    <div class="rodape">

    <hr>

    <b>Projeto de Consultoria Estatística</b><br>

    Sistema desenvolvido para estimativa automática do preço de venda
    de imóveis utilizando o modelo Random Forest.<br><br>

    <b>Desenvolvido por:</b><br>
    Eduarda da Silva Brito<br>
    Maria Helena<br>
    Ana Maria<br><br>

    <b>Universidade Estadual da Paraíba (UEPB)</b><br>
    Curso de Bacharelado em Estatística

    </div>
    """,
    unsafe_allow_html=True
)