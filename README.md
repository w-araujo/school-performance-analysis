# 📊 School Performance Analysis

Este projeto utiliza um modelo de regressão linear para prever a nota final dos alunos com base em horas de estudo, frequência e nota anterior.

![modelo](https://github.com/w-araujo/school-performance-analysis/blob/main/model_web.png)

## 🛠️ Passo a Passo do Projeto

1. **Importação da Base de Dados**:
   - O primeiro passo consiste em carregar a base de dados contendo informações sobre horas de estudo, frequência e notas anteriores dos alunos. Essa etapa é crucial para garantir que temos todos os dados necessários para o treinamento do modelo.

2. **Treinamento do Modelo**:
   - Em seguida, o modelo de regressão linear é treinado usando os dados importados. Os dados são separados em 80% para treinamento e 20% para testes, permitindo que o modelo aprenda a partir de um conjunto maior de dados e teste sua precisão em um conjunto menor e separado.

3. **Cálculo da Acurácia**:
   - Após o treinamento, avaliamos a performance do modelo calculando sua acurácia. Essa métrica é fundamental para entender o quão bem o modelo está prevendo as notas finais dos alunos com base nos dados de entrada.

4. **Geração do Gráfico de Dispersão**:
   - Por último, um gráfico de dispersão é gerado para visualizar as previsões do modelo. Esse gráfico ajuda a entender a relação entre as variáveis e a qualidade das previsões, permitindo uma análise visual dos dados.


## 🚀 Funcionalidades

#### 1. 📄 `model.py`

Este arquivo contém toda a lógica do projeto, incluindo a importação dos dados, o treinamento do modelo de regressão linear, a avaliação de sua acurácia e a geração do gráfico de dispersão. É o núcleo da aplicação, onde são realizadas as operações necessárias para prever a nota final dos alunos com base em suas horas de estudo, frequência e notas anteriores.

#### 2. 📄 `app.py`

Este arquivo é responsável por criar a interface do usuário utilizando o Streamlit. A interface permite que os usuários interajam com o modelo, visualizem as previsões e explorem os resultados da análise. O `app.py` integra as funcionalidades do `model.py` de forma amigável, facilitando o acesso aos dados e às previsões feitas pelo modelo.

## ⚙️ Como Rodar o Projeto

### 1. Clone o Repositório
   - Comece clonando o repositório para sua máquina local. Use o seguinte comando:
     ```bash
     git clone https://github.com/w-araujo/school-performance-analysis.git
     ```
     
### 2. Navegue até o Diretório do Projeto
   - Entre no diretório do projeto clonado

### 3. Crie o ambiente virtual 
   - Primeiro crie o ambiente virtual
     ```bash
     python3 -m venv env
     ```

### 4. Ative o ambiente virtual 
   - Depois ative o ambiente virtual
     ```bash
     source env/bin/activate
     ```

### 5. Execute o Script de Treinamento
   - Para executar o projeto primeiro passo é treinar o modelo e gerar o arquivo `model.pkl`, além da imagem `scatter_plot.png` com o gráfico de dispersão. Execute o seguinte comando:
     ```bash
     python src/model.py
     ```

### 6. Abra a Interface do Usuário
   - Após treinar o modelo, você pode abrir a interface do usuário utilizando o Streamlit. Execute o comando abaixo:
     ```bash
     streamlit run src/app.py
     ```

### 7. Interaja com a Aplicação
   - Acesse a interface do usuário no seu navegador (normalmente em `http://localhost:8501`) para visualizar e interagir com as previsões do modelo.

## 📝 License
  
This project is under the MIT license. See the file LICENSE for more details.

## 📧 Contact

<div style="display: flex">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wesley-araujo-a99198201/)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/w-araujo)

</div>
