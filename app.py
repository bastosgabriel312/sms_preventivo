import PySimpleGUI as sg
from pandas_back import *



data = d_mais_um().strftime("%d.%m")

#Frases SMS 
frase_sp1 = 'SEU COMPROMISSO COM SEM PARAR VENCE HOJE! Devido atual cenario de preferencia aos canais digitais, APP e Internet Banking. Tel 40202350 Whats 11 969180729.'
frase_sp2 = "SEU COMPROMISSO COM O SEM PARAR VENCE DIA "+data+"!Devido atual cenario de preferencia aos canais digitais, APP e Internet Banking.Tel.40202350 Whats 11969180729."
frase_ipanema = "SEU COMPROMISSO COM A IPANEMA VENCE HOJE! Devido atual cenario de preferencia aos canais digitais, APP e Internet Banking. Tel 08000258961 Whats 11 961731064."
frase_ipanemad1 = "SEU COMPROMISSO COM A IPANEMA VENCE DIA "+data+"!Devido atual cenario de preferencia aos canais digitais, APP e Internet Banking.Tel.40202350 Whats 11969180729."

#formatação de data atual concatenada (DiaMesAno)
hoje = date.today()
hoje = hoje.strftime("%d%m%Y")

#Define Tema
sg.theme('DarkGrey4') 

# Define os conteúdos no layout 
layout = [[sg.Text(('CONVERSOR SMS'), size=(20, 1), justification='center', font=('Courier 12', 25))],
            #FRAME 1 - FRASES
            [sg.Frame(layout=[[sg.Radio('   Sem parar', "RADIO1",key='semparar', default=True, size=(15,1))],
            [sg.Radio('Sem parar D+1', "RADIO1",key='semparard1')],
            [sg.Radio('Ipanema', "RADIO1",key='ipanema')],
            [sg.Radio('Ipanema D+1', "RADIO1",key='ipanemad1')],
            [sg.Radio("Outro: ","RADIO1", key='rdoutro'), sg.Input(key='outro', size=(41,1))]],
                title='Frase',title_color='red', size=(41,1))],
        
            #FRAME 2 - ARQUIVO
            [sg.Frame(layout=[
                [sg.Input(size=(31,1),key='carquivo'), sg.FileBrowse(key='arquivo')],
                [sg.Text('Exportar:'),
                    sg.Radio('.txt',"RADIO3", key='txt', size=(3,5)),
                    sg.Radio('.csv',"RADIO3",  key='csv', default=True, size=(27,5)) ],
            [sg.FolderBrowse(initial_folder ='/' , button_text = "Selecionar Pasta", key='export'),sg.Text(size=(30,1), key='-OUTPUT-')]],
            title='Arquivo', title_color = 'red')],
            [sg.Button('Ok'), sg.Button('Sair')]]

          
#Criar layout da tela
window = sg.Window('Arquivo SMS', layout)

# Looping para interações na tela do app
while True:
    event, values = window.read()
    # Ver quando a janela é fechada ou o evento é sair
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    # Output a message to the window
    if event == 'Ok':
        #Visualização de eventos utilizados
        '''
        print('Semparar: ',values['semparar'])
        print('Semparar D+1: ',values['semparard1'])
        print('ipanema: ',values['ipanema'])
        print('ipanema D+1: ',values['ipanemad1'])
        print('Outro: ',values['rdoutro'])
        print('Input outro: ',values['outro'])  
        print('Arquivo browse: ',values['arquivo'])
        print('Arquivo input: ',values['carquivo'])
        print('Txt: ',values['txt'])
        print('csv: ',values['csv'])
        print('arquivo export', values['export'])
        '''

        #Verifica se o campo de arquivo é diferente de vazio        
        if values['arquivo']!='':
            #Verifica se o valor selecionado txt e atribui a variavel tipo
            if values['txt']:
                tipo = 'txt'
            #Verifica se o valor selecionado csv e atribui a variavel tipo caso não seja 'txt'
            elif values['csv']:
                tipo = 'csv'
            #Veriica qual o layout/frase escolhido
            if values['semparar']:
                nome_arquivo = ""+hoje+"_PREVENTIVA_SEMPARAR_SHORT_1"
                #Função de tratamento de dataset Sms Sem Parar proveniente de pandas_back
                dataset = sms_semparar(values['arquivo'],frase_sp1)
                #Função exportar dados proveniente de pandas_back
                exportar_dados(dataset, nome_arquivo, tipo,values['export'])
                sg.popup("Arquivo Exportado!!")
            elif values['semparard1']:
                nome_arquivo = ""+hoje+"_PREVENTIVA_SEMPARAR_SHORT_2"
                #Função de tratamento de dataset Sms Sem Parar proveniente de pandas_back
                dataset = sms_semparar(values['arquivo'],frase_sp2)
                #Função exportar dados proveniente de pandas_back
                exportar_dados(dataset, nome_arquivo,tipo,values['export'])
                sg.popup("Arquivo Exportado!!")
            elif values['ipanema']:
                nome_arquivo = ""+hoje+"_PREVENTIVA_IPANEMA_SHORT"
                #Função de tratamento de dataset Sms Ipanema proveniente de pandas_back
                dataset = sms_ipanema(values['arquivo'],frase_ipanema)
                #Função exportar dados proveniente de pandas_back
                exportar_dados(dataset, nome_arquivo,tipo,values['export'])
                sg.popup("Arquivo Exportado!!")
            elif values['ipanemad1']:
                nome_arquivo = ""+hoje+"_PREVENTIVA_IPANEMA_SHORT_2"
                #Função de tratamento de dataset Sms Ipanema proveniente de pandas_back
                dataset = sms_ipanema(values['arquivo'],frase_ipanemad1)
                #Função exportar dados proveniente de pandas_back
                exportar_dados(dataset, nome_arquivo,tipo,values['export'])
                sg.popup("Arquivo Exportado!!")
            elif values['rdoutro']:
                nome_arquivo = ""+hoje+"_SMS"
                #Função de tratamento de dataset Sms Sem Parar proveniente de pandas_back
                dataset = sms_semparar(values['arquivo'],values['outro'])
                #Função exportar dados proveniente de pandas_back
                exportar_dados(dataset, nome_arquivo,tipo,values['export'])
                sg.popup("Arquivo Exportado!!")
            #Output que aparece assim que a pasta destino do arquivo exportado é escolhida
            values['-OUTPUT-'] = values['export']

                    
            
                
                
                
#Fechar janela (caso saia do looping)       
window.close()
