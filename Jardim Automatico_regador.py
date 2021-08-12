def regador(umidade_solo_atual, umidade_solo_minima):

    segundos_bomba = 0

    if umidade_solo_atual < umidade_solo_minima:
        segundos_bomba = 40
        return segundos_bomba
    return segundos_bomba