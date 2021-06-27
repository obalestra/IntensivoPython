#Análise de Dados com Python
#Desafio:
#Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.

#O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.

#Isso representa uma perda de milhões para a empresa.

#O que a empresa precisa fazer para resolver isso?

#Base de Dados: https://drive.google.com/drive/folders/1w3TmCcQPoc7ew1CXmwwEUpWeHJzJQqGZ?usp=sharing
#Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

#Passo a Passo:
#Passo 1: Importar base de dados
#Passo 2: Visualizar a base de dados
#Passo 3: Ajeitar Problemas da Base de Dados
#Valores de "tipo" errado
#Valores vazios
#Passo 4: Visão geral da distribuição dos cancelamentos
#Passo 5: Analisar como cada característica do cliente impacta no indicador de churn
#Passo 1 e 2

from IPython.display import display
import pandas as pd
import plotly.express as px

telecom_users = pd.read_csv("telecom_users.csv")
display(telecom_users)
telecom_users = telecom_users.drop("Unnamed: 0", axis=1)
display(telecom_users)

# Passo 3
print(telecom_users.info())
# obrigatoriamente nessa ordem
# transformar coluna que deveria ser número e está como texto em número
telecom_users["TotalGasto"] = pd.to_numeric(telecom_users["TotalGasto"], errors="coerce")
print(telecom_users.info())

# remover a coluna que está 100% vazia
telecom_users = telecom_users.dropna(how='all', axis=1)

# remover a linha que tem um item vazio
telecom_users = telecom_users.dropna()

print(telecom_users.info())

#Passo 4
display(telecom_users['Churn'].value_counts())
display(telecom_users['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

#Passo 5
# para edições nos gráficos: https://plotly.com/python/histograms/

for coluna in telecom_users:
    if coluna != "IDCliente":
        # criar a figura
        fig = px.histogram(telecom_users, x=coluna, color="Churn")
        # exibir a figura
        fig.show()
        display(telecom_users.pivot_table(index="Churn", columns=coluna, aggfunc='count')["IDCliente"])