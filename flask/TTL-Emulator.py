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
            #print(cfreq)
            cwidth = request.form['cwidth']
            #print(cwidth)
            term.getMessage("start", "clk", int(cwidth), int(cfreq))
    return render_template('index.html')

@app.route('/handle_random', methods=['POST'])
def handle_random():
    if request.method == "POST":
        rfreq = request.form['rfreq']
        rwidth = request.form['rwidth']
        term.getMessage("start", "rand", int(rwidth), int(rfreq))
    return render_template("index.html")

@app.route('/handle_stop', methods=['POST'])
def handle_stop():
    if request.method == "POST":
        term.getMessage("stop", None, None, None)
    return render_template("index.html")

if __name__ == '__main__':
     app.run()