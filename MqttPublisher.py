import paho.mqtt.client as mqtt
# The callback for when the client receives a CONNACK response from the server.

class MqttPublisher:
	
	global dataPublishArray;
	global client;
	dataPublishArray=[]
	client = mqtt.Client()	
		
	@staticmethod
	def addToDataArray(data):
		dataPublishArray.append(data);
	
	def on_connect(client, userdata, rc):
		print("Connected with result code "+str(rc))
		# Subscribing in on_connect() means that if we lose the connection and
		# reconnect then subscriptions will be renewed.
				
	def on_disconnect(client, userdata, rc):
		if rc != 0:
			print("Unexpected disconnection.")
			MqttPublisher.connectClient()
		
	# The callback for when a PUBLISH message is received from the server.
	def on_message(client, userdata, msg):
		print(msg.topic+" "+str(msg.payload))

	@staticmethod
	def publishMessage():
		data=dataPublishArray.pop(0);
		client.publish("/com/bosch/xdk", data)
		print("dataPublished : "+data)
	
	@staticmethod	
	def connectClient():
		print("----------------connecting to Broker -----------------")	
		client.on_connect = MqttPublisher.on_connect
		client.on_disconnect = MqttPublisher.on_disconnect
		client.connect("test.mosquitto.org", 1883, 60)
		print("----------------connected to Broker---------------------------")	

	# Blocking call that processes network traffic, dispatches callbacks and
	# handles reconnecting.
	# Other loop*() functions are available that give a threaded interface and a
	# manual interface.
	#client.loop_forever()
	
	@staticmethod
	def startPublisher():
		print("---------------Publisher Started-------------------------- ")
		while True :
			if(len(dataPublishArray)>0):
				MqttPublisher.publishMessage();	
		return
