#from escreve_arquivo_csv import *
#from controle_luz import *
#from regador import *
#from semana_planta import *
#from temperatura_ar_interna import *
#from umidade_ar_interna import *

from JardimAutomaticoComunicacao import *


global luminosidade_atual
global umidade_solo_atual
global temperatura_ar_interna_atual
global umidade_ar_atual
global lista_de_topicos


topico_leitura_umidade_solo = "estufa/leituras/umidade_solo"
topico_leitura_umidade_ar = "estufa/leituras/umidade_ar"
topico_leitura_temperatura_ar_interna = "estufa/leituras/temperatura_ar_interna"
topico_leitura_luminosidade = "estufa/leituras/luminosidade"
lista_de_topicos = [topico_leitura_umidade_solo, topico_leitura_umidade_ar,
                    topico_leitura_temperatura_ar_interna, topico_leitura_luminosidade]


hora_de_ligar = 5.0                     # Variável definida manualmente
horas_ligada = 18.0                     # Variável definida manualmente

umidade_solo_minima = 45.0              # Variável definida manualmente

data_inicio_planta = 0                  # Variável definida manualmente

temperatura_ar_interna_minima = 21.0    # Variável definida manualmente
temperatura_ar_interna_maxima = 24.0    # Variável definida manualmente

umidade_ar_minima = 60                  # Variável definida manualmente
umidade_ar_maxima = 70                  # Variável definida manualmente

liga_luz = 0                            # Variável de liga e desliga

liga_resfriador = 0                     # Variável de liga e desliga
liga_aquecedor = 0                      # Variável de liga e desliga

liga_umidificador = 0                   # Variável de liga e desliga
liga_desumidificador = 0                # Variável de liga e desliga

liga_segundos_bomba = 0                 # Variável de liga e desliga
conectado = False


while True:

    if not conectado:
        cliente_mqtt = ProtocoloMqtt("estufa", "10.3.141.1", lista_de_topicos)  # Variável que comptem uma str com endereço do servidor
        cliente_mqtt.conecta_servidor_mqtt()
    cliente_mqtt.comeca_loop_mqtt()

    hora_anterior = 0                           # Variável para definir se grava ou não no csv agora

    intervalo_minutos_entre_gravacoes_cvs = 5   # Variável que define de quanto em quanto tempo grava os dados no arquivo csv

    for topico in lista_de_topicos:
        cliente_mqtt.subescreve_ao_topico(topico)
        sleep(1)
    print('main', dicionario_de_leituras)
    cliente_mqtt.encerra_loop_mqtt()
    tempo_rerodar_while_true = 30               # Variável para defirir de quantos em quanstos segundos reroda o programa
    sleep(tempo_rerodar_while_true)

