import os

def Excluir(path):
    dir = os.listdir(path)
    print("Exclusão : " + path )
    cont = 0 
    for file in dir:
        print(file)
        #os.remove(file)
        os.remove('{}/{}'.format(path, file))        
        cont = cont +1

    print('Total excluidos : ' + str(cont))

#C:\projetos\datavix\robo\digitadorIN\lidas
#C:\projetos\datavix\robo\digitadorIN\lidasXLS
Excluir('C:/projetos/datavix/robo/digitadorIN/lidas')
Excluir('C:/projetos/datavix/robo/digitadorIN/lidasXLS')


