import streamlit as st
import pandas as pd

def criar_csv():
    # Criar dados
    dados = {
        'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo'],
        'Idade': [25, 30, 22, 28, 35]
    }
    
    # Criar DataFrame e salvar como CSV
    df = pd.DataFrame(dados)
    df.to_csv('dados.csv', index=False) 
    return "Arquivo dados.csv criado com sucesso!"

def ler_dados():
    try:
        # Ler o arquivo CSV
        df = pd.read_csv('dados.csv')
        return df
    except FileNotFoundError:
        return None

def verificar_idade(nome, df):
    # Verificar se o nome existe
    if nome in df['Nome'].values:
        idade = df[df['Nome'] == nome]['Idade'].iloc[0]
        idade_max = df['Idade'].max()
        mais_velho = idade == idade_max
        
        if mais_velho:
            return f"{nome} tem {idade} anos, é a pessoa mais velha da lista."
        else:
            return f"{nome} tem {idade} anos, não é a pessoa mais velha da lista."
    else:
        return "Nome não encontrado."

def main():
    st.title("Verificador de Idade")
    
    # Criar o arquivo CSV
    if st.button("Criar arquivo CSV"):
        st.write(criar_csv())
    
    # Ler dados
    df = ler_dados()
    
    if df is not None:
        # Campo para entrada do nome
        nome = st.text_input("Digite um nome:")
        
        if nome:
            resultado = verificar_idade(nome, df)
            st.write(resultado)
    else:
        st.error("Arquivo dados.csv não encontrado. Clique no botão para criar.")

if __name__ == "__main__":
    main()
