#Automação Web e Busca de Informações com Python
#Desafio:
#Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:

#Dólar
#Euro
#Ouro
#Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.

#Base de Dados: https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V?usp=sharing

#Para isso, vamos criar uma automação web:

#Usaremos o selenium
#Importante: baixar o webdriver

# instalar o selenium
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome('/Users/otavio.balestra/.conda/envs/macbook/lib/python3.9/site-packages/selenium/webdriver/chrome/chromedriver')

# para rodar o chrome em 2º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True # also works
# nav = webdriver.Chrome(options=chrome_options)

nav = webdriver.Chrome()

# pesquisar cotação dolar
nav.get("https://www.google.com/")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = nav.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

# pesquisar cotação euro
nav.get("https://www.google.com/")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = nav.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

# pegar cotacao ouro
nav.get("https://www.melhorcambio.com/")
aba_original = nav.window_handles[0]
nav.find_element_by_xpath('//*[@id="commodity-hoje"]/tbody/tr[2]/td[2]/a/img').click()
aba_nova = nav.window_handles[1]
nav.switch_to.window(aba_nova)
cotacao_ouro = nav.find_element_by_id('comercial').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

nav.quit()



