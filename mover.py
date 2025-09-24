import time, datetime

import os 

#os.rename('relatorios_01_12_2019_31_12_2019teste.xlsx', '/projetos/datavix/robo/digitador/lidas/lida-relatorios_01_12_2019_31_12_2019teste.xlsx')

def xldate_to_datetime(xldate):
  tempDate = datetime.datetime(1900, 1, 1)
  deltaDays = datetime.timedelta(days=int(xldate))
  secs = (int((xldate%1)*86400)-60)
  detlaSeconds = datetime.timedelta(seconds=secs)
  TheTime = (tempDate + deltaDays + detlaSeconds )
  return TheTime.strftime("%Y-%m-%d %H:%M:%S")

#def teste(msgg):
#    print(msgg)


#path = 'C:/projetos/datavix/robo/digitador'
#for p, _, files in os.walk(os.path.abspath(path)):
#    for file in files: 
#        print(os.path.join(p, file))
#        teste("rerere")

DataNova = xldate_to_datetime(43800.7916666667)
print(DataNova)


