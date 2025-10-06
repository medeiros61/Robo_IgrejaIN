#py excluiarquivos.py
#py converterXLStoCSV.py
#py main_v4.py
#C:\projetos\datavix\robo\digitadorIN\venv4_win\Scripts\deactivate.bat

from configparser import ConfigParser
import csv
import os 
import time
import requests
import re
from datetime import datetime
import Parametros as bd_p
#sys.path.insert (0, 'C:\\projetos\\RoboLerEmail')

#import EnviarEmail
import CapturarCoockies as cc

PastaProcessados = os.path.abspath(os.path.join(os.path.dirname(__file__),  "..", "..", "..", "arquivos_robos", "Igreja_processados"))
pathCSV = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "arquivos_robos", "Igreja_CSV"))
config = ConfigParser()

#varARRAffinity="4158b8cb52670287f6c8ed527deabcf61e852bbce20c1d69134187e490db1687	"
#varSessionID="kt2z4ur1f0tb3pxg1et5rjvo		"
#varAspxauth="A377ADE28E10D3FAF8CD1E5C7B22D0B1632F597A238C8551B0670914D0361736857721638E866639B413DB72FE7AE818645D7613A60F106C8FDBAB64252FE5EC97CC1F19D6487A9B7EB55A1377E01F9C60011D6A95788307B9B08E1ED6139889A92921B49075D05AECB2083C0BC71BB41FA0B39724736CF5E8521EDEE27EE4F51763BEC23BEEEAB311162E84C3D0A1B6AE1373349EBA74D9F3784A0BE738E7CE59B582D8C4581A590E552D027E7EE828		"

def TratarHoras(Horas):
    hora = int(Horas[:2])
    if hora < 10:
    #    print('menor')
        Horas = Horas[1:]
    #else:
    #    print("maior")

    #print(Horas)
    return Horas


def RetNumMes(Data):
    #mes = Data[:8]
    mes = Data
    MesAno = "#errRetNumMes"

    if format('JANEIRO' in mes)=="True":
        MesAno = "01/"  

    if format('FEVEREIRO' in mes)=="True":
        MesAno = "02/"  

    if format('MARÇO' in mes)=="True":
        MesAno = "03/"  

    if format('ABRIL' in mes)=="True":
        MesAno = "04/"  

    if format('MAIO' in mes)=="True":           #localizar string
        MesAno = "05/"  

    if format('JUNHO' in mes)=="True":
        MesAno = "06/"  

    if format('JULHO' in mes)=="True":
        MesAno = "07/" 

    if format('AGOSTO' in mes)=="True":
        MesAno = "08/" 

    if format('SETEMBRO' in mes)=="True":
        MesAno = "09/" 

    if format('OUTUBRO' in mes)=="True":
        MesAno = "10/" 

    if format('NOVEMBRO' in mes)=="True":
        MesAno = "11/" 

    if format('DEZEMBRO' in mes)=="True":
        MesAno = "12/" 

    #print("Dentro funcao: "+MesAno)
    #print("ano " + Data[-4:])
    MesAno = MesAno+Data[-4:]    
    #print(Data)
    return MesAno

def ProcuraNaLista(Procura,Lista):
    for index, item in enumerate(Lista):
        Encontrado = format(Procura[1:11] in item)
        #Encontrado = format(Procura in item)
        if Encontrado == "True":
            #print("Encontrado " + str(index) +" "+ item)
            return item[1:6]

def RetIdIgreja(v_Igreja):

    url = "https://www.liontechieq.com.br/RelatorioCulto/Create"

    payload = {}
    #headers = {'Cookie': 'ASP.NET_SessionId=443jzsicvf3whnbiglkze5pv; ARRAffinity=cb1d004228e5e638cf6f288f7672a0c4c4fb23b09c8f14e08ab3cbc6d50ef4f2; .ASPXAUTH=44760D05C5105FECD69D2F882DE0B5EECBB1C22D674FC0EE56A0701AC42375AF40183BECB1883C5F0144BE9E93A752459E344F23A8431E94234DD93DE6427A4159E0D3B15FC80DDC8BBAB36F6286A43A2BC623F39A3B726CC88FA123256B452E22EC3975BE8D6E437B4D7A1757942F643414AA0026FCF1FFCD766C88C5285C385B839981CCA0999442A150D5FBF8A2D37B0CA557EDB119561B5864D0CAC0681A847BB50EB368633F1EA891DFDFA44458'}
    headers = {'Cookie': 'ASP.NET_SessionId='+ varSessionID + '; ARRAffinity='+ varARRAffinity +'; .ASPXAUTH=' + varAspxauth}
    time.sleep(2)
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.request("GET", url, headers=headers, data=payload, timeout=40)
            break
        except Exception as e:
            print(f"Erro ao fazer requisição: {e}")
            if attempt < max_retries - 1:
                print("Tentando novamente em 2 minutos...")
                time.sleep(120)
            else:
                print("Falha após múltiplas tentativas.")
                return None

    texto = response.text #.encode('utf8')
    txt = "<option value=(.+?)</option>"
    txt = "<option value=(.+?)</option>"
    txt = 'value=(.*)</option>'
    x = re.findall(txt, texto)

    v_Igreja = ">" + v_Igreja
    print('---------')

    #print("Resultado lista : "+ProcuraNaLista(v_Igreja,x))
    ID = ProcuraNaLista(v_Igreja,x)

    return ID


