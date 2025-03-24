import random
import pandas as pd
import streamlit as st
import os

frutas = ['banana', 'maçã', 'laranja', 'uva', 'maçã',"melão","mamão","banana"]

# Título do app
st.title("Controle de Frutas")

# Botão para gerar novo arquivo
if st.button("Gerar novo arquivo de frutas"):
    # criar e fecha o arquivo apos o termino do for
    #escreve para cada linha uma fruta e a quantidade aleatoria de 0 a 100
    with open("minhas_frutas.txt", "w", encoding="utf-8") as f:
        for fruta in frutas:
            quantidade = random.randint(0, 100)
            f.write(f"{fruta},{quantidade}\n")
    st.success("Arquivo gerado com sucesso!")

# Verificar se o arquivo existe
if os.path.exists("minhas_frutas.txt"):
    # Ler o arquivo em formato de dataframe e names= (definir o nome das colunas)
    df = pd.read_csv("minhas_frutas.txt", names=['Fruta', 'Quantidade'])

    # Mostrar dados originais
    st.subheader("Dados Originais")
    st.dataframe(df)

    # Agrupar por fruta para somar as quantidades por conta as frutas repetidas
    # reseta os indices por conta de nao haver mais fruta repetida 
    df_agrupado = df.groupby('Fruta')['Quantidade'].sum().reset_index()

    # Mostrar dados agrupados
    st.subheader("Quantidade Total por Fruta")
    st.dataframe(df_agrupado)
else:
    st.warning("Arquivo 'minhas_frutas.txt' não encontrado. Por favor, clique no botão acima para gerar o arquivo.")





