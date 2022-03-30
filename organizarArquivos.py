import os
import shutil
import xlrd
import pandas as pd
import time

try:

    df = pd.read_excel('./LISTA.xlsx')
    pns = df['PNS'].values.tolist()
    print("Nome da Pasta de Busca")
    pasta = input()

    print("Nome da Pasta para Colar")
    pasta_colar = input()

    pns_encontrados = []

    for pn in pns:
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                if pn in arquivo:
                    try:
                        pns_encontrados.append([pn,arquivo])
                        shutil.copy(os.path.join(diretorio,arquivo), os.path.join(pasta_colar,arquivo))
                    except:
                        o = 0

    df = pd.DataFrame(pns_encontrados)
    df.to_excel('relatorio.xlsx')
    print('Busca finalizada, pode fechar o programa :)')
    time.sleep(99999)
except:
    print('ERROOOOOOOOOOOOOOOOO !! chame o suporte.')
    time.sleep(99999)