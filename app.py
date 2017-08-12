from flask import Flask, render_template
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/blink/<int:speed>')
def blink(speed):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

    GPIO.output(7,True)## Switch on pin 7
    time.sleep(speed)## Wait
    GPIO.output(7,False)## Switch off pin 7
    time.sleep(speed)## Wait
    GPIO.cleanup()