def LancamentoValores(v_Dia, v_Hora, v_ID_Entidade,v_Dizimos, v_OfertaMissoes, v_OfertasEspeciais, v_OfertasGerais, v_OutrasEntradas, v_Periodo):

    #payload = 'Dia=13&Dizimos=20,50&Hora=20%3A30&ID_Entidade=51993&OfertaMissoes=21,54&OfertasEspeciais=22,33&OfertasGerais=0%2C02&OutrasEntradas=0%2C04&Periodo=04/2020'
    payload = 'Dia=' + v_Dia + '&Dizimos=' + str(v_Dizimos) + '&Hora=' + str(v_Hora) + '&ID_Entidade=' + str(v_ID_Entidade) + '&OfertaMissoes=' + str(v_OfertaMissoes) + '&OfertasEspeciais=' + str(v_OfertasEspeciais) + '&OfertasGerais=' + str(v_OfertasGerais) + '&OutrasEntradas=' + str(v_OutrasEntradas) + '&Periodo=' + v_Periodo  

    #***************************************************************
    url = "https://www.liontechieq.com.br/RelatorioCulto/Create"

    #payload1 = 'Dia=05&Dizimos=420%2C99&Hora=20%3A30&ID_Entidade=52030&OfertaMissoes=12%2C12&OfertasEspeciais=12%2C123&OfertasGerais=0&OutrasEntradas=0&Periodo=04/2020'
    headers = {
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.liontechieq.com.br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ASP.NET_SessionId='+ varSessionID + '; ARRAffinity='+ varARRAffinity +'; .ASPXAUTH=' + varAspxauth}
    #'Cookie': 'ASP.NET_SessionId=443jzsicvf3whnbiglkze5pv; ARRAffinity=cb1d004228e5e638cf6f288f7672a0c4c4fb23b09c8f14e08ab3cbc6d50ef4f2; .ASPXAUTH=44760D05C5105FECD69D2F882DE0B5EECBB1C22D674FC0EE56A0701AC42375AF40183BECB1883C5F0144BE9E93A752459E344F23A8431E94234DD93DE6427A4159E0D3B15FC80DDC8BBAB36F6286A43A2BC623F39A3B726CC88FA123256B452E22EC3975BE8D6E437B4D7A1757942F643414AA0026FCF1FFCD766C88C5285C385B839981CCA0999442A150D5FBF8A2D37B0CA557EDB119561B5864D0CAC0681A847BB50EB368633F1EA891DFDFA44458'
    time.sleep(2)
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = requests.request("POST", url, headers=headers, data=payload, timeout=40)
            break
        except Exception as e:
            print(f"Erro ao fazer requisição: {e}")
            if attempt < max_retries - 1:
                print("Tentando novamente em 1 minuto...")
                time.sleep(60)
            else:
                print("Falha após múltiplas tentativas.")
                return
    
#    print('NÃO lançar valores por enquanto (TESTE)')
    print("Gravado Produção")
    #print(payload)


def LERARQUIVO(ArquivoCSV):
    global Erro
    #f = csv.reader(open(ArquivoCSV,encoding='utf-8'), delimiter=';')
    f = csv.reader(open(ArquivoCSV), delimiter=';')

    #cont = 1
    #linha = 0
    for linha in f:
        print('-------------------------------' + str(f.line_num))
        print (linha)

        if f.line_num == 1:  # se for a 1 linha

            igreja = linha[0]
            mes = linha[4]
            igreja = igreja[8:]    #rever aqui

            idEntidade= RetIdIgreja(igreja)
            #print(idEntidade)
            if idEntidade == None:
                print("Erro RetIdIgreja" + igreja)
                Erro = "True"
                break

            continue
        else:  # as demais linhas

            Data = linha[8]
            Dizimo = linha[2]
            OfertasGerais = linha[3]
            OfertasEspeciais = linha[4]
            OfertasMissoes = linha[5]
            OutrasOfertas = linha[6]

            Dizimo = Dizimo.replace(".",",")
            OfertasGerais = OfertasGerais.replace(".",",") 
            OfertasEspeciais = OfertasEspeciais.replace(".",",")
            OfertasMissoes = OfertasMissoes.replace(".",",") 
            OutrasOfertas = OutrasOfertas.replace(".",",") 

            if f.line_num > 2 :   # se for a 1 linha
                #teclado.pressed([Key.ctrl, Key.esc])
                Soma = float(0)
                nDizimo = float(Dizimo.replace(",","."))
                nOfertasGerais = float(OfertasGerais.replace(",","."))
                nOfertasEspeciais = float(OfertasEspeciais.replace(",",".")) 
                nOfertasMissoes = float(OfertasMissoes.replace(",",".")) 
                nOutrasOfertas = float(OutrasOfertas.replace(",","."))
                Soma = nDizimo + nOfertasGerais + nOfertasEspeciais + nOfertasMissoes + nOutrasOfertas
                #
                if Data != "" and Soma > 0: # desconsiderar ultima linha 

                    mes = mes.strip()
                    MesAno = RetNumMes(mes)                #periodo
                    if MesAno[:13] == "#errRetNumMes":
                        print("Erro :" + mes)
                        break

                    Dia = Data[:2]              #dia
                    Horas = Data[11:]                             #HORARIO

                    LancamentoValores(Dia, Horas, idEntidade, Dizimo, OfertasMissoes, OfertasEspeciais, OfertasGerais, OutrasOfertas, MesAno)
                    #lancar aqui ()
                    time.sleep(1.2)
            

    print('Fim arquivo : ' + ArquivoCSV)
    time.sleep(1)
    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('ATENÇÃO TROCA DE ARQUIVO')

def Inicio():
    
    global varARRAffinity
    global varSessionID
    global varAspxauth
    global ultAtualizacao,data_inicio_ddmmyyyy,caminhoConfig

    caminhoConfig = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.ini"))
    config.read(caminhoConfig)

    data_inicio = datetime.now()
    ultAtualizacao=config.get("default","UltAtualizacao")
    varARRAffinity=config.get("default","ARRAffinity")
    varSessionID=config.get("default","SessionID")
    varAspxauth=config.get("default","Aspxauth")

    path = pathCSV
    pathDestino = PastaProcessados
    print(path)
    #path = 'P:/planilhas'
    #pathDestino = 'P:/lidas'
    Erro = "False"
    data_inicio_ddmmyyyy = data_inicio.strftime('%d/%m/%Y')

    if ultAtualizacao==data_inicio_ddmmyyyy:
        for p, _, files in os.walk(os.path.abspath(path)):
            for file in files: 
                #print(os.path.join(p, file))
                ArquivoCSV = os.path.join(p, file)
                ArquivoCSVDestino = pathDestino +'/'+ file
                print(ArquivoCSV)
                if Erro == "False":
                    LERARQUIVO(ArquivoCSV)
                    if Erro == "True":
                        break
                    os.rename(ArquivoCSV, ArquivoCSVDestino)
#        print("Processo Finalizado")
        data_fim = datetime.now()
        data_inicio_texto = data_inicio.strftime('%d/%m/%Y %H:%M:%S')
        data_fim_texto = data_fim.strftime('%d/%m/%Y %H:%M:%S')
#        print(data_inicio_texto)
#        print(data_fim_texto)
    else:
        for p, _, files in os.walk(os.path.abspath(path)):
            for file in files:
                print("**************************************")
                print("** CHAVES DE ACESSO DESATUALIZADAS! **")
                print("**************************************")
                cc.Peguaroscoockies(caminhoConfig)
                data_fim = datetime.now()
                data_fim_texto = data_fim.strftime('%d/%m/%Y %H:%M:%S')
                print("atualizado")
                print(data_fim_texto)
                break        

def rotinasms():
    
    try:
        bd_p.Atualizar_Parametro('robo_igrejas', 'ativo')
    except Exception as e:
        Horario_ErroBD = datetime.now()
        Horario_ErroBD_texto = Horario_ErroBD.strftime('%d/%m/%Y %H:%M:%S')
        print(f'[{Horario_ErroBD_texto}] Ocorreu um erro ao atualizar Banco de dados(King Host) : {e}')    
        print(f'Continuando Execução...')
        
def atualizar_cookies_BD():
    try:
        atualizar = bd_p.pegar_parametro('igreja_cookies_pedido_att')
        if atualizar =='sim':
            if ultAtualizacao==data_inicio_ddmmyyyy:
                
                bd_p.Atualizar_Parametro('igreja_cookies_data_att', f'{ultAtualizacao}')
                bd_p.Atualizar_Parametro('igreja_ARRAffinity', f'{varARRAffinity}')
                bd_p.Atualizar_Parametro('igreja_SessionID', f'{varSessionID}')
                bd_p.Atualizar_Parametro('igreja_Aspxauth',f'{varAspxauth}')
                bd_p.Atualizar_Parametro('igreja_cookies_pedido_att', 'nao')
                print("Solicitação externa para atualizar os cookies concluida")
            else:
                print("Atualizando Cookies...")
                cc.Peguaroscoockies(caminhoConfig)
    except Exception as e:
        pass   
            
while True:
#    print("**************************************")
#    print("**   INICIO  PROCESSO  LIONTECH  !  **")
#    print("**************************************")

    Inicio()
#    rotinasms()
    #atualizar_cookies_BD()
    for i in range(60, 0, -1):
        print(f"Aguardando {i} segundos...", end='\r')
        time.sleep(1)
    print(" " * 30, end='\r')  # limpa a linha

#fim



