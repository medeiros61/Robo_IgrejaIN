import os
import xlrd
#xlrd==1.2.0
import csv
from datetime import date, timedelta, datetime


def AbrirXLS(ArquivoXLS, pathDestinoCSV, ArquivoCSV):

#    print(ArquivoXLS )
#    print(pathDestinoCSV + ArquivoCSV )
#    print("---------------------------------")
    Saidas = False
    wb = xlrd.open_workbook(ArquivoXLS)
    sh = wb.sheet_by_index(0)
    
    pathDestinoSaida = 'C:\\projetos\\datavix\\robo\\digitadorOUT\\excel\\' ## Linha nova 

    ArquivoSaidas = pathDestinoSaida + ArquivoCSV.replace('csv','xlsx') ## Linha nova 

    
    ArquivoCSV = pathDestinoCSV + ArquivoCSV
    your_csv_file = open(ArquivoCSV, 'w')

    wr = csv.writer(your_csv_file, delimiter=';', quoting=csv.QUOTE_NONE, lineterminator = '\n', dialect = 'excel')
#    wr = csv.writer(your_csv_file, delimiter=';', quoting=csv.QUOTE_NONE, lineterminator = '\n', escapechar='\\')

    gravaLinha = "S"
    for rownum in range(sh.nrows):

        vLinha = sh.row_values(rownum)
        if 'CONTA CREDITO (Codigo Site)' in vLinha:## Linha nova para saidas 
           
            wb.release_resources()## Linha nova 
            os.rename(ArquivoXLS,ArquivoSaidas)## Linha nova 
            print(f'Arquivo de Saidas movido {ArquivoXLS} para {ArquivoSaidas}')
            Saidas = True
            break## Linha nova 
            
        if rownum < 2:
            #print(sh.cell_value(rowx=rownum, colx=1))
            vLinha = vLinha+["data1"]
            gravaLinha = "S"

        if rownum >= 2 and  sh.cell_value(rowx=rownum, colx=0) != 'TOTAIS:':
            #if sh.cell_value(rowx=rownum, colx=0)==5429392.0: 
            #    print(sh.cell_value(rowx=rownum, colx=0))
            data1 = sh.cell_value(rowx=rownum, colx=1)
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(data1, wb.datemode)
            vData1 = str(year) + '-' + str(month) + '-' + str(day) + ' ' + str(hour) + ':' + str(minute) #+ ':' + str(second)
            vData1 = datetime.strptime(vData1, '%Y-%m-%d %H:%M') 
            vData1F = vData1.strftime('%d/%m/%Y %H:%M')
            vLinha = vLinha+[vData1F]

            Dizimos = sh.cell_value(rowx=rownum, colx=2)
            Ofertas_Gerais = sh.cell_value(rowx=rownum, colx=3)
            Ofertas_Especiais = sh.cell_value(rowx=rownum, colx=4)
            Ofertas_Missões = sh.cell_value(rowx=rownum, colx=5)
            Outras_Ofertas = sh.cell_value(rowx=rownum, colx=6)
            TotalLinha = Dizimos + Ofertas_Gerais + Ofertas_Especiais + Ofertas_Missões + Outras_Ofertas
            print(TotalLinha)
            gravaLinha = "S"

            if TotalLinha == 0:
                gravaLinha = "N"

        if rownum >= 2 and sh.cell_value(rowx=rownum, colx=0) == 'TOTAIS:':
            #print(sh.cell_value(rowx=rownum, colx=1))
            vLinha = vLinha+[""]
            gravaLinha = "N"            

        if gravaLinha == "S":
            wr.writerow(vLinha)

    your_csv_file.close()  #- fecha arquivo csv
    if Saidas:
        return False
    else:
        return True


def converterXLStoCSV():    
    #ler arquivos até o fim 
    #path = 'C:/projetos/datavix/robo/digitadorIN/planilhas'
    #pathDestino = 'C:/projetos/datavix/robo/digitadorIN/lidas'

    pathDestinoCSV = 'C:/projetos/datavix/robo/digitadorIN/csv/'
    path = 'C:\\projetos\\datavix\\robo\\digitadorIN\\planilhasPART1'
    pathDestinoXLS = 'C:/projetos/datavix/robo/digitadorIN/lidasXLS/'
    
#    path = input("Entre com a pasta: ")
    #print(path)
    if path == "" or path == "1":
        path = 'C:\\projetos\\datavix\\robo\\digitadorIN\\planilhasPART1'

    if path == "2":
        path = 'C:\\projetos\\datavix\\robo\\digitadorIN\\planilhasPART2'

    if path == "3":
        path = 'C:\\projetos\\datavix\\robo\\digitadorIN\\planilhasPART3'

    if path == "4":
        path = 'C:\\projetos\\datavix\\robo\\digitadorIN\\planilhasPART4'

    if path == "5":
        path = 'C:\\projetos\\datavix\\robo\\digitadorIN\\planilhasPART5'


    cont = 0 
    for p, _, files in os.walk(os.path.abspath(path)):
        for file in files: 
            print(os.path.join(p, file))

            ArquivoCSV = file[:-5] + ".csv"
            Entrada = AbrirXLS(os.path.join(p, file), pathDestinoCSV, ArquivoCSV) 
            if Entrada:
                #terminar aqui 
                os.rename(path + "/" + file, pathDestinoXLS + file)
                cont = cont + 1
                #print(path + "/" + file + "----" + pathDestinoXLS + file)
                print("Movendo arquivo--> " + pathDestinoXLS + file)

    print("Total de aqrquivos processados " + str(cont)) 

#converterXLStoCSV()   #executa função

