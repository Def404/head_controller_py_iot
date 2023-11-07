FROM python:3.10
WORKDIR /app
ADD req_mqtt.txt .
RUN pip install --upgrade pip
RUN pip install -r /req_mqtt.txt
ADD main.py .
CMD ["python", "./main.py"]