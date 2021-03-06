from RF24 import * 
import time

radio = RF24(RPI_V2_GPIO_P1_15, RPI_V2_GPIO_P1_24, BCM2835_SPI_SPEED_8MHZ)

pipes = [0xF0F0F0F0E1, 0xF0F0F0F0D2]


radio.begin()
radio.enableDynamicPayloads()
radio.setRetries(5,15)

radio.openReadingPipe(1, pipes[0])
radio.openReadingPipe(2, pipes[1])

radio.startListening()

radio.printDetails()

while True:
    pipe = radio.available_pipe();
    #print("pipe value:",pipe)
    if(pipe[0] == True):
        done = False
        data = None
        len = radio.getDynamicPayloadSize()
        print "data length:", len
        data = radio.read(len)
        print('Got data={0} from pipe={1}'.format(data, pipe[1]))
    time.sleep(1)
