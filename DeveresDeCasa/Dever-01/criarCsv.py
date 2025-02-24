import pandas as pd

# Dados já criados por motivos de preguiça
data = {
    "Nome": ["Davi Miranha", "Anna Ketchup", "Leticia Avatar", "Mateus Daddy"],
    "Data de Nascimento": ["03/15/1990", "07/22/1985", "11/05/1993", "01/30/1998"],
    "Dia do Cadastro": ["2025/02/20", "2025/02/19", "2025/02/18", "2025/02/17"],
    "Hora de Cadastro": ["14:35", "10:20", "16:45", "09:15"]
}

# Criação da tabela CSV
df = pd.DataFrame(data)

# Nome do arquivo CSV
file_path_corrected = "csvDataCriado.csv"

# Salvar o arquivo
df.to_csv(file_path_corrected, index=False, encoding='utf-8-sig', sep=';')

# Mensagem
print(f"Arquivo salvo em: {file_path_corrected}")
