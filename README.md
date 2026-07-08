\# Projeto de Consultoria Estatística



\## Descrição



Este repositório reúne os materiais desenvolvidos na disciplina de Consultoria Estatística do Curso de Bacharelado em Estatística da Universidade Estadual da Paraíba (UEPB).



O projeto tem como objetivo desenvolver um sistema de apoio à precificação de imóveis por meio de Modelos Lineares Generalizados (MLG), utilizando informações estruturais dos imóveis para estimar automaticamente o preço de venda.



Como produto final, foi desenvolvida uma aplicação interativa em Streamlit que permite ao usuário informar as características de um imóvel e obter uma estimativa do seu valor de venda.



\---



\## Objetivos



\- Realizar o tratamento e a limpeza da base de dados;

\- Desenvolver uma análise exploratória dos dados;

\- Ajustar e comparar Modelos Lineares Generalizados (MLG);

\- Selecionar o modelo estatístico com melhor desempenho;

\- Desenvolver uma aplicação em Streamlit para estimativa automática do preço de imóveis.



\---



\## Base de dados



Foi utilizada a base \*\*House Prices: Advanced Regression Techniques\*\*, disponibilizada na plataforma Kaggle.



A base contém informações estruturais de imóveis residenciais localizados na cidade de Ames, Iowa (Estados Unidos), sendo o preço de venda (SalePrice) a variável resposta do estudo.



\---



\## Estrutura do repositório



```

projeto\_1\_consultoria/

│

├── dados/

│   ├── pre\_projeto/

│   └── projeto\_final/

│

├── scripts/

│   ├── pre\_projeto/

│   └── projeto\_final/

│

├── relatorios/

│   ├── pre\_projeto/

│   └── projeto\_final/

│

├── apresentacoes/

│   ├── pre\_projeto/

│   └── projeto\_final/

│

├── app/

│   └── app.py

│

└── README.md

```



\---



\## Como executar



1\. Clone este repositório.

2\. Abra o projeto em seu ambiente Python.

3\. Instale as dependências necessárias.

4\. Execute o notebook para reproduzir as análises.

5\. Para utilizar a aplicação, execute:



```bash

streamlit run app.py

```



\---



\## Tecnologias utilizadas



\- Python

\- Pandas

\- NumPy

\- Statsmodels

\- Scikit-learn

\- Plotly

\- Matplotlib

\- Seaborn

\- Streamlit



\---



\## Produto desenvolvido



O principal produto deste projeto é uma aplicação em \*\*Streamlit\*\*, capaz de:



\- Receber as características estruturais de um imóvel;

\- Ajustar automaticamente o Modelo Linear Generalizado (MLG);

\- Estimar o preço de venda do imóvel;

\- Exibir métricas de desempenho do modelo.



\---



\## Autoras



\- Eduarda da Silva Brito

\- Maria Helena

\- Ana Maria



Universidade Estadual da Paraíba – UEPB



Curso de Bacharelado em Estatística



Disciplina: Consultoria Estatística



Professor: Pedro Monteiro de Almeida Júnior

