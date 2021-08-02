import os
import os.path, time
import shutil
from datetime import date

data_atual = date.today()
pasta = 'C:/Users/STREAMSERVE/Downloads/Deletar-1d/'

if len(data_atual.strftime('%d')) == 1:
    dia_atual = '0' + data_atual.strftime('%d')
else:
    dia_atual = data_atual.strftime('%d')
    
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        dataCriacaoArquivo = time.ctime(os.path.getctime(pasta + arquivo))
        if len(dataCriacaoArquivo[8:10]) == 1:
            diaCriacaoArquivo = '0' + dataCriacaoArquivo[8:10]
        else:
            diaCriacaoArquivo = dataCriacaoArquivo[8:10]

        if dataCriacaoArquivo[8:10] != dia_atual:
            os.remove(pasta + arquivo)
