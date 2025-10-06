from requests import options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from configparser import ConfigParser 
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def Peguaroscoockies(Arquivo):
    try: 
        import tempfile

        config = ConfigParser()
        # Configurar opções do Chrome
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument('--headless')
        opcoes.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        opcoes.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # diretório temporário único

        # Configurar o serviço do ChromeDriver usando o WebDriver Manager
        servico = Service(ChromeDriverManager().install())

        # Inicializar o navegador Chrome com as opções configuradas
        navegador = webdriver.Chrome(service=servico, options=opcoes)

        # URL do site a ser aberto (substitua pelo site desejado)
        site = 'https://www.liontechieq.com.br/'

        # Abrir o site no navegador
        navegador.get(site)
        WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        Usuario = 'Datavixcontabil'
        Senha = 'Dtvcont@040817'
        Senha = 'Dtv@040817'
        
        campo_login =  WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, 'Login')))
        campo_senha = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, 'Senha')))
        campo_login.send_keys(Usuario)
        campo_senha.send_keys(Senha)
        campo_senha.submit()
        
        WebDriverWait(navegador, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        cookies = navegador.get_cookies()
        # Nomes dos cookies que você deseja acessar
        Coockie1 = 'ARRAffinity'
        Coockie2 = 'ASP.NET_SessionId'
        Coockie3 = '.ASPXAUTH'
        # encontre os valores desejados
        for cookie in cookies:
            if cookie['name'] == f'{Coockie1}':
                Coockie1_value = cookie['value']
            if cookie['name'] == f'{Coockie2}':
                Coockie2_value =cookie['value']
            if cookie['name'] == f'{Coockie3}':
                Coockie3_value =cookie['value']

        DataAtual = datetime.now()
        DataAtual = DataAtual.strftime('%d/%m/%Y')
        config.read(f'{Arquivo}')
        config.set("default","UltAtualizacao",f'{DataAtual}')
        config.set("default","ARRAffinity",f'{Coockie1_value}')
        config.set("default","SessionID",f'{Coockie2_value}')
        config.set("default","Aspxauth",f'{Coockie3_value}')
        # Escreva as configurações atualizadas de volta para o arquivo
        with open(f'{Arquivo}', 'w') as configfile:
            config.write(configfile)
        print(f"Chaves Atualizadas:\n UltAtualizacao = {DataAtual}\n ARRAffinity = {Coockie1_value}\n SessionID = {Coockie2_value}\n Aspxauth = {Coockie3_value}")
        
        # Esperar por 2 segundos (opcional)
        time.sleep(2)
        
    except Exception as e:
            print(f"Ocorreu um erro ao pegar os coockies: {e}")  


