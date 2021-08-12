def temperatura_ar_interna(temperatura_ar_interna_atual, temperatura_ar_interna_minima, temperatura_ar_interna_maxima):

    resfriador = False
    aquecedor = False

    if temperatura_ar_interna_atual <= temperatura_ar_interna_minima:
        aquecedor = True

    if temperatura_ar_interna_atual >= temperatura_ar_interna_maxima:
        resfriador = True

    return resfriador, aquecedor