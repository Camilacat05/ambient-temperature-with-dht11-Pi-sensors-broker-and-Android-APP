import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time

SENSOR_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
client=mqtt.Client()
client2=mqtt.Client()

try:
    client.username_pw_set("asymwrrf","eyaeogtkoSeS")#replace with your user name and password
    client.connect("m24.cloudmqtt.com",13308,5)
    
    client2.username_pw_set("umqxzygo","Piw8gmrGbpwG")#replace with your user name and password
    client2.connect("m24.cloudmqtt.com",13270,5)
except KeyboardInterrupt:
    print("erro")

try:
    while True:
        umid,temp = dht.read_retry(dht.DHT11,14)
        client2.publish("pi2",temp) #pi is topic
        print("Temperatura: ",temp)
        value = GPIO.input(18)
        if(value == 1):
            print("Bebe em movimento")
        client.publish("pi",value) #pi is topic
        time.sleep(0.5)
except KeyboardInterrupt:
    print("end")
    client.disconnect()

