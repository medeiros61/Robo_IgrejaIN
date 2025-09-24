import os 
import xlrd
from pynput.keyboard import Key, Controller 
import time, datetime


def xldate_to_datetime(xldate):
  tempDate = datetime.datetime(1900, 1, 1)
  deltaDays = datetime.timedelta(days=int(xldate))
  secs = (int((xldate%1)*86400)-60)
  detlaSeconds = datetime.timedelta(seconds=secs)
  TheTime = (tempDate + deltaDays + detlaSeconds )
  return TheTime.strftime("%Y-%m-%d %H:%M:%S")


def LERARQUIVO(ArquivoExcel):
    #import os 
    #import xlrd
    #from pynput.keyboard import Key, Controller 
    #import time

    #workbook = xlrd.open_workbook('relatorios_01_12_2019_31_12_2019teste.xlsx')
    #workbook = xlrd.open_workbook('relatorios_01_12_2019_31_12_2019 (2).xlsx')
    workbook = xlrd.open_workbook(ArquivoExcel)

    teclado = Controller()
    time.sleep(1)

    worksheet = workbook.sheet_by_index(0)
    #cont = 1

    for row_num in range(worksheet.nrows):
        #row = worksheet.row_values(row_num)
        if row_num == 0:  # se for a 1 linha

            igreja = str(worksheet.cell_value(row_num, 0))
            mes = worksheet.cell_value(row_num, 4)
            igreja = igreja[8:]
            mes = mes[8:]
            #print(igreja)
            #print(mes)

            continue
        else:  # as demais linhas

            Data = worksheet.cell_value(row_num, 1)
            print(Data)
            
            #DataNova = int(xldate_to_datetime(Data))
            #print(DataNova)
        

            #print(Data)
            Dizimo = str(worksheet.cell_value(row_num, 2))
            OfertasGerais = str(worksheet.cell_value(row_num, 3))
            OfertasEspeciais = str(worksheet.cell_value(row_num, 4))
            OfertasMissoes = str(worksheet.cell_value(row_num, 5))
            OutrasOfertas = str(worksheet.cell_value(row_num, 6))

            #Dizimo = Dizimo.replace(".",",")
            #OfertasGerais = OfertasGerais.replace(".",",") 
            #OfertasEspeciais = OfertasEspeciais.replace(".",",")
            #OfertasMissoes = OfertasMissoes.replace(".",",") 
            #OutrasOfertas = OutrasOfertas.replace(".",",") 

            if row_num > 1 :   # se for a 1 linha
                #Soma = OfertasGerais + int(OfertasEspeciais) + int(OfertasMissoes) + int(OutrasOfertas)
                #Soma = float(Dizimo) + float(OfertasGerais) # + OfertasEspeciais  + OfertasMissoes + OutrasOfertas
                #Soma = 123,22+123,22
                #print("Soma4")

                #if Soma > 0 :
                #print(worksheet.cell_value(row_num, 2))

                #time.sleep(2)
                # controlar teclado
                #print('teclado v1')
                #print(Data)

                #teclado.pressed([Key.ctrl, Key.esc])
                if Data != "": # desconsiderar ultima linha 
                    teclado.press(Key.tab)
                    teclado.release(Key.tab)

                    time.sleep(1)
                    teclado.type(igreja)
                    teclado.press(Key.tab)
                    teclado.release(Key.tab)

                    teclado.type(mes)
                    teclado.press(Key.tab)
                    teclado.release(Key.tab)

                    #teclado.type(Data[:2])
                    teclado.type(str(Data))

                    teclado.press(Key.tab)
                    teclado.release(Key.tab)

                    #teclado.type(Data[12:])
                    teclado.type(str(Data))
                    teclado.press(Key.tab)
                    teclado.release(Key.tab)

                    time.sleep(0.5)

                    teclado.type(Dizimo)
                    teclado.press(Key.tab)
                    teclado.release(Key.tab)

                    teclado.type(OfertasGerais)
                    teclado.press(Key.tab)
                    teclado.release(Key.tab)

                    teclado.type(OfertasEspeciais)
                    teclado.press(Key.tab)
                    teclado.release(Key.tab)
                    time.sleep(0.5)

                    teclado.type(OfertasMissoes)
                    teclado.press(Key.tab)
                    teclado.release(Key.tab)
                    time.sleep(0.5)

                    teclado.type(OutrasOfertas)
                    teclado.press(Key.tab)
                    teclado.release(Key.tab)
                    #time.sleep(1)

                    teclado.press(Key.enter)
                    teclado.release(Key.enter)
                    #time.sleep(1)

                    teclado.press(Key.enter)
                    teclado.release(Key.enter)

                    time.sleep(4)
                    print('pr.')
            

    workbook.release_resources()
    del workbook

    # Movendo e renomeando com os.rename
    #os.rename('diretorio/origem/nome-arquivo', 'diretorio/destino/novo-nome-arquivo')
    #print(str(cont) + ' Total')
    print('Fim arquivo : ' + ArquivoExcel)



path = 'C:/projetos/datavix/robo/digitador/planilhas'
pathDestino = 'C:/projetos/datavix/robo/digitador/lidas'
print('inicio em  1')
time.sleep(1)
print('inicio em  2')
time.sleep(1)
print('inicio em  3')
time.sleep(1)
print('inicio em  4')
time.sleep(1)
print('inicio em  5')
time.sleep(1)


for p, _, files in os.walk(os.path.abspath(path)):
    for file in files: 
        #print(os.path.join(p, file))
        ArquivoExcel = os.path.join(p, file)
        ArquivoExcelDestino = pathDestino +'/'+ file
        LERARQUIVO(ArquivoExcel)
        os.rename(ArquivoExcel, ArquivoExcelDestino)
        #print(ArquivoExcel)
        print(ArquivoExcelDestino)

print("Processo Finalizado")


#fim



