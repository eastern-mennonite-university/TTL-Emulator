from flask import Flask, render_template
import serial

app = Flask(__name__)

@app.route("/")
def send(self, request):
    self.cfreq = request.GET.get('cfreq')
    self.cwidth = request.GET.get('cwidth')
    self.rmin = request.GET.get('rmin')
    self.rmax = request.GET.get('rmax')
    self.rwidth = request.GET.get('rwidth')
    go = False
    if request.method == 'clock':
        if self.cfreq != True:
            print("bruh")
        else:
            if self.cwidth != True:
                print("bruh")
            else:
                go = True
                #Change COM3 to whatever port the Arduino is on
                arduino = serial.Serial("COM3", 9600)
                while go:
                    data = arduino.readline()
                    if data:
                        pass
                    else:
                        arduino.write(bytes("clock"))
                        arduino.write(bytes(self.cfreq))
                        print(self.cfreq)
                        arduino.write(bytes(self.cwidth))
                        arduino.write(bytes("start"))
        print("clock")
    elif request.method == 'random':
        if self.rmin != True:
            print("bruh")
        elif self.rmax != True:
            print("bruh")
        elif self.rmax and self.rmin != True:
            print("bruh")
        elif self.rmin <= self.rmax:
            print("bruh")
        else:
            if self.rwidth != True:
                print("bruh")
            else:
                go = True
                #Change COM3 to whatever port the Arduino is on
                arduino = serial.Serial("COM3", 9660)
                while go:
                    data = arduino.readline()
                    if data:
                        pass
                    else:
                        arduino.write(bytes("random"))
                        arduino.write(bytes(self.rmin))
                        arduino.write(bytes(self.rmax))
                        arduino.write(bytes(self.rwidth))
                        arduino.write(bytes("start"))
    return render_template('index.html')