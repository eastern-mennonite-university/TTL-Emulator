from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import serial
# Create your views here.
class sendCommands:
    def home(self, request):
        return redirect("index")    
    
    def send(self, request):
        self.cfreq = request.GET.get('cfreq')
        self.cwidth = request.GET.get('cwidth')
        self.rmin = request.GET.get('rmin')
        self.rmax = request.GET.get('rmax')
        self.rwidth = request.GET.get('rwidth')
        go = False
        if request.method == 'clock':
            if self.cfreq != True:
                messages.warning(request, 'Please add a clock frequency')
            else:
                if self.cwidth != True:
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
                            arduino.write(bytes(self.cfreq))
                            print(self.cfreq)
                            arduino.write(bytes(self.cwidth))
                            arduino.write(bytes("start"))
            print("clock")
        elif request.method == 'random':
            if self.rmin != True:
                messages.warning(request, 'Please add a minimum value for the randomizer')
            elif self.rmax != True:
                messages.warning(request, 'Please add a maximum value for the randomizer')
            elif self.rmax and self.rmin != True:
                messages.warning(request, 'Please add randomization values')
            elif self.rmin <= self.rmax:
                messages.warning(request, 'Your minimum is larger than the maximum')
            else:
                if self.rwidth != True:
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
                            arduino.write(bytes(self.rmin))
                            arduino.write(bytes(self.rmax))
                            arduino.write(bytes(self.rwidth))
                            arduino.write(bytes("start"))
        else:
            return render(request, 'index.html')