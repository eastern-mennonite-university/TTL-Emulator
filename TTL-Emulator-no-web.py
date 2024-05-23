import serial

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
        #Change COM3 to whatever port the Arduino is on
        try:
            arduino = serial.Serial("COM3", 9600)
            while go:
                data = arduino.readline()
                if data:
                    pass
                else:
                    arduino.write(bytes("start,clk,"+cwidth+","+cfreq))
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
                arduino = serial.Serial("COM3", 9660)
                while go:
                    data = arduino.readline()
                    if data:
                        pass
                    else:
                        arduino.write(bytes("start,rand,"+rwidth+","+rfreqc))
            except Exception as e:
                print(e)