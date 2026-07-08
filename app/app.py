# ==========================================================
# APP STREAMLIT - PREVISÃO DE PREÇO DE IMÓVEIS
# ==========================================================

import streamlit as st
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from pathlib import Path
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

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
    **Modelo:** MLG Gamma  
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
    Produto de dados desenvolvido a partir de um Modelo Linear Generalizado (MLG) Gamma
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
    4. O sistema exibirá uma estimativa do preço de venda com base no modelo estatístico ajustado.
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
# AJUSTE DO MODELO
# ==========================================================

@st.cache_resource
def ajustar_modelo(modelo):
    formula = """
    SalePrice ~ GrLivArea + OverallQual + GarageCars +
    BedroomAbvGr + LotArea + YearBuilt + FullBath
    """

    modelo_gamma_final = smf.glm(
        formula=formula,
        data=modelo,
        family=sm.families.Gamma(
            link=sm.families.links.Log()
        )
    ).fit()

    return modelo_gamma_final

modelo_gamma_final = ajustar_modelo(modelo)

# ==========================================================
# AVALIAÇÃO DO MODELO
# ==========================================================

y_real = modelo["SalePrice"]
y_pred = modelo_gamma_final.predict(modelo)

rmse = mean_squared_error(y_real, y_pred) ** 0.5
mae = mean_absolute_error(y_real, y_pred)
r2 = r2_score(y_real, y_pred)

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
    "📐 Área construída do imóvel",
    min_value=300,
    max_value=6000,
    value=1800,
    step=50,
    help="Área construída do imóvel, conforme a base original."
)

OverallQual = st.slider(
    "⭐ Qualidade geral do imóvel",
    min_value=1,
    max_value=10,
    value=8,
    help="Nota de qualidade geral do imóvel, variando de 1 a 10."
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
    "🌳 Área total do terreno",
    min_value=1000,
    max_value=50000,
    value=9000,
    step=500,
    help="Área total do terreno do imóvel."
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
        "Área construída",
        "Qualidade geral",
        "Vagas na garagem",
        "Número de quartos",
        "Área do terreno",
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

st.dataframe(resumo, use_container_width=True, hide_index=True)

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

if st.button("🔎 Estimar preço do imóvel", use_container_width=True):
    preco_previsto = modelo_gamma_final.predict(novo_imovel)[0]

    valor = f"{preco_previsto:,.2f}"
    valor = valor.replace(",", "X").replace(".", ",").replace("X", ".")

    st.markdown(
        f"""
        <div class="card">
            <p class="texto-card">💰 Preço estimado de venda</p>
            <div class="resultado">US$ {valor}</div>
            <p class="texto-card">
            Estimativa baseada no Modelo Linear Generalizado (MLG) com distribuição Gamma
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

st.subheader("📊 Desempenho do modelo")

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
    "As métricas são calculadas automaticamente a partir do modelo ajustado na aplicação."
)

# ==========================================================
# INFORMAÇÕES COMPLEMENTARES
# ==========================================================

st.markdown("---")

with st.expander("ℹ️ Como interpretar as variáveis?"):
    st.write(
        """
        - **Área construída:** representa o tamanho da área construída do imóvel.
        - **Qualidade geral:** nota de qualidade da construção e acabamento.
        - **Vagas na garagem:** capacidade da garagem em número de veículos.
        - **Número de quartos:** quantidade de dormitórios do imóvel.
        - **Área do terreno:** tamanho total do lote.
        - **Ano de construção:** ano em que o imóvel foi construído.
        - **Banheiros completos:** quantidade de banheiros completos disponíveis.
        """
    )

with st.expander("📊 Sobre o modelo utilizado"):
    st.write(
        """
        O modelo utilizado nesta aplicação é um **Modelo Linear Generalizado (MLG)**
        com distribuição **Gamma** e função de ligação **log**.

        A escolha desse modelo foi fundamentada na análise exploratória dos dados,
        que evidenciou que a variável resposta apresenta valores contínuos, estritamente
        positivos e distribuição assimétrica à direita, características compatíveis com
        a distribuição Gamma.

        O modelo foi ajustado utilizando a base de dados **House Prices: Advanced Regression Techniques**,
        disponibilizada na plataforma Kaggle.

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
    de imóveis utilizando Modelos Lineares Generalizados (MLG).<br><br>

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