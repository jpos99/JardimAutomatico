def humidade_ar(umidade_ar_atual, umidade_ar_minima, umidade_ar_maxima):
    """
    Recebe humidade atual, maxima e minima. Retorna tupla True ou False para umidificador e desumidificador nesta ordem.
    True = liga, false = não liga
    """

    umidificador = False
    desumidificador = False

    if umidade_ar_atual <= umidade_ar_minima:
        umidificador = True

    if umidade_ar_atual >= umidade_ar_maxima:
        desumidificador = True

    return umidificador, desumidificador