import socket
import thread
import MqttPublisher
import paho.mqtt.publish as publish

   
UDP_IP = "192.168.1.20"
UDP_PORT = 5005

print("----------------------------------------------------")
print ("Opening UDP socket")
print("----------------------------------------------------") 
print()
print("UDP IP : "+UDP_IP+" UDP PORT : "+str(UDP_PORT))
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

MqttPublisher.MqttPublisher.connectClient()

thread.start_new_thread(MqttPublisher.MqttPublisher.startPublisher,())

while True:
   # print("Data read Start")
   data, addr = sock.recvfrom(140) # buffer size is 1024 bytes
   # print("data read end")
   MqttPublisher.MqttPublisher.addToDataArray(data)
   #print "received message:", data
   #publish.single("/com/bosch/xdk/data/",data,hostname="iot.eclipse.org")
   #print("data published : "+data)
