#Automação de Sistemas e Processos com Python
#Desafio:
#Todos os dias, o nosso sistema atualiza as vendas do dia anterior. O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior

#E-mail da diretoria: seugmail+diretoria@gmail.com
#Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/1mhXZ3JPAnekXP_4vX7Z_sJj35VWqayaR?usp=sharing

#Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

#Passo 1: Lógica de Programação
#Passo 2: Transformar o passo a passo em Python

import pyautogui
import time
import pyperclip

#pyautogui.PAUSE = 1
#pyautogui.alert("Vai começar, aperte OK e não mexa em nada")

# opção 1 - abrir navegador novo e entrar no chrome
# pyautogui.press("winleft")
# pyautogui.write("chrome")
# pyautogui.press("enter")

# opção 2 - abrir uma nova aba
#pyautogui.hotkey('command', 't')

# abrir drive
# ensinar aqui o write
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing"
#pyperclip.copy(link)
#pyautogui.hotkey("command", "v")
#pyautogui.press("enter")
#time.sleep(7)

# baixar base de dados atualizada
#pyautogui.click(414, 271, clicks=2)
#time.sleep(2)
#pyautogui.click(407, 353)
#pyautogui.click(1163, 153)
#pyautogui.click(1052, 599)
#time.sleep(10)

#Vamos agora ler o arquivo baixado para pegar os indicadores
#Faturamento
#Quantidade de Produtos
from IPython.display import display
import pandas as pd
import pyperclip

df = pd.read_excel("Vendas - Dez.xlsx")
display(df)
faturamento = df['Valor Final'].sum()
qtde_produtos = df['Quantidade'].sum()
print(faturamento)
print(qtde_produtos)

#Vamos agora enviar um e-mail pelo gmail
texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {qtde_produtos:,}

Abs
Otavio Balestra Filho"""

print(texto)

# abrir aba gmail
pyautogui.hotkey('command', 't')
pyautogui.write("mail.google.com")
pyautogui.press('enter')
time.sleep(5)

# clicar em escrever email
pyautogui.click(133, 183)

# preencher informações do e-mail
pyautogui.write('otaviobalestra+diretoria@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
assunto = "Relatório de Vendas de Ontem"
pyperclip.copy(assunto)
pyautogui.hotkey("command", 'v')
pyautogui.press("tab")

pyperclip.copy(texto)
pyautogui.hotkey("command", 'v')

# enviar e-mail
pyautogui.hotkey('command', 'enter')

# avisar que acabou
pyautogui.alert("Fim da Automação. Seu computador já voltou a ser seu")