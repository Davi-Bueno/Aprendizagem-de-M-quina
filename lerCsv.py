import pandas as pd
import streamlit as st
import os
import subprocess

# Caminho do arquivo CSV previamente criado
definir_caminho = "csvDataCriado.csv"

# Leitura do CSV
try:
    df = pd.read_csv(definir_caminho, sep=';', encoding='utf-8-sig')
    st.write("### 📋 Dados CSV:")
    st.dataframe(df)  # Exibe a tabela no Streamlit
except FileNotFoundError:
    st.error("🚨 Arquivo CSV não encontrado! Certifique-se de que o script foi executado corretamente.")
    st.stop()

# Variável de estado para evitar execução automática no início
if "registro_exibido" not in st.session_state:
    st.session_state.registro_exibido = False
if "ultimo_n" not in st.session_state:
    st.session_state.ultimo_n = None  # Armazena o último `n` exibido

# Mapeamento de registros para imagens
imagens = {
    0: "eu.jpg",
    1: "ana_heinz.webp",
    2: "let_avatar.jpg",
    3: "math_gravido.webp"
}

# Formulário para capturar "Enter" automaticamente
with st.form(key="formulario_registro"):
    n = st.text_input(f"Digite o número do registro (0 a {len(df) - 1}):")
    submit_button = st.form_submit_button("🔍 Exibir Registro")  # Botão para enviar manualmente

# Se o botão foi pressionado OU se o usuário apertou "Enter" dentro do formulário
if submit_button or n:
    try:
        n = int(n)  # Converter input para número

        if 0 <= n < len(df):  # Verifica se o número está dentro do intervalo válido
            registro = df.iloc[n]

            # Exibir os dados formatados
            st.success(
                f"### ✅ Registro Encontrado\n\n"
                f"**👤 Nome:** {registro['Nome']}\n\n"
                f"**📅 Data de Nascimento:** {registro['Data de Nascimento']}\n\n"
                f"**📌 Data de Cadastro:** {registro['Dia do Cadastro']}\n\n"
                f"**⏰ Hora de Cadastro:** {registro['Hora de Cadastro']}"
            )
            st.session_state.registro_exibido = True  # Marca que um registro válido foi exibido
            st.session_state.ultimo_n = n  # Salva o último `n` exibido

            # Exibir imagem correspondente
            if n in imagens:
                caminho_imagem = imagens[n]
                if os.path.exists(caminho_imagem):
                    st.image(caminho_imagem, width=300)
                else:
                    st.warning(f"⚠️ Imagem '{caminho_imagem}' não encontrada no diretório.")

        else:  # Número inválido
            st.warning(
                f"### ❌ ERRO: Registro Inválido\n\n"
                f"🔴 **Número escolhido ({n}) está fora do intervalo permitido!**\n\n"
                f"✔️ Escolha um número entre **0 e {len(df) - 1}**."
            )
            st.session_state.registro_exibido = False  

    except ValueError:
        st.error("⚠️ ERRO: Entrada inválida! Digite um número válido entre 0 e {}.".format(len(df) - 1))
        st.session_state.registro_exibido = False 

# Se o registro foi exibido E for o número 3, exibir botão para alterar o papel de parede
if st.session_state.registro_exibido and st.session_state.ultimo_n == 3:
    if st.button("⚠️ NÃO CLIQUE AQUI!"):
        script_path = os.path.join(os.getcwd(), "change_wallpaper.ps1")
        try:
            # Executa o script PowerShell
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path], shell=True)
            st.success("✅ Papel de parede alterado com sucesso!")
        except Exception as e:
            st.error(f"🚨 Erro ao alterar o plano de fundo: {e}")
