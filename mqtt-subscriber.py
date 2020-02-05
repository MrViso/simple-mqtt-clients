import sys, getopt
import paho.mqtt.client as mqtt
import time
import random
import array

# Main client program
def main(argv):
  # Default values
  # hostname
  broker = "localhost"
  # port
  port = 1883
  # client name
  name = "Device 1"
  # topic
  topics = ['/data']

  # Try to load Options
  try:
    opts, args = getopt.getopt(argv, "h:p:n:t:", ["help", "hostname=", "port=", "name=", "topic="])
  # Wrong options
  except getopt.GetoptError:
    print ('Error: publisher.py -h <hostname> -p <port>')
    sys.exit(2)
  # Load Options and argument
  for opt, arg in opts:
    # Help Option
    if opt == '--help':
      print ('Help: publisher.py -h <hostname> -p <port>')
      sys.exit()
    # Optional Hostname instead of localhost
    elif opt in ("-h", "--hostname"):
      broker = arg
      print ('Set Broker Hostname ' + broker)
    # Optional Port
    elif opt in ("-p", "--port"):
      port = int(arg)
    # Client name
    elif opt in ("-n", "--name"):
      name = arg
    elif opt in ("-t", "--topic"):
      topics.append(arg)


  # Subscriber Part

  # Time to live
  timelive = 60

  # On Connect
  def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to topics
    for topic in topics:
      print("Subscribe to Topic: " + topic)
      client.subscribe(topic)

  # Payload
  def on_message(client, userdata, msg):
    print(msg.payload.decode())

  client = mqtt.Client()
  try:
    print ('Connect with ' + broker + ':' + str(port))
    client.connect(broker, port, timelive)
  # Wrong options
  except:
    print ('Error: Connection failed')
  client.on_connect = on_connect
  client.on_message = on_message
  client.loop_forever()

# Run Main program
if __name__ == "__main__":
   main(sys.argv[1:])
