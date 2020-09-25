from arquivo_sms import *

data = d_mais_um().strftime("%d.%m")
frase_sp1 = 'SEU COMPROMISSO COM SEM PARAR VENCE HOJE! Devido atual cenario de preferencia aos canais digitais, APP e Internet Banking. Tel 40202350 Whats 11 969180729.'
frase_sp2 = "SEU COMPROMISSO COM O SEM PARAR VENCE DIA "+data+"!Devido atual cenario de preferencia aos canais digitais, APP e Internet Banking.Tel.40202350 Whats 11969180729."

#sms_semparar('sms',frase_sp1)
print("ENVIO DE BOLETO VIA SMS \n")
print("ESCOLHA UMA OPÇÃO: \n 1. Sem Parar \n 2. Sem Parar D+1 \n 3. Ipanema \n 0. Outra Frase")
hoje = date.today()
hoje = hoje.strftime("%d%m%Y")

while True:
    try:
        a = int(input("Digite um número: "))
        if a == 1:
            nome_arquivo = ""+hoje+"_PREVENTIVA_SEMPARAR_SHORT_1"
            dataset = sms_semparar('sms',frase_sp1)
            exportar_dados(dataset, nome_arquivo)
        elif a == 2:
            dataset = sms_semparar('sms',frase_sp2)
            nome_arquivo = ""+hoje+"_PREVENTIVA_SEMPARAR_SHORT_2"
            sms_semparar('sms',frase_sp1)
            exportar_dados(dataset, nome_arquivo)
        elif a == 3:
            print("Ainda Não disponivel")
        elif a == 0:
            print("Digite a Frase:")
        break
    except ValueError:
        print('SOMENTE NUMEROS')
    except PermissionError:
        print("A planilha Temp deve permanecer fechada durante a execução")
