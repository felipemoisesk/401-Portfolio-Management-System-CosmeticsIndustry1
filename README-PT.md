<h1 align="center">
     <a> 401-Sistema-Gestao-Portfolio-IndustriaCosmeticos1 </a>
</h1>

<h4 align="center">
	🚧 OUT/21 até MAR/22 🚀 🚧
</h4>

## 💻 Sobre o projeto

O Sistema de Gestão de Portfólio, ou SGP, é um sistema desenvolvido para o núcleo Portfólio & Categorias, Diretoria de Inteligência de Mercado, que oferece uma visão detalhada do portfólio de varejo, em nível de SKU, considerando a coleta, processamento, democratização e análise de dados para os stakeholders da empresa.

A ferramenta a seguir, contempla a fase de ETL do projeto, coletando e processando dados de diversos sistemas da empresa, disponibilizados após a extração em arquivos .xlsx ou .csv, em sua maioria.

A construção desta ferramenta reduziu o tempo de processamento em 87% em relação a solução original que fora desenvolvida em Excel pelo time anteriormente responsável, passando de +8h para menos de 1h, considerando o início processamento até a entrega final com pré-análises e ferramenta gráfica.

A fim de atender as necessidades de um time marjoritariamente composto por pessoas com habilidades em negócio, foi escolhido o Microsoft SharePoint como repositório de arquivos brutos, tratados e refinados, emulando um ambiente em camadas (Bronze, Prata e Ouro) já conhecido em pipelines ETL em engenharia de dados.

Como parte da análise dos dados, os painéis em Tableau e PowerBI foram disponibilizados para a equipe, incluindo modelagem de dados dimensionais em ambos.

O projeto traz valor e autonomia para a equipe de negócios, desde ETL até autoconsumo de dados e análise da equipe.

---

## ⚙️ Funcionalidades

- [x] **Automação de ETL**:
  - [x] criação de datamart, localhost e Microsoft SharePoint, em camadas Bronze, Prata e Ouro:
    - bronze: dados extraídos dos sistemas em formatos TXT, XLSX e CSV
    - prata: dados tratados, limpos e organizados em arquivos tabulares 
    - ouro: dados refinados, com modelagem dimensional aplicada para entrada nas ferramentas de dataviz da empresa
  - [x] interação entre script e usuário:
    - navegação entre os módulos e sub-módulos que deseja atualizar de forma interativa e instruída, através de perguntas e seleção de respostas

- [x] **Ferramenta construída em módulos interconectados**: 
  - [x] módulo Performance Financeira 
    - regiões geográficas
    - regiões comerciais
    - canais de venda
  - [x] módulo Planejamento Comercial 
    - regiões geográficas
    - canais de venda

---

## 🚀 Como executar a ferramenta


Ao executar os scripts, o usuário receberá na tela de execução perguntas a respeito dos módulos que deseja atualizar.

Todavia, esta ferramenta é composta por três estágios:

1. Coleta das informações transacionais da empresa, via xlsx/txt/csv, ou relatórios gerados nos diversos sistemas da empresa e departamentos (inserção camada Bronze) 
2. Execução automatizada de script em python para processamento, limpeza de dados, modelagem dimensional de dados e pré-organização de arquivos de dados (inserção camada Prata)
3. Disponibilização em repositório, output, dos dados tratados conforme requisitos de negócio (inserção camada Ouro)

💡 A visualização de dados via Tableau ou PowerBi utilizam o output da camada Ouro da ferramenta.

### Pré-requisitos

Por ser uma ferramenta que funciona localmente, antes de começar, você vai precisar fazer o download deste projeto em sua máquina, pois assim os repositórios já serão vinculados ao diretório do projeto. Além disto, recomendo fazer o download do [Git](https://git-scm.com) para controle de versões. Sobre IDE, utilizei o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=linux).

---

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

#### **ETL**  ([Python](https://www.python.org/))

-   **[Pandas](https://pandas.pydata.org/)**
-   **[NumPy](https://github.com/ReactTraining/react-router/tree/master/packages/react-router-dom)**
-   **[OS](https://docs.python.org/3/library/os.html)**
-   **[Matplotlib](https://matplotlib.org/)**

### **Visualização de Dados**

-   **[Tableau](https://www.tableau.com/)**
-   **[PowerBI](https://powerbi.microsoft.com/pt-br/)**

### **Repositório de Dados**

-   **[Microsoft SharePoint](https://www.microsoft.com/pt-br/microsoft-365/sharepoint/collaboration)**

#### **Utilitários**

-   Editor:  **[PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=linux)**

---

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

Feito com ❤️ por Felipe Möises 👋🏽 [Entre em contato!](https://www.linkedin.com/in/felipemoises/)

---

##  Versões do README

[Francês 🇫🇷](./README-FR.md)  |  [Inglês 🇺🇸](./README.md)
