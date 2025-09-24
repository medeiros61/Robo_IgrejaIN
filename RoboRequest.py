import requests 
import re
import http.cookiejar, urllib.request

def cokkieSession():

    url = "https://www.liontechieq.com.br"
 
#    response = requests.request("POST", url)
#    txtCokkies = str(response.cookies.values)

    s = requests.Session()
#    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get(url)

    print(r.text)





def cokkie():

    url = "https://www.liontechieq.com.br/"
 
    response = requests.request("POST", url)
    txtCokkies = str(response.cookies.values)
    print(txtCokkies)

    #txt = "<option value=(.+?)</option>"
    #txt = 'value=(.*)</option>'
    #txt = r"name=(.+?),"
    txt = 'name=|value='

    print('#############################')

    #txtCokkies = 'Anderson Antonio name= Medeiros'
    print(re.findall(r"value=.*',", txtCokkies))

    print(re.findall(r"value=+.*?',", txtCokkies))
    txtCokkies = re.findall(r"value=+.*?',", txtCokkies)
    print('#############################')
    txtCokkies = str(txtCokkies)
    
    txtCokkies = txtCokkies[txtCokkies.find("'")+1:txtCokkies.rfind("'")]
    print('############FIM############')

    print(txtCokkies)

    #print(response.cookies.values)
#    response = requests.request("POST", url, headers=headers, data = payload)


def login():
    url = "https://www.liontechieq.com.br/"

    payload = 'Login=datavixcontabil&Senha=datavix040817'
    headers = {
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.liontechieq.com.br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded'
#    'Cookie': 'ARRAffinity=cb1d004228e5e638cf6f288f7672a0c4c4fb23b09c8f14e08ab3cbc6d50ef4f2; ASP.NET_SessionId=nbq4j251rrsittvrvniqevzh; .ASPXAUTH=CE85497EA02C15A32A101F3138A98EF5FEB7F6C86940D2C36DF2BA7324CE7D2DB157EC4038D4E72D12B3A6A4F281834DE111ADD118D34026A63F66E8A0EB212065C69A17C68F036B53EFC31EAEBEF73E0A5E45DF284FBA5BB4913CBF81903E3B5EE5840C593B99EFF58DB6B02F55A2A26A903D645FF5DA23C824067FDF87D19283BF35FBFE1E55E76BE3353BCB384604FB772925D194C4A2BAE39A1E7497ED88AF5953A9D254EFDA9057B2B030A4CDDC'
    }

    #response = requests.request("POST", url, headers=headers, data = payload)
    response = requests.request("POST", url)
    txtCokkies = str(response.cookies.values)
    #print(requests.cookies.RequestsCookieJar.values)
        
    texto = response.text
    #print(response.status_code)
    #response = requests.get(url)
    #print(texto)
    Encontrado = format("Esqueci meu login/senha" in texto)      # "erro"
    print("erro : " + Encontrado)
        
    session = requests.Session()
    session.get(url)
    print('session cookies')
    print(session.cookies)

    if Encontrado == "False":               #erro
        print('------------------cookies------------------------')
        #print(response.cookies['.ASPXAUTH'])
        txtCokkies = str(response.cookies.values)
        print(txtCokkies)
        #txtCokkies = re.findall(r"value=+.*?',", txtCokkies)
        #print('#############################')
        #txtCokkies = str(txtCokkies)
        #txtCokkies = txtCokkies[txtCokkies.find("'")+1:txtCokkies.rfind("'")]
        print('############FIM############')
        print(txtCokkies)

    else:
        print('Erro')

    #url = 'http://somewebsite/some/cookie/setting/url'
    #r = requests.get(url)
    #r.cookies['some_cookie_name']
    #'some_cookie_value'



