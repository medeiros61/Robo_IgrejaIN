#py excluiarquivos.py
#py converterXLStoCSV.py
#py main_v3.py
#C:\projetos\datavix\robo\digitadorIN\venv4_win\Scripts\deactivate.bat

import csv
import os 
import time
import requests
import re
from datetime import datetime

data_inicio = datetime.now()
varARRAffinity="db03eb84b94e0e75cae00ae6b694f97e17266ab17f2e71cbe1ff54140ff5b6ec"
varSessionID="qzkoc54qvbejjkossljycute"
varAspxauth="8232FEC96CA7E3A2FC1531BA8F2E25501C26334B546C38B780D6E22BC0F8930B147378B6CF4FD506FBC73C716008E86C19B6B2B19DBCC342AB591DC949CF683322757FDC6DF511276BB69612E7A7EE0A3C2ADEFCED4AACC3AC19C4384EDAD26C9D7A6336097C186365FEDB33636641ADC6222104E1FF031451F93A286B0BDC77F7D962AABCB01FF7365CD0914EAAA7A663DB6FCCE12B89ACC824A7B02D1D8EB24BFA71E3AF09F12092ECB670AF309F5D"


#varARRAffinity="dc5ae3a07547a86cc44690165a56c0c39dfa24c118f982d37f22b06427a75573"
#varSessionID="sbajcu5iw43m44qg2xxueajj"
#varAspxauth="9F4C7038F332FB377EDE368889084524F11CDA887ECA64FAC41102DBC48671D1C4C3374888183715B50F23CEC49C7BEF45E715A5DF03B0033DFD540A5A20F440E27D8ED25CB417680C88C013D8766D089AE46E135BF26019661215A2950AD6FD3FF8057B595F3075FE416ED4B2195E1A29E1D01C44F55B524CC05127ECDFB886467D25717E8FED4D299D063C02B17F411206AE1B7E8EF58A7CDD1D05CB2780FD46654D0F75BFBA76EE2EA70AF283EB11"

#'Cookie': 'ARRAffinity=cb1d004228e5e638cf6f288f7672a0c4c4fb23b09c8f14e08ab3cbc6d50ef4f2; 
#ASP.NET_SessionId=c1faka2otz4mkluva0tnqkv5; 
#.ASPXAUTH=12645A66ECE7555BD4B6C6B3FB9C3B2A323013FF456823FA765E3DE182A1C6F49F9B48A0B9D5A75306C1B96C91AEA5BEF8C61F665CDF56CEBBABBFA664C7A80140B58A404BA704216800ECF0B575A92167F2348CC5771936C17BAFFAF0F0A8C1D48D14145B9FFFEFE713A66BC4596F8C324AB40163EA0B4239E4876C00E30969AE87C3131518A423276703B63662CD479624BCD91A5651AFE35528C2CCF1080F9381D1DB84FDCC558AB697C1CB0A20E7'


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
#    print('AQUI')
#    print(Data)
#    print(mes)
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
    #print("Procura : "+ Procura)
    for index, item in enumerate(Lista):
        #test = format(">95" in item)
        #print(item + " Procura -> " + Procura)

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

    response = requests.request("GET", url, headers=headers, data = payload)
    texto = response.text #.encode('utf8')
    txt = "<option value=(.+?)</option>"
    txt = "<option value=(.+?)</option>"
    txt = 'value=(.*)</option>'
    x = re.findall(txt, texto)

    v_Igreja = ">" + v_Igreja
    print('---------')
#    print(x)

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

    response = requests.request("POST", url, headers=headers, data = payload)

    #print(response.text.encode('utf8'))
    print("payload")
    ##print(url)
    ##print(headers)
    print(payload)
    #print(payload1)


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
            #mes = mes[-11:]
            #print("aqui 1:" + mes)
            igreja = igreja[8:]    #rever aqui

            #
            #print("Igreja :" + igreja)
            idEntidade= RetIdIgreja(igreja)
            print(idEntidade)
            if idEntidade == None:
                print("Erro RetIdIgreja" + igreja)
                Erro = "True"
                break

            continue
        else:  # as demais linhas

            Data = linha[8]
            #print(Data)
            #os.system("pause")

            #DataNova = int(xldate_to_datetime(Data))
            #print(DataNova)
        
 
            #print(linha)
            Dizimo = linha[2]
            #print(Dizimo)
            OfertasGerais = linha[3]
            #print(OfertasGerais)
            OfertasEspeciais = linha[4]
            #print(OfertasEspeciais)
            OfertasMissoes = linha[5]
            #print(OfertasMissoes)
            OutrasOfertas = linha[6]
            #print(OutrasOfertas)

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
                    #print("Mes 1 : " + mes)
                    MesAno = RetNumMes(mes)                #periodo
                    #print("MesAno 2 : " + MesAno)
                    if MesAno[:13] == "#errRetNumMes":
                        print("Erro :" + mes)
                        break

                    Dia = Data[:2]              #dia
                    #print(Data[11:])
                    #Horas = TratarHoras(Data[11:])              #HORARIO
                    Horas = Data[11:]                             #HORARIO

                    #print(Horas)
                    #Dizimo='{:5.2f}'.format(nDizimo)
                    #OfertasGerais='{:5.2f}'.format(nOfertasGerais)
                    #OfertasEspeciais ='{:5.2f}'.format(nOfertasEspeciais)
                    #OutrasOfertas ='{:5.2f}'.format(nOutrasOfertas)
                    #OfertasMissoes ='{:5.2f}'.format(nOfertasMissoes)


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


path = 'C:/projetos/datavix/robo/digitadorIN/csv'
pathDestino = 'C:/projetos/datavix/robo/digitadorIN/lidas'
#path = 'P:/planilhas'
#pathDestino = 'P:/lidas'
Erro = "False"
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

        #print(ArquivoCSVDestino)


print("Processo Finalizado")
data_fim = datetime.now()

data_inicio_texto = data_inicio.strftime('%d/%m/%Y %H:%M:%S')
data_fim_texto = data_fim.strftime('%d/%m/%Y %H:%M:%S')

print(data_inicio_texto)
print(data_fim_texto)


#fim



