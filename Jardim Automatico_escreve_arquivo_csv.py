from os.path import exists
from datetime import datetime

# mudar o nome do arquivo csv uma vez por semana. Usar o dia da semana para saber quando criar novo arquivo

def muda_de_booleano_para_string(booleano):
    if booleano == True:
        return 'Liga'
    return 'desliga'

def escreve_arquivo_csv(temperatura, umidade_do_ar, umidade_solo, luminosidade, liga_luz, liga_resfriador,
                        liga_aquecedor, liga_umidificador, liga_desumidificador, liga_segundos_bomba):

    data_e_hora_atual = datetime.now()

    if exists("Monitoramento.csv"):     #if que muda o nome do arquivo em função da data
        arquivo_monitoramento = open("Monitoramento.csv", "a")      # "a" = addicionar
        arquivo_monitoramento.write(f'{data_e_hora_atual};{temperatura};{umidade_do_ar};{umidade_solo};{luminosidade};'
                                    f'{muda_de_booleano_para_string(liga_luz)};'
                                    f'{muda_de_booleano_para_string(liga_resfriador)};'
                                    f'{muda_de_booleano_para_string(liga_aquecedor)};'
                                    f'{muda_de_booleano_para_string(liga_umidificador)};'
                                    f'{muda_de_booleano_para_string(liga_desumidificador)};'
                                    f'{liga_segundos_bomba}\n')
    else:
        arquivo_monitoramento = open("Monitoramento.csv", "w") # "w" escrever o arquivo
        arquivo_monitoramento.write("Data e hora;Temperatura;Umidade do ar;Umidade do solo;Luminosidade;"
                                    "Luz;Resfriador;Aquecedor;Umidificador;Desumidificador;Segundos_bomba\n")

    arquivo_monitoramento.close()

