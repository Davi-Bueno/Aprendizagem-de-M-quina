import random
import pandas as pd

frutas = ['banana', 'maçã', 'laranja', 'uva', 'maçã',"melão","mamão","banana"]

# criar e fecha o arquivo apos o termino do for
#escreve para cada linha uma fruta e a quantidade aleatoria de 0 a 100
with open("minhas_frutas.txt", "w", encoding="utf-8") as f:
    for fruta in frutas:
        quantidade = random.randint(0, 100)
        f.write(f"{fruta},{quantidade}\n")

# Ler o arquivo em formado de dataframe e names= (definir o nome das colunas)
df = pd.read_csv("minhas_frutas.txt", names=['Fruta', 'Quantidade'])

# Agrupar por fruta para somar as quantidades por conta as frutas repetidas
# reseta os indices por conta de nao haver mais fruta repetida 
df_agrupado = df.groupby('Fruta')['Quantidade'].sum().reset_index()

# Exibir o DataFrame com as quantidades somadas
print("\nQuantidade total por fruta:")
print(df_agrupado)



