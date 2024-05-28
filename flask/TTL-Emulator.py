from flask import Flask, render_template, request
import serial
import subprocess
import serialPythonScriptLinux as term
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_clock', methods=['POST'])
def handle_clock():
    if request.method  == "POST":
            cfreq = request.form['cfreq']
            print(cfreq)
            cwidth = request.form['cwidth']
            print(cwidth)
            term.getMessage("start", "clk", int(cwidth), int(cfreq))
    return render_template('index.html')

@app.route('/handle_random', methods=['POST'])
def handle_random():
    if request.method == "POST":
        rfreq = request.args('rfreq')
        rwidth = request.args('rwidth')
        subprocess.run("python3", "serialPythonScriptLinux.py", "rand", rwidth, rfreq)
    return render_template("index.html")

@app.route('/handle_stop', methods=['POST'])
def handle_stop():
    go = False
    if request.method == "POST":
        subprocess.run("python3", "serialPythonScriptLinux.py", "stop")
    return render_template("index.html")

if __name__ == '__main__':
     app.run()