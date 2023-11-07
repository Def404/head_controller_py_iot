import os
import time

import paho.mqtt.client as mqtt
from datetime import datetime

CLIENT_NAME = os.environ.get("CLIENT_NAME")
BROKER_HOST = os.environ.get("BROKER_HOST")
BROKER_PORT = int(os.environ.get("BROKER_PORT"))
TOPIC = os.environ.get("TOPIC")


def on_connect(client, userdata, flags, rc):
    if not rc:
        print(f'{datetime.utcnow()} | {client} connect to broker', flush=True)
    else:
        print(f'{datetime.utcnow()} | {client} not connect to broker {rc}', flush=True)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    TOPIC = msg.topic
    payload = msg.payload.decode('utf-8')
    print(f'{datetime.utcnow()} | Get messege {TOPIC}: {payload}')


def main():
    client = mqtt.Client(CLIENT_NAME)
    client.on_connect = on_connect
    client.connect(host=BROKER_HOST, port=BROKER_PORT)
    client.subscribe(TOPIC)
    client.loop_forever()


if __name__ == '__main__':
    main()