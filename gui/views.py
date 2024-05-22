from django.shortcuts import render
from django.contrib import messages
import serial
# Create your views here.
class sendCommands:
    def home(self, request):
        return render(request, "index.html")    
    
    def send(self, request):
        cfreq = request.GET.get('cfreq')
        cwidth = request.GET.get('cwidth')
        rmin = request.GET.get('rmin')
        rmax = request.GET.get('rmax')
        rwidth = request.GET.get('rwidth')
        go = False
        if request.method == 'clock':
            if cfreq != True:
                messages.warning(request, 'Please add a clock frequency')
            else:
                if cwidth != True:
                    messages.warning(request, 'Please add a clock pulse width')
                else:
                    go = True
                    arduino = serial.Serial("COM3", 9600)
                    while go:
                        data = arduino.readline()
                        if data:
                            pass
                        else:
                            arduino.write(bytes("clock"))
                            arduino.write(bytes(cfreq))
                            arduino.write(bytes(cwidth))
                            arduino.write(bytes("start"))
            print("clock")
        elif request.method == 'random':
            if rmin != True:
                messages.warning(request, 'Please add a minimum value for the randomizer')
            elif rmax != True:
                messages.warning(request, 'Please add a maximum value for the randomizer')
            elif rmax and rmin != True:
                messages.warning(request, 'Please add randomization values')
            elif rmin <= rmax:
                messages.warning(request, 'Your minimum is larger than the maximum')
            else:
                if rwidth != True:
                    messages.warning(request, 'Please add a pulse width')
                else:
                    go = True
                    arduino = serial.Serial("COM3", 9660)
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
        else:
            return render(request, 'index.html')