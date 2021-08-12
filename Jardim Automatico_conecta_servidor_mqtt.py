import time

cliente_mqtt =
endereco_servidor_mqtt = 10.3.141.1

def conecta_servidor_mqtt(conectado):

    while conectado == False:
        try:
            cliente_mqtt.connect(endereco_servidor_mqtt)
            conectado = True
            print("Conectado!!")
        except:
            conectado = False
        time.sleep(5)