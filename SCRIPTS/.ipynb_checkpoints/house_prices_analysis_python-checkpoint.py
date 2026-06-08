import numpy as np
import pandas as pd

# Supondo que você já carregou seu dataset
df = pd.read_csv('/home/delfos/Documentos/UEPB_20260326/PEDRO_MONTEIRO/CONSULTANCY/CONSULTANCY_PROJECTS/HOUSE_PRICES_PROJECT/DATA/house-prices-advanced-regression-techniques/train.csv')
print(df.head())

def tratar_valores_nulos(df):
    df_clean = df.copy()

    # 1. Colunas onde "NA" significa que a casa NÃO POSSUI o item (Preencher com "None")
    cols_none = [
        'PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 
        'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 
        'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 
        'BsmtFinType2', 'MasVnrType'
    ]
    for col in cols_none:
        df_clean[col] = df_clean[col].fillna("None")

    # 2. Colunas numéricas onde "NA" significa que não há o item (Preencher com 0)
    # Ex: Se não tem garagem, a área da garagem é 0 e o ano de construção pode ser 0
    cols_zero = [
        'GarageYrBlt', 'GarageArea', 'GarageCars', 'BsmtFinSF1', 
        'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 
        'BsmtHalfBath', 'MasVnrArea'
    ]
    for col in cols_zero:
        df_clean[col] = df_clean[col].fillna(0)

    # 3. LotFrontage (Fachada do lote)
    # Casas no mesmo bairro tendem a ter fachadas parecidas. Vamos preencher com a mediana do bairro.
    df_clean['LotFrontage'] = df_clean.groupby('Neighborhood')['LotFrontage'].transform(
        lambda x: x.fillna(x.median())
    )

    # 4. Variáveis categóricas comuns onde "NA" é dado faltante de verdade (Preencher com a Moda)
    # A moda é o valor que mais aparece na coluna.
    cols_mode = [
        'MSZoning', 'Electrical', 'KitchenQual', 'Exterior1st', 
        'Exterior2nd', 'SaleType'
    ]
    for col in cols_mode:
        df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

    # 5. Utilities (A maioria esmagadora é "AllPub", então essa coluna geralmente não ajuda muito e pode ser dropada)
    # Mas se quiser manter, preencha com a moda também ou remova.
    if 'Utilities' in df_clean.columns:
        df_clean = df_clean.drop(['Utilities'], axis=1)

    # 6. Functional (O dicionário de dados diz que NA significa "Typ" - Typical)
    df_clean['Functional'] = df_clean['Functional'].fillna("Typ")
    
    df_tratado = tratar_valores_nulos(df)
    df_tratado

    return df_clean

    print(df.isnull().sum().max())


# Aplicando a função no seu dataframe
# df_corrigido = tratar_valores_nulos(df)
# print("Valores nulos restantes:", df_corrigido.isnull().sum().max())