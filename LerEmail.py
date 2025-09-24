import main_v5 as main_v5
import converterXLStoCSV as converter

import win32com.client as win32

from pathlib import Path
#https://www.youtube.com/watch?v=kqsX2daN8Dk&t=490s

from datetime import datetime
def main():
    hoje = datetime.now()
    hojestr = hoje.strftime('%d/%m/%Y')

    PastaDestino = "C:/AutoArquivos/igreja/arquivos/"
    PastaDestino = "C:/projetos/datavix/robo/digitadorIN/planilhasPART1/"
    print('INICIO - ler email')

#    destino = Path.cwd() / "output"
#    destino.mkdir(parents=True, exist_ok=True)

    outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")

    inbox = outlook.GetdefaultFolder(6)
    #inbox = outlook.Folders("contato@datavigital.com.br").Folders("Inbox")
    messages = inbox.items


    for m in messages:
        subject = m.Subject
        anexo = m.Attachments
        conteudo = m.body
        data = m.ReceivedTime.strftime("%d/%m/%Y")
        if data == hojestr:
            print(data)
            print(subject)
            if subject.lower().find('regiao') >0 or subject.lower().find('seguras') >0:
    #            print(subject)
        #        print(conteudo)
                if subject.lower().find('seguras') >0:
                    print(conteudo)
                    conteudoSplit = conteudo.split("=")
                    print(conteudoSplit[1])
                    print(conteudoSplit[2])
                    print(conteudoSplit[3])

                for att in anexo:
                    print(str(att))
                    nomeArq=str(att)
                    if nomeArq.lower().find('xlsx') >0:
                        hoje = datetime.now()
                        millisec = int(hoje.timestamp() * 1000)
                        att.SaveAsFile(PastaDestino + str(millisec)+ str(att))

    print('Arquivos Baixados')

    print('Chamada para CONVERTER arquivos')
    converter.converterXLStoCSV()

    print('Chamada para SUBMETER LionTech arquivos')
    main_v5.Inicio()

main()


      