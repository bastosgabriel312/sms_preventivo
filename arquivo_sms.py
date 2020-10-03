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

def exportar_dados(nome,arquivo):
    nome.to_csv(""+arquivo+".csv", index = False, header = False, sep = ';', encoding = 'utf-8')
    
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



def num_teste(arquivo):
    dataset = pd.read_fwf(""+arquivo+".txt", sep=';',dtype='unicode', header = None)
    return dataset

def sms_semparar(arquivo,frase):
    #pandas lê o arquivo (.txt) e coloca dentro da variavel
    dataset = pd.read_fwf(""+arquivo+".txt", sep=';',dtype='unicode', header = None)
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

