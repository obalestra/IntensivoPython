#Projeto Ciência de Dados - Previsão de Vendas
#Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a #empresa Hashtag investe: TV, Jornal e Rádio
#Passo a Passo de um Projeto de Ciência de Dados
#Passo 1: Entendimento do Desafio
#Passo 2: Entendimento da Área/Empresa
#Passo 3: Extração/Obtenção de Dados
#Passo 4: Ajuste de Dados (Tratamento/Limpeza)
#Passo 5: Análise Exploratória
#Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
#Passo 7: Interpretação de Resultados
#Importar a Base de dados

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn.model_selection
from IPython.display import display
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

advertising = pd.read_csv("advertising.csv")
display(advertising)

#Análise Exploratória
#Vamos tentar visualizar como as informações de cada item estão distribuídas
#Vamos ver a correlação entre cada um dos itens

sns.heatmap(advertising.corr(), annot =True, cmap="Wistia")
plt.show()
sns.pairplot(advertising)
plt.show()

#Com isso, podemos partir para a preparação dos dados para treinarmos o Modelo de Machine Learning
#Separando em dados de treino e dados de teste

x = advertising.drop('Vendas', axis=1)
y = advertising['Vendas']
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.3, random_state=1)

#Temos um problema de regressão - Vamos escolher os modelos que vamos usar:
#Regressão Linear
#RandomForest (Árvore de Decisão)

# treino AI
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

rf_reg = RandomForestRegressor()
rf_reg.fit(x_train, y_train)

#Teste da AI e Avaliação do Melhor Modelo
#Vamos usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece
#Também vamos olhar o MSE (Erro Quadrático Médio) -> diz o quanto o nosso modelo "erra" quando tenta fazer uma previsão

# teste AI
test_pred_lin = lin_reg.predict(x_test)
test_pred_rf = rf_reg.predict(x_test)

r2_lin = metrics.r2_score(y_test, test_pred_lin)
mse_lin = metrics.mean_squared_error(y_test, test_pred_lin)
print(f"R² da Regressão Linear: {r2_lin}")
print(f"MSE da Regressão Linear: {mse_lin}")
r2_rf= metrics.r2_score(y_test, test_pred_rf)
mse_rf = metrics.mean_squared_error(y_test, test_pred_rf)
print(f"R² do Random Forest: {r2_rf}")
print(f"MSE do Random Forest: {mse_rf}")

#Visualização Gráfica das Previsões

df_resultado = pd.DataFrame()
# df_resultado.index = x_test
df_resultado['y_teste'] = y_test
df_resultado['y_previsao_rf'] = test_pred_rf
df_resultado['y_previsao_lin'] = test_pred_lin

# display(df_resultado)
# df_resultado = df_resultado.reset_index(drop=True)
plt.figure(figsize=(15, 5))
sns.lineplot(data=df_resultado)
plt.show()
display(df_resultado)

#Qual a importância de cada variável para as vendas?
# importancia_features = pd.DataFrame(rf_reg.feature_importances_, x_train.columns)
# plt.figure(figsize=(15, 5))
sns.barplot(x=x_train.columns, y=rf_reg.feature_importances_)
plt.show()

#Será que estamos investindo certo?
print(advertising[["Radio", "Jornal"]].sum())