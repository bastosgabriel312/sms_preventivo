# Importa Pandas e datetime
import pandas as pd
from datetime import date


#FUNÇÕES DO PANDAS (criadas como padrões para projeto)


def localizar_dados(dataset, coluna, valor_procurado):
    dado = dataset.loc[dataset[coluna] == valor_procurado]
    return dado

def deletar_coluna(dataset,nome_coluna):
    dataset.drop([nome_coluna],axis=1,inplace=True)
    dataset

def adicionar_coluna(dataset, nome_coluna,componentes):
    dataset[nome_coluna] = componentes
    dataset.head()

def contar_valores(dataset, coluna):
    data = pd.value_counts(dataset[coluna], dropna = False)
    return data

def exportar_dados(nome,arquivo,tipo,pasta):
    if tipo == 'csv':
        nome.to_csv(""+pasta+"/"+arquivo+".csv", index = False, header = False, sep = ';', encoding = 'utf-8')
    elif tipo == 'txt':
        nome.to_csv(""+pasta+"/"+arquivo+".txt", index = False, header = False, sep = ';', encoding = 'utf-8')

def contar_nulos_coluna(dataset, coluna):
    dados = pd.value_counts(dataset[coluna], dropna = False)
    return dados

def dividir_coluna(dataframe,delimi,coluna):
    df = dataframe[coluna].str.split(delimi)
    df = df.str.get(0)
    return df

def inserir_linha(idx, df, df_inserir):
    dfA = df.iloc[:idx, ]
    dfB = df.iloc[idx:, ]

    df = dfA.append(df_inserir).append(dfB).reset_index(drop = True)

    return df

#FUNÇÕES SMS



def tratamento_ipanema(data):

    #Separando as colunas FONE em Dataframes diferentes
    d1 = data['FONE1']
    d2 = data['FONE2']
    d3 = data['FONE3']
    d4 = data['FONE4']
    d5 = data['FONE5']
    d6 = data['FONE6']
    d7 = data['FONE7']

    #Dataframe 1 recebe ao final do arquivo os outros dataframes
    d1 = d1.append(d2, ignore_index=True)
    d1 = d1.append(d3, ignore_index=True)
    d1 = d1.append(d4, ignore_index=True)
    d1 = d1.append(d5, ignore_index=True)
    d1 = d1.append(d6, ignore_index=True)
    d1 = d1.append(d7, ignore_index=True)

    # Exclui as linhas nulas
    d1 = d1.dropna()

    # Transforma em string para retirar o .0 no final dos números
    d1 = d1.astype(str)
    df = d1.str.split('.')
    df = df.str.get(0)
    
    return df

def sms_ipanema(CSV,frase):
    #Lê o CSV
    data = pd.read_csv(CSV, sep=';')
    #utiliza a função para tratar os dados no arquivo
    data = tratamento_ipanema(data)
    #Transforma de Pandas.Series em Pandas.DataFrame
    data = data.to_frame()
    #recebe arquivo de números teste para inclusão nas primeiras linhas da tabela
    dic = dividir_coluna(num_teste('numteste'), ';',0)
    #Transforma de Pandas.Series em Pandas.DataFrame
    dic = dic.to_frame()
    #Header da coluna recebe o nome '0'
    data.columns = [0]
    #função inserir linha para incluir os números no inicio da tabela
    data = inserir_linha(0,data,dic)
    #define duas colunas no dataframe: |1|frase|
    data = pd.DataFrame(data, columns = [0,'frase'])
    #todas as linhas da coluna frase recebem o parametro frase
    data['frase'] = frase

    return data
    
    



def num_teste(arquivo):
    dataset = pd.read_fwf(""+arquivo+".txt", sep=';',dtype='unicode', header = None)
    return dataset

def sms_semparar(arquivo,frase):
    #pandas lê o arquivo (.txt) e coloca dentro da variavel
    dataset = pd.read_fwf(arquivo, sep=';',dtype='unicode', header = None)
    #retorno da função num_teste dentro de uma variavel lendo o arquivo 'numteste.txt'
    dic = num_teste('numteste')
    #Uso da função inserir_linha para mescar dois dataframes
    dataset = inserir_linha(0, dataset, dic)
    #Uso da função dividir_coluna para separar os números dos nomes
    dataset = dividir_coluna(dataset, ';',0)
    print(dataset)
    #define duas colunas no dataframe: |1|frase|
    dataset = pd.DataFrame(dataset, columns = [0,'frase'])
    #todas as linhas da coluna frase recebem o parametro frase
    dataset['frase'] = frase
    return dataset

def d_mais_um():
    #data_atual recebe dia de hoje
    data_atual = date.today()
    #d_1 recebe data atual + 1 dia
    d_1 = date.fromordinal(data_atual.toordinal()+1)
    #dia_semana recebe função que transforma em número o dia da semana aplicada no d_1
    dia_semana = d_1.weekday()
    #condição para verificar se dia da semana é sabado
    if dia_semana == 0 or dia_semana == 5:
        d_1 = date.fromordinal(data_atual.toordinal()+3)
        

    return d_1


