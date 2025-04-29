import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# Carregar o dataset
iris = load_iris()
X = iris.data
y = iris.target
nomes_especies = iris.target_names

# Treinar o modelo Random Forest
modelo_rf = RandomForestClassifier()
modelo_rf.fit(X, y)

# Treinar o modelo KNN
modelo_knn = KNeighborsClassifier(n_neighbors=3)
modelo_knn.fit(X, y)

# Interface Streamlit
st.title("Classificação de Flores - Dataset Íris 🌸")
st.write("Insira as características da flor para prever a espécie:")

# Coletar entradas do usuário
comprimento_sepala = st.number_input("Comprimento da sépala (cm)", min_value=0.0, step=0.1)
largura_sepala = st.number_input("Largura da sépala (cm)", min_value=0.0, step=0.1)
comprimento_petala = st.number_input("Comprimento da pétala (cm)", min_value=0.0, step=0.1)
largura_petala = st.number_input("Largura da pétala (cm)", min_value=0.0, step=0.1)

entrada = np.array([[comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]])

if st.button("Classificar"):
    # Previsão com Random Forest
    predicao_rf = modelo_rf.predict(entrada)
    especie_rf = nomes_especies[predicao_rf[0]]

    # Previsão com KNN
    predicao_knn = modelo_knn.predict(entrada)
    especie_knn = nomes_especies[predicao_knn[0]]

    st.subheader("Resultados da Classificação:")
    st.write(f"🌲 Random Forest: **{especie_rf}**")
    st.write(f"🤖 K-Nearest Neighbors (k=3): **{especie_knn}**")

    # Gráfico de comparação
    fig, ax = plt.subplots()
    cores = ['red', 'green', 'blue']

    for i, cor in enumerate(cores):
        idx = np.where(y == i)
        ax.scatter(X[idx, 0], X[idx, 1], label=nomes_especies[i], c=cor)

    # Marcar o ponto inserido pelo usuário
    ax.scatter(comprimento_sepala, largura_sepala, c='black', marker='X', s=100, label='Sua entrada')

    ax.set_xlabel('Comprimento da Sépala (cm)')
    ax.set_ylabel('Largura da Sépala (cm)')
    ax.legend()
    ax.set_title('Visualização das Espécies - Sepala')

    st.pyplot(fig)
