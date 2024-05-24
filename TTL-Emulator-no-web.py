import serial
import time

while True:
    mode = input("Input 'clock' for predictable triggering. Input 'random' for pseudo-random triggering: ")

    if mode == 'clock':

        cfreq = input("Input Frequency (ex: 1 for 1Hz, 1,000 for 1kHz): ")
        cwidth = input("Input Pulse Width (ex: 1 for 1μs, 100 for 1ms): ")
        try:
            cfreq = int(cfreq)
            cwidth = int(cwidth)
        except Exception as e:
            print(e)

        go = True
        send = "start,clk,"+str(cfreq)+","+str(cwidth)
        #Change COM3 to whatever port the Arduino is on
        try:
            arduino = serial.Serial("/dev/ttyACM0", 9600, timeout = 1)
            info = arduino.read(arduino.in_waiting)
            print(info)
            arduino.reset_input_buffer()
            arduino.write(bytes(send, 'utf-8'))
            time.sleep(0.05)
            while go:
                if arduino.in_waiting > 0:
                    info = arduino.read(arduino.in_waiting)
                    print(info)
                    arduino.reset_input_buffer()
        except Exception as e:
            print(e)
    
    elif mode == 'random':
            rfreqc = input("Input Center Frequency: ")
            rwidth = input("Input Pulse Width (ex: 1 for 1μs, 100 for 1ms): ")
            try:
                rfreqc = int(rfreqc)
                rwidth = int(rwidth)
            except Exception as e:
                print(e)
            go = True
            #Change COM3 to whatever port the Arduino is on
            try:
                arduino = serial.Serial("/dev/ttyACM0", 9600)
                while go:
                    data = arduino.readline()
                    if data:
                        print(data)
                    else:
                        arduino.write(bytes("start,rand,"+rwidth+","+rfreqc))
            except Exception as e:
                print(e)