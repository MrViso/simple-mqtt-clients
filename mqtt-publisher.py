import sys, getopt
import paho.mqtt.client as mqtt
import time
import random

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
  topic = "/data"

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
    # Optional Port
    elif opt in ("-p", "--port"):
      port = int(arg)
    # Client name
    elif opt in ("-n", "--name"):
      name = arg
    elif opt in ("-t", "--topic"):
      topic = arg

  # Response
  def on_publish(client,userdata,result):
    print(name + " : Data published.")
    pass

  # Define client object
  client = mqtt.Client(name)
  client.on_publish = on_publish
  # Connect with Broker
  client.connect(broker, port)

  # Do Iteration with publishing numbers
  for i in range(20):
    # Random number for slee time
    d = random.randint(1, 5)
    #telemetry to send
    message = name + " : Data " + str(i)
    # Sleep for a random moment
    time.sleep(d)
    #publish message
    ret = client.publish(topic, message)

  # Iteration stops
  print("Stopped...")

# Run Main program
if __name__ == "__main__":
   main(sys.argv[1:])