'''
def publica_comandos_para_estufa(umidade_solo_atual, temperatura_ar_interna_atual, umidade_ar_atual):

    liga_luz = controle_luz(hora_de_ligar,
                            horas_ligada)

    # temperatura_ar_interna_atual = float(temperatura_ar_interna_atual.decode("utf-8"))
    liga_resfriador, liga_aquecedor = temperatura_ar_interna(temperatura_ar_interna_atual,
                                                             temperatura_ar_interna_minima,
                                                             temperatura_ar_interna_maxima)

    # umidade_ar_atual = float(umidade_ar_atual.decode("utf-8"))
    liga_umidificador, liga_desumidificador = humidade_ar(umidade_ar_atual,
                                                          umidade_ar_minima,
                                                          umidade_ar_maxima)

    # umidade_solo_atual = float(umidade_solo_atual.decode("utf-8"))
    liga_segundos_bomba = regador(umidade_solo_atual,
                                  umidade_solo_minima)

    """
    cliente_mqtt.publish('estufa/comandos',
                        f'{muda_de_booleano_para_string(liga_luz)};'
                        f'{muda_de_booleano_para_string(liga_resfriador)};'
                        f'{muda_de_booleano_para_string(liga_aquecedor)};'
                        f'{muda_de_booleano_para_string(liga_umidificador)};'
                        f'{muda_de_booleano_para_string(liga_desumidificador)};'
                        f'{liga_segundos_bomba}', retain=True)
    """

    cliente_mqtt.publish("estufa/comandos/umidade_solo", f'{liga_segundos_bomba}', retain=True)
    cliente_mqtt.publish("estufa/comandos/umidade_ar", f'{muda_de_booleano_para_string(liga_umidificador)};'
                        f'{muda_de_booleano_para_string(liga_desumidificador)}', retain=True)
    cliente_mqtt.publish("estufa/comandos/temperatura_ar_interna" f'{muda_de_booleano_para_string(liga_resfriador)};'
                        f'{muda_de_booleano_para_string(liga_aquecedor)}', retain=True)
    cliente_mqtt.publish("estufa/comandos/luminosidade" f'{muda_de_booleano_para_string(liga_luz)}', retain=True)


    liga_luz = controle_luz(hora_de_ligar,
                            horas_ligada)

    temperatura_ar_interna_atual = trata_valor_recebido(temperatura_ar_interna_atual)
    liga_resfriador, liga_aquecedor = temperatura_ar_interna(temperatura_ar_interna_atual,
                                                             temperatura_ar_interna_minima,
                                                             temperatura_ar_interna_maxima)

    umidade_ar_atual = trata_valor_recebido(umidade_ar_atual)
    liga_umidificador, liga_desumidificador = humidade_ar(umidade_ar_atual,
                                                          umidade_ar_minima,
                                                          umidade_ar_maxima)

    umidade_solo_atual = trata_valor_recebido(umidade_solo_atual)
    liga_segundos_bomba = regador(umidade_solo_atual,
                                  umidade_solo_minima)

    publica_comandos_para_estufa(umidade_solo_atual, temperatura_ar_interna_atual, umidade_ar_atual)


    if hora_anterior < int((time.time()/60)+intervalo_minutos_entre_gravacoes_cvs):
        hora_anterior = int((time.time()/60)+intervalo_minutos_entre_gravacoes_cvs)
        escreve_arquivo_csv(temperatura_ar_interna_atual,
                            umidade_ar_atual,
                            umidade_solo_atual,
                            luminosidade_atual,
                            liga_luz,
                            liga_resfriador,
                            liga_aquecedor,
                            liga_umidificador,
                            liga_desumidificador,
                            liga_segundos_bomba)




# semana = semana_planta(data_inicio_planta)  # retorna numero de semanas da planta

"""
#colocar esses valors em um arquivo de configuração
#Colocar esse if dentro da função semana_planta
if semana <= 8:                              #Vegetativo
    hora_de_ligar = 5.0                     #Variável definida manualmente
    horas_ligada = 18.0                     #Variável definida manualmente

    umidade_solo_minima = 45.0              #Variável definida manualmente

    data_inicio_planta = 0                  #Variável definida manualmente

    temperatura_ar_interna_minima = 21.0    #Variável definida manualmente
    temperatura_ar_interna_maxima = 24.0    #Variável definida manualmente

    umidade_ar_minima = 0.65                #Variável definida manualmente
    umidade_ar_maxima = 0.70                #Variável definida manualmente

else:                                       #Flora
    hora_de_ligar = 6.0                     #Variável definida manualmente
    horas_ligada = 12.0                     #Variável definida manualmente

    umidade_solo_minima = 45.0              #Variável definida manualmente

    data_inicio_planta = 0                  #Variável definida manualmente

    temperatura_ar_interna_minima = 24.0    #Variável definida manualmente
    temperatura_ar_interna_maxima = 27.0    #Variável definida manualmente

    umidade_ar_minima = 0.60                #Variável definida manualmente
    umidade_ar_maxima = 0.65                #Variável definida manualmente

#Escrever função processa_dados

def processa_dados (temperatura_ar_interna_atual, umidade_ar_atual, umidade_solo_atual, luminosidade_atual):

    global liga_luz
    global liga_resfriador
    global liga_aquecedor
    global liga_umidificador
    global liga_desumidificador
    global liga_segundos_bomba

    # Falso desliga, Verdadeiro liga

    liga_luz = controle_luz(hora_de_ligar, horas_ligada)
    liga_resfriador, liga_aquecedor = temperatura_ar_interna(temperatura_ar_interna_atual, temperatura_ar_interna_minima, temperatura_ar_interna_maxima)
    liga_umidificador, liga_desumidificador = humidade_ar(umidade_ar_atual, umidade_ar_minima, umidade_ar_maxima)
    liga_segundos_bomba = regador(umidade_solo_atual, umidade_solo_minima)
    
    escreve_arquivo_csv(temperatura, umidade_do_ar, umidade_solo, luminosidade, liga_luz, liga_resfriador,
                            liga_aquecedor, liga_umidificador, liga_desumidificador, liga_segundos_bomba)

    return (liga_luz, liga_resfriador, liga_aquecedor, liga_umidificador, liga_desumidificador, liga_segundos_bomba)



#controle_luz(hora_de_ligar, horas_ligada)
#regador(umidade_solo_atual, umidade_solo_minima)
#semana_planta(data_inicio_planta)
#temperatura_ar_interna(temperatura_ar_interna_atual, temperatura_ar_interna_minima, temperatura_ar_interna_maxima)
#humidade_ar(umidade_ar_atual, umidade_ar_minima, umidade_ar_maxima)'''
