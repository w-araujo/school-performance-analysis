import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import matplotlib.pyplot as plt


def load_data(file_path):
    """
    Carrega os dados de um arquivo CSV.

    :param file_path: Caminho para o arquivo CSV
    :return: DataFrame contendo os dados
    """
    data = pd.read_csv(file_path)
    return data

def train_model(data):
    """
    Treina um modelo de regressão linear com os dados fornecidos.

    :param data: DataFrame com os dados de entrada
    :return: modelo treinado
    """
    X = data[["study_hours", "attendance", "previous_grade"]] # Características
    y = data["final_grade"] # Alvo

    # Divide os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Cria o modelo de regressão linear
    model = LinearRegression()

    # Treina o modelo
    model.fit(X_train, y_train)

    # Salva o modelo treinado em um arquivo
    joblib.dump(model, "model.pkl")

    # Os coeficientes indicam o impacto de cada variável na previsão da nota final.
    print("Coeficientes:", model.coef_)

    # O intercepto fornece uma base para a previsão quando todas as variáveis são zero.
    print("Intercepto:", model.intercept_)


    # Avalia o modelo no conjunto de teste
    score = model.score(X_test, y_test)
    print(f"Acurácia do modelo no conjunto de teste: {score:.2f}")

    # Faz previsões com o conjunto de teste
    predictions = model.predict(X_test)

    return model, predictions, y_test

def plot_predictions(predictions, y_test):
    """
    Plota o gráfico de dispersão das previsões versus os valores reais.

    :param predictions: Previsões do modelo
    :param y_test: Valores reais para comparação
    """
    # Calcula o erro absoluto das previsões
    absolute_errors = abs(predictions - y_test)

    # Gráfico de dispersão dos erros absolutos
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(y_test, predictions, c=absolute_errors, cmap='coolwarm', alpha=0.6)
    plt.colorbar(scatter, label='Erro Absoluto')
    plt.xlabel("Nota Real")
    plt.ylabel("Previsão do Modelo")
    plt.title("Gráfico de Dispersão das Previsões com Erros Coloridos")

    # Salva o gráfico como imagem
    plt.savefig("scatter_plot.png")
    print("Gráfico de dispersão salvo como 'scatter_plot.png'")

if __name__ == "__main__":
    # Carrega os dados
    data = load_data("data/students_data.csv")

    # Treina o modelo
    model, predictions, y_test = train_model(data)

    # Grafico das previsões
    plot_predictions(predictions, y_test)

    print("Modelo treinado e salvo como 'model.pkl'")
