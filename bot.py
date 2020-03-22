import os
import time
import re
import requests
import json
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from selenium import webdriver



class wppbot:

    dir_path = os.getcwd()

    def __init__(self, nome_bot):
        print(self.dir_path)
        self.nome_bot = nome_bot
        self.bot = ChatBot(nome_bot)
        self.bot.set_trainer(ListTrainer)

        self.chrome = self.dir_path+'/chromedriver'

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36")
        self.options.add_argument(r"user-data-dir="+self.dir_path+"/profile/wpp")
        self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)

    def inicia(self,nome_contato):

        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(30)

        self.caixa_de_pesquisa = self.driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']")


        self.caixa_de_pesquisa.send_keys(nome_contato)
        time.sleep(2)
        print(nome_contato)
        self.contato = self.driver.find_element_by_xpath(f"//span[@title='{nome_contato}']")
        self.contato.click()
        time.sleep(2)



    def saudacao(self,frase_inicial):
        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_13mgZ')

        if type(frase_inicial) == list:
            for frase in frase_inicial:
                self.caixa_de_mensagem.send_keys(frase)
                time.sleep(1)
                self.botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                self.botao_enviar.click()
                time.sleep(1)
        else:
            return False

    def escuta(self):
        post = self.driver.find_elements_by_class_name('_1zGQT')
        ultimo = len(post) - 1
        texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
        return texto

    def aprender(self,ultimo_texto,frase_inicial,frase_final,frase_erro):
        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_13mgZ')
        self.caixa_de_mensagem.send_keys(frase_inicial)
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        self.botao_enviar.click()
        self.x = True
        while self.x == True:
            texto = self.escuta()

            if texto != ultimo_texto and re.match(r'^\.\.\.', texto):
                if texto.find('?') != -1:
                    ultimo_texto = texto
                    texto = texto.replace('...', '')
                    texto = texto.lower()
                    texto = texto.replace('?', '?*')
                    texto = texto.split('*')
                    novo = []
                    for elemento in texto:
                        elemento = elemento.strip()
                        novo.append(elemento)

                    self.bot.train(novo)
                    self.caixa_de_mensagem.send_keys(frase_final)
                    time.sleep(1)
                    self.botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                    self.botao_enviar.click()
                    self.x = False
                    return ultimo_texto
                else:
                    self.caixa_de_mensagem.send_keys(frase_erro)
                    time.sleep(1)
                    self.botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                    self.botao_enviar.click()
                    self.x = False
                    return ultimo_texto
            else:
                ultimo_texto = texto

    def noticias(self):

        req = requests.get('https://newsapi.org/v2/top-headlines?sources=globo&pageSize=5&apiKey=f6fdb7cb0f2a497d92dbe719a29b197f')
        noticias = json.loads(req.text)

        for news in noticias['articles']:
            titulo = news['title']
            link = news['url']
            new = f'{self.nome_bot}: ' + titulo + ' ' + link + '\n'

            self.caixa_de_mensagem.send_keys(new)
            time.sleep(1)

    def responde(self,texto):
        response = self.bot.get_response(texto)
        # if float(response.confidence) > 0.5:
        response = str(response)
        response = f'{self.nome_bot}: ' + response
        self.caixa_de_mensagem = self.driver.find_element_by_class_name('_13mgZ')
        self.caixa_de_mensagem.send_keys(response)
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        self.botao_enviar.click()

    def treina(self,nome_pasta):
        for treino in os.listdir(nome_pasta):
            conversas = open(nome_pasta+'/'+treino, 'r').readlines()
            self.bot.train(conversas)

    def cardapio(self):
        itens = ["Cerveja - R$ 5,00", "Coxinha - R$ 3,50", "Refri - R$ 4,00"]
        for item in itens:
            self.caixa_de_mensagem.send_keys(f'\n{self.nome_bot}: {item}')
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        self.botao_enviar.click()

    def bebidas(self):
        itens = ["Água sem gás - R$ 2,00", "Água Tônica - R$ 3,50","Refrigerante litro - R$ 5,00"]
        for item in itens:
            self.caixa_de_mensagem.send_keys(f'\n{self.nome_bot}: {item}')
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        self.botao_enviar.click()

    def cervejas(self):
        itens = ["Schin 600ml - R$ 5,00", "Devassa 600ml - R$ 6,00", "Itaipava 600ml - R$ 6,00"]
        for item in itens:
            self.caixa_de_mensagem.send_keys(f'\n{self.nome_bot}: {item}')
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        self.botao_enviar.click()

    def tiragostos(self):
        itens = ["Camarão ao Alho e Óleo - R$ 25,00", "Carne do Sol - R$ 20,00", "Frango a Passarinha - R$ 16,00"]
        for item in itens:
            self.caixa_de_mensagem.send_keys(f'\n{self.nome_bot}: {item}')
        time.sleep(1)
        self.botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        self.botao_enviar.click()
        