def createLancamento():

    url = "https://www.liontechieq.com.br/RelatorioCulto/Create"

    payload = 'Dia=13&Dizimos=20,50&Hora=20%3A30&ID_Entidade=51993&OfertaMissoes=21,54&OfertasEspeciais=22,33&OfertasGerais=0%2C02&OutrasEntradas=0%2C04&Periodo=04/2020'
    headers = {
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.liontechieq.com.br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ARRAffinity=cb1d004228e5e638cf6f288f7672a0c4c4fb23b09c8f14e08ab3cbc6d50ef4f2; ASP.NET_SessionId=nbq4j251rrsittvrvniqevzh; .ASPXAUTH=CE85497EA02C15A32A101F3138A98EF5FEB7F6C86940D2C36DF2BA7324CE7D2DB157EC4038D4E72D12B3A6A4F281834DE111ADD118D34026A63F66E8A0EB212065C69A17C68F036B53EFC31EAEBEF73E0A5E45DF284FBA5BB4913CBF81903E3B5EE5840C593B99EFF58DB6B02F55A2A26A903D645FF5DA23C824067FDF87D19283BF35FBFE1E55E76BE3353BCB384604FB772925D194C4A2BAE39A1E7497ED88AF5953A9D254EFDA9057B2B030A4CDDC'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))


def VerificaLancamento():
    url = "https://www.liontechieq.com.br/RelatorioCulto/VerificaLancamentoExistente?Hora=19:30&Periodo=04/2020&Dia=2&ID_TransacaoGrupo=undefined&ID_Entidade=51993"

    payload = {}
    headers = {
    'Cookie': '.ASPXAUTH=CE85497EA02C15A32A101F3138A98EF5FEB7F6C86940D2C36DF2BA7324CE7D2DB157EC4038D4E72D12B3A6A4F281834DE111ADD118D34026A63F66E8A0EB212065C69A17C68F036B53EFC31EAEBEF73E0A5E45DF284FBA5BB4913CBF81903E3B5EE5840C593B99EFF58DB6B02F55A2A26A903D645FF5DA23C824067FDF87D19283BF35FBFE1E55E76BE3353BCB384604FB772925D194C4A2BAE39A1E7497ED88AF5953A9D254EFDA9057B2B030A4CDDC; ARRAffinity=cb1d004228e5e638cf6f288f7672a0c4c4fb23b09c8f14e08ab3cbc6d50ef4f2'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))


def ProcuraNaLista(Procura,Lista):
    for index, item in enumerate(Lista):
        #test = format(">95" in item)
        Encontrado = format(Procura in item)

        #print(test)
        if Encontrado == "True":
            print("Encontrado " + str(index) +" "+ item)
            return item[1:6]


def CarregarCreateLimpo():
    url = "https://www.liontechieq.com.br/RelatorioCulto/Create"

    payload = {}
    headers = {
    'Cookie': '.ASPXAUTH=CE85497EA02C15A32A101F3138A98EF5FEB7F6C86940D2C36DF2BA7324CE7D2DB157EC4038D4E72D12B3A6A4F281834DE111ADD118D34026A63F66E8A0EB212065C69A17C68F036B53EFC31EAEBEF73E0A5E45DF284FBA5BB4913CBF81903E3B5EE5840C593B99EFF58DB6B02F55A2A26A903D645FF5DA23C824067FDF87D19283BF35FBFE1E55E76BE3353BCB384604FB772925D194C4A2BAE39A1E7497ED88AF5953A9D254EFDA9057B2B030A4CDDC; ARRAffinity=cb1d004228e5e638cf6f288f7672a0c4c4fb23b09c8f14e08ab3cbc6d50ef4f2'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    texto = response.text #.encode('utf8')

    txt = "<option value=(.+?)</option>"
    txt = "<option value=(.+?)</option>"
    txt = 'value=(.*)</option>'
    x = re.findall(txt, texto)

    print(ProcuraNaLista(">62829",x))

def login1():
    url = "https://www.liontechieq.com.br/"

    payload = 'Login=datavixcontabil&Senha=datavix040817'
    headers = {
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.liontechieq.com.br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded'
#    'Cookie': 'ARRAffinity=cb1d004228e5e638cf6f288f7672a0c4c4fb23b09c8f14e08ab3cbc6d50ef4f2; ASP.NET_SessionId=nbq4j251rrsittvrvniqevzh; .ASPXAUTH=CE85497EA02C15A32A101F3138A98EF5FEB7F6C86940D2C36DF2BA7324CE7D2DB157EC4038D4E72D12B3A6A4F281834DE111ADD118D34026A63F66E8A0EB212065C69A17C68F036B53EFC31EAEBEF73E0A5E45DF284FBA5BB4913CBF81903E3B5EE5840C593B99EFF58DB6B02F55A2A26A903D645FF5DA23C824067FDF87D19283BF35FBFE1E55E76BE3353BCB384604FB772925D194C4A2BAE39A1E7497ED88AF5953A9D254EFDA9057B2B030A4CDDC'
    }

    #response = requests.request("POST", url, headers=headers, data = payload)
    

    response = requests.request("GET", url)
    txtCokkies = str(response.cookies.values)
    print(requests.cookies.RequestsCookieJar.values)
    print ("---------------------ANTIGO----------------------------------")    

    #print(txtCokkies)    

    print ("---------------------novo----------------------------------")    
    txtCokkies = str(response.cookies.get_dict())
    print(txtCokkies)    
    print(response.cookies["ARRAffinity"])          #mais correto 
    
    print("HEADERS")
    txtCokkies = str(response.headers)
    print(txtCokkies)    


#    print(response.cookies["ASP.NET_SessionId"])
    #response = requests.cookies.extract_cookies_to_jar["ASP.NET_SessionId"]
    
    print(response.cookies.extract_cookies["ASP.NET_SessionId"])
    response.cookies.get_policy
#    print("TEXT")
#    txtCokkies = str(response.text)
#    print(txtCokkies)    


#CarregarCreateLimpo()
#login()
#cokkie()
#cokkieSession()
login1()
