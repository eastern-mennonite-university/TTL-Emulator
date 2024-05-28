from flask import Flask, render_template, request
import serial
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def send():
    go = False
    if request.method == 'POST':
        if request.form["clock"]:
            cfreq = request.form.get('cfreq')
            cwidth = request.form.get('cwidth')
            subprocess.run("python3", "serialPythonScriptLinux.py", "clk", str(cwidth), str(cfreq))
            go = True
        elif request.form['random']:
            rfreq = request.form.get('rfreq')
            rwidth = request.form.get('rwidth')
            subprocess.run("python3", "serialPythonScriptLinux.py", "rand", str(rwidth), str(rfreq))
            go = True
    while go:
        if request.form['stop']:
            subprocess.run("python3", "serialPythonScriptLinux.py", "stop")
            go = False
    return render_template('index.html')