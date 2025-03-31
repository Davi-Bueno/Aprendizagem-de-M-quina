import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def criar_dados_imc():
    # Criando mais dados com uma transição mais suave próximo ao limite de 30
    dados = {
        'IMC': [
            18.0, 20.0, 23.0, 24.5,  # Peso normal
            26.0, 27.0, 28.5, 29.0, 29.5, 29.9,  # Sobrepeso
            30.0, 30.5, 31.0, 33.0, 36.0, 41.0   # Diferentes graus de obesidade
        ],
        'Obeso': [
            False, False, False, False,  # Peso normal
            False, False, False, False, False, False,  # Sobrepeso
            True, True, True, True, True, True      # Obesidade (IMC >= 30)
        ]
    }
    
    # Criando o DataFrame
    df = pd.DataFrame(dados)
    return df

def treinar_modelo(df):
    X = df[['IMC']].values
    # Definimos y diretamente baseado no ponto de corte
    y = (X.flatten() >= 30.0)  # Garantindo comparação com float
    
    clf = RandomForestClassifier(
        n_estimators=1,    
        max_depth=1,       
        random_state=42
    )
    clf.fit(X, y)
    
    return clf


def main():
    st.title('Dados de IMC e Obesidade')
    
    # Criando e exibindo os dados
    df = criar_dados_imc()
    
    st.write('### Dados de Treinamento:')
    st.dataframe(df)
    
    # Interface para fazer previsões
    st.write('### Faça uma Previsão')
    novo_imc = st.number_input('Digite um novo valor de IMC:', min_value=10.0, max_value=50.0, value=25.0, step=0.1)
    
    if st.button('Verificar'):
        resultado = "OBESO" if novo_imc >= 30.0 else "NÃO OBESO"
        st.write(f'Para um IMC de {novo_imc}, a classificação é: **{resultado}**')

if __name__ == '__main__':
    main()
