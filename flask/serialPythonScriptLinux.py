
# code adapted from here: https://www.tinkerassist.com/blog/arduino-serial-port-read

import argparse
import serial.tools.list_ports
import time
import sys

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()



# for now we hard code the COM port to use
portVar = "/dev/ttyACM0"
# set up serial object and open
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
# wait for one second.
time.sleep(1)


    
def sendMessage(msg):
##    # take serial to pass on to arduino or end loop desired
##    msg = input("give message to send via serial, (or exit to end)")
##    if msg == "exit":
##        loop=False
##    # reset input buffer so that serial messages from arduino from immediately after command are printed
    serialInst.reset_input_buffer()
    serialInst.write((msg+"\n").encode('utf-8'))
    # wait 2 seconds to ensure the command registers
    time.sleep(2)
    # print 50 lines of Serial messages coming from arduino (if they exist)
    # we do this to see what the time seems to be
    for i in range(50):
        if serialInst.in_waiting:
            packet = serialInst.readline()
            sys.stdout.write(packet.decode('utf').rstrip('\n')+'\n')

def error(self, message):
        sys.stderr.write(f'error: {message}\n')
        self.print_help()
        sys.exit(2)
        

def getMessage(start_stop,typ,pulse_width,freq):
    if start_stop == "stop":
        sendMessage(start_stop)
    elif start_stop == "start":
        if freq > 400:
            sys.stdout.write("max value of frequency is 400 Hz. frequency has been set to 400 Hz")
            sendMessage(start_stop + "," + typ + "," + str(pulse_width) + "," + "400")
        else:
            sendMessage(start_stop + "," + typ + "," + str(pulse_width) + "," + str(freq))


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Trigger Emulator to set type of trigger and frequency")

    # Add arguments
    parser.add_argument('start_stop', type=str, choices=["start","stop"], help="keyword to start or stop signal. use \"start\" or \"stop\".")
    parser.add_argument('type', type=str, choices=["clk","rand"], nargs="?", help="type of trigger, \"clk\" for clocked and \"rand\" for random.")
    parser.add_argument('pulse_width', type=int, nargs="?", help="pulse width of signal (in microseconds)")
    parser.add_argument('frequency', type=int, nargs="?", help="frequency of clocked signal or average? frequency of random signal (in Hz)")

    # Parse the arguments
    args = parser.parse_args()

    # Use the arguments
    getMessage(args.start_stop,args.type,args.pulse_width,args.frequency)
    print(type(args.frequency))
    

if __name__ == "__main__":
    main()
