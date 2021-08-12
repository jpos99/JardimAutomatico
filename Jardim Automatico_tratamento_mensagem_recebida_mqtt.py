def tratamento_mensagem_recebida_mqtt(recebe_da_estufa):
    print("def tratamento_leitura_recebida_mqtt(recebe_da_estufa):")
    global umidade_solo_atual
    global luminosidade_atual
    global umidade_ar_atual
    global temperatura_ar_interna_atual

    recebe_da_estufa = recebe_da_estufa.decode("utf-8")
    print("def tratamento_leitura_recebida_mqtt(recebe_da_estufa): / recebe_da_estufa = recebe_da_estufa.decode('utf-8')")
    # Umidade do solo, Luminosidade, Umidade do ar, temperatura
    umidade_solo_atual = float(recebe_da_estufa.split(';')[0])
    luminosidade_atual = float(recebe_da_estufa.split(';')[1])
    umidade_ar_atual = float(recebe_da_estufa.split(';')[2])
    temperatura_ar_interna_atual = float(recebe_da_estufa.split(';')[3])
    print(f'Unimdade Solo = {umidade_solo_atual}; '
          f'Luminosidade = {luminosidade_atual}; '
          f'Umidade Ar = {umidade_ar_atual}; '
          f'Temperatura Ar = {temperatura_ar_interna_atual}')