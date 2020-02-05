FROM python:latest
RUN pip install paho-mqtt
WORKDIR /mqtt-clients
COPY mqtt-subscriber.py ./
ENV host localhost
ENV port 1883
ENV topic /data1
#CMD python mqtt-subscriber.py -h ${host} -t ${topic} -p ${port}
CMD python mqtt-subscriber.py -h ${host} -t ${topic} -p ${port}
