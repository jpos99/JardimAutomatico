from datetime import datetime


def controle_luz(hora_de_ligar, horas_ligada):

    data_atual = datetime.now()
    horario_atual = data_atual.hour
    hora_de_desligar = hora_de_ligar + horas_ligada

    if hora_de_ligar <= horario_atual < hora_de_desligar:

        return True

    return False

