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
                    arduino.write(bytes("clock"))
                    arduino.write(bytes(cfreq))
                    print(cfreq)
                    arduino.write(bytes(cwidth))
                    arduino.write(bytes("start"))
        except Exception as e:
            print(e)
    
    elif mode == 'random':
            print("Input Average frequency (ex: min=1 max=10 for ~10Hz")
            rmin = input("Minimum: ")
            rmax = input("Maximum: ")
            rwidth = input("Input Pulse Width (ex: 1 for 1μs, 100 for 1ms): ")
            try:
                rmin = int(rmin)
                rmax = int(rmax)
                rwidth = int(rwidth)
            except Exception as e:
                print(e)
            go = True
            #Change COM3 to whatever port the Arduino is on
            arduino = serial.Serial("COM3", 9660)
            try:
                while go:
                    data = arduino.readline()
                    if data:
                        pass
                    else:
                        arduino.write(bytes("random"))
                        arduino.write(bytes(rmin))
                        arduino.write(bytes(rmax))
                        arduino.write(bytes(rwidth))
                        arduino.write(bytes("start"))
            except Exception as e:
                print(e)