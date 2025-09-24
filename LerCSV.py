import csv
import time
from datetime import datetime


#C:\projetos\datavix\robo\digitador\relatorios_01_12_2019_31_12_2019teste.csv
#print __doc__
#planilhas\relatorios_ Jeronimo Monteiro.csv
#C:\projetos\robo\digitador\planilhas

data_inicio = datetime.now()

#f = csv.reader(open("C:/projetos/datavix/robo/digitadorIN/planilhas/relatorios_01_03_2020_31_03_2020 (10).csv"),delimiter=';')
#f = csv.reader(open("C:/projetos/datavix/robo/digitadorIN/planilhas/relatorios_01_03_2020_31_03_2020 (10).csv"),delimiter=';')
f = csv.reader(open("C:/projetos/datavix/robo/digitadorIN/lidas/castelo.csv"),delimiter=';')

time.sleep(2)
for linha in f:
    #print (f.line_num)
    if f.line_num == 1:
        #print (linha)
        igreja = linha[0]
        print(igreja)
        igreja = igreja[10:]
        print(igreja)
    #print (linha[0])
    #print (linha[1])
    #print (linha[2])

print (f.line_num, 'linhas lidas')
print ('--- fim')
data_fim = datetime.now()
data_fim = data_fim.strftime('%d/%m/%Y %H:%M:%S')
data_inicio = data_inicio.strftime('%d/%m/%Y %H:%M:%S')


print(data_inicio)
print(data_fim)
