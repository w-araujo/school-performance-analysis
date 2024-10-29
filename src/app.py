import streamlit as st
import joblib
import pandas as pd

# Carrega o modelo treinado
model = joblib.load("model.pkl")

def predict_grade(study_hours, attendance, previous_grade):
    """
    Faz a previsão da nota final usando o modelo treinado.

    :param study_hours: Horas de estudo
    :param attendance: Frequência
    :param previous_grade: Nota anterior
    :return: Nota final prevista
    """
    input_data = pd.DataFrame([[study_hours, attendance, previous_grade]], columns=["study_hours", "attendance", "previous_grade"])
    predicted_grade = model.predict(input_data)
    return predicted_grade[0]

# Interface Streamlit
st.image("logo.png")
st.title("Análise de rendimento Escolar")


study_hours = st.number_input("Horas de Estudo", min_value=0, max_value=10, step=1)
attendance = st.number_input("Frequência (%)", min_value=0, max_value=100, step=10)
previous_grade = st.number_input("Nota Anterior", min_value=0, max_value=100, step=10)

if st.button("Prever Nota Final"):
    predicted = predict_grade(study_hours, attendance, previous_grade)
    final_grade = min(predicted, 100)
    st.write(f"A nota final prevista é: {final_grade:.2f}")
