from time import sleep
import paho.mqtt.client as paho

dicionario_de_leituras = {}


class ProtocoloMqtt():

    @staticmethod
    def tratamento_leitura_recebida_mqtt(mensagem_recebida, topico_recebido):

        leitura_recebida_da_estufa = mensagem_recebida.decode("utf-8")
        grandeza_recebida = topico_recebido.split("/")[-1]
        dicionario_de_leituras[grandeza_recebida] = float(leitura_recebida_da_estufa)

        return dicionario_de_leituras

    @staticmethod
    def recebe_mensagem_mqtt(client, userdata, message):

        mensagem = message.payload
        topico_recebido = message.topic
        sleep(1)
        return ProtocoloMqtt.tratamento_leitura_recebida_mqtt(mensagem, topico_recebido)

    def __init__(self, nome_cliente_mqtt, endereco_servidor_mqtt):
        self.nome_client_mqtt = nome_cliente_mqtt
        self.endereco_servidor_mqtt = endereco_servidor_mqtt

        self.cliente_mqtt = paho.Client(nome_cliente_mqtt)
        self.cliente_mqtt.username_pw_set(username="estufa1", password="tomates")
        self.cliente_mqtt.on_message = self.recebe_mensagem_mqtt

    def conecta_servidor_mqtt(self):
        global conectado
        conectado = False
        while conectado == False:
            print("tentando conectar")
            self.cliente_mqtt.username_pw_set(username="estufa1", password="tomates")
            try:
                self.cliente_mqtt.connect(self.endereco_servidor_mqtt)
                conectado = True
                print("Conectado!!")
                return conectado
            except:
                conectado = False
            sleep(5)

    def comeca_loop_mqtt(self):
        self.cliente_mqtt.loop_start()

    def encerra_loop_mqtt(self):
        self.cliente_mqtt.loop_stop()

    def subescreve_ao_topico(self, topico):
        self.cliente_mqtt.subscribe(topico)

    def publica_ao_topico(self):
        pass
