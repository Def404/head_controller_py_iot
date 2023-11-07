import os
import paho.mqtt.client as mqtt
from datetime import datetime

CLIENT_NAME = os.environ.get("CLIENT_NAME")
BROKER_HOST = os.environ.get("BROKER_HOST")
BROKER_PORT = int(os.environ.get("BROKER_PORT"))
TOPIC = os.environ.get("TOPIC")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    TOPIC = msg.topic
    payload = msg.payload.decode('utf-8')
    print(f'{datetime.utcnow()} | Get messege {TOPIC}: {payload}')


if __name__ == '__main__':
    client = mqtt.Client(CLIENT_NAME, clean_session=True, userdata=None, transport="tcp")
    # client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host=BROKER_HOST, port=BROKER_PORT)

    client.subscribe(TOPIC)
    client.loop_forever()