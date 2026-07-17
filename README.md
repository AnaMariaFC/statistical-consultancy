# Projeto de Consultoria Estatística

## Descrição

Este repositório reúne os materiais desenvolvidos na disciplina de Consultoria Estatística do Curso de Bacharelado em Estatística da Universidade Estadual da Paraíba (UEPB).

O projeto tem como objetivo desenvolver um sistema de apoio à precificação de imóveis utilizando técnicas de Estatística e Ciência de Dados. Inicialmente, foram ajustados Modelos Lineares Generalizados (MLG) com distribuições Gaussiana e Gamma para identificar os fatores associados ao preço de venda dos imóveis. Em seguida, foi realizada uma etapa de validação preditiva comparando o Modelo Linear Generalizado (MLG) Gamma com o modelo **Random Forest**.

Como resultado da validação, o **Random Forest** apresentou melhor desempenho preditivo e foi utilizado no desenvolvimento da aplicação em Streamlit, que permite ao usuário estimar automaticamente o preço de venda de um imóvel a partir de suas características estruturais.

---

## Objetivos

- Realizar o tratamento e a limpeza da base de dados;
- Desenvolver uma análise exploratória dos dados;
- Ajustar Modelos Lineares Generalizados (MLG);
- Realizar a validação preditiva comparando o MLG Gamma e o Random Forest;
- Selecionar o modelo com melhor desempenho preditivo;
- Desenvolver uma aplicação em Streamlit para estimativa automática do preço de imóveis.

---

## Base de dados

Foi utilizada a base **House Prices: Advanced Regression Techniques**, disponibilizada na plataforma Kaggle.

A base contém informações estruturais de imóveis residenciais localizados na cidade de Ames, Iowa (Estados Unidos), sendo o preço de venda (**SalePrice**) a variável resposta do estudo.

---

## Estrutura do projeto

```text
projeto_1_consultoria/

├── dados/
├── scripts/
├── relatorio/
├── apresentacao/
├── app/
│   └── app.py
├── imagens/
└── README.md
```

---

## Como executar

1. Clone este repositório.
2. Abra o projeto em seu ambiente Python.
3. Instale as dependências necessárias.
4. Execute o notebook para reproduzir as análises.
5. Para utilizar a aplicação, execute:

```bash
streamlit run app/app.py
```

---

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Statsmodels
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---

## Produto desenvolvido

O principal produto deste projeto é um aplicativo em **Streamlit**, capaz de:

- Receber as características estruturais de um imóvel;
- Utilizar o modelo **Random Forest** para estimar automaticamente o preço de venda;
- Exibir o valor estimado do imóvel;
- Apresentar métricas de desempenho do modelo.

---

## Autoras

- Eduarda da Silva Brito
- Maria Helena
- Ana Maria

**Universidade Estadual da Paraíba – UEPB**

Curso de Bacharelado em Estatística

Disciplina: Consultoria Estatística

Professor: Pedro Monteiro de Almeida Júnior