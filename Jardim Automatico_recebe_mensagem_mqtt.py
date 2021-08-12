from tratamento_mensagem_recebida_mqtt import *
from conecta_servidor_mqtt import *
import paho.mqtt.client as paho

def recebe_mensagem_mqtt(client, userdata, message):
    print("## def recebe_mensagem_mqtt(client, userdata, message):")
    #print("Recebi mensagem_recebida")
    print(message.topic, "def recebe_mensagem_mqtt(client, userdata, message): / message.topic = {message.topic}")
    print(message.payload,  "def recebe_mensagem_mqtt(client, userdata, message): / message.topic = {message.payload}")
    tratamento_mensagem_recebida_mqtt(message.payload)

cliente_mqtt = paho.Client('estufa')
#cliente_mqtt.username_pw_set(username="usuario", password="1234")
cliente_mqtt.on_message = recebe_mensagem_mqtt
conectado = False

def conecta_servidor_mqtt(conectado):

    while conectado == False:
        try:
            cliente_mqtt.connect(endereco_servidor_mqtt)
            conectado = True
            print("Conectado!!")
        except:
            conectado = False
        print('saiu do try')
        time.sleep(2)