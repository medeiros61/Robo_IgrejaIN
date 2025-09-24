#C:\projetos\datavix\robo\digitadorIN\venvRoboIN\Scripts\activate.bat
#C:\projetos\datavix\robo\digitadorIN\venvRoboIN\Scripts\deactivate.bat
import PySimpleGUI as sg

def inicio():
    sg.theme('DarkGrey2')  # please make your creations colorful

    layout = [  [sg.Text('ARRAffinity'),sg.Input(size=(15,0), key='ARRAffinity')],
                [sg.Text('SessionID'),sg.Input(size=(15,0), key='SessionID')],
                [sg.Text('Aspxauth'),sg.Input(size=(15,0), key='Aspxauth')], 
                [sg.OK(), sg.Cancel()]] 
    window = sg.Window('TOKEN DE AUTORIZAÇÃO', layout)
    v = True
    while v==True:
        event, values = window.read()
        print(event)
        print(values)
        if event =='Cancel':
            v = False 
            window.close()
        if event == 'OK':  
            print('tese')  
            v = False 


inicio()

