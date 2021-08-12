import time

def semana_planta(data_inicio_planta):

    data_atual = (time.time()/60)/60
    direrenca_horas = data_atual - data_inicio_planta
    semana = direrenca_horas / 168
    return int(semana)+1
