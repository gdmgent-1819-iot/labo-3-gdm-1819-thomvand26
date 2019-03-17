'''
Sensehat Dashboard
--------------------
Author: gdm-1819-thomvand26
Modified: 03-12-2019
--------------------
Installation:
sudo pip3 -U Flask
Docs: http://flask.pocoo.org/docs/1.0/
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import the libraries
from flask import Flask, jsonify, render_template, request
from sense_hat import SenseHat

# Create an instance of flask
app = Flask(__name__)

# Create an instance of the sensehat
sense = SenseHat()

# Define the root route
@app.route('/')
def index():
  return 'Look the flask server is running'

# Define the nmd route
@app.route('/nmd')
def nmd():
  return 'Greetings Earthlings. We are NMDrs'

# Define the my_ip route
@app.route('/my_ip', methods=['GET'])
def my_ip():
  return jsonify({
    'ip': request.remote_addr
  }), 200

# Define the api_environment route
@app.route('/api/environment', methods=['GET'])
def api_environment():
  environment_obj = {
    'temperature': {
      'value': round(sense.get_temperature()),
      'unit': u'°C'
    },
    'humidity': {
      'value': round(sense.get_humidity()),
      'unit': u'%'
    },
    'pressure': {
      'value': round(sense.get_pressure()),
      'unit': u'mbar'
    }
  }
  return jsonify(environment_obj), 200

# Define the api_environment route
@app.route('/environment', methods=['GET'])
def environment():
  environment_obj = {
    'temperature': {
      'value': round(sense.get_temperature()),
      'unit': u'°C'
    },
    'humidity': {
      'value': round(sense.get_humidity()),
      'unit': u'%'
    },
    'pressure': {
      'value': round(sense.get_pressure()),
      'unit': u'mbar'
    }
  }
  return render_template('environment.html', environment=environment_obj)

  
@app.route('/kleur', methods=['GET'])
def kleur():
  environment_obj = {
    # 'temperature': {
    #   'value': round(sense.get_temperature()),
    #   'unit': u'C'
    # },
    # 'humidity': {
    #   'value': round(sense.get_humidity()),
    #   'unit': u'%'
    # },
    # 'pressure': {
    #   'value': round(sense.get_pressure()),
    #   'unit': u'mbar'
    # }
  }
  return render_template('index.html', index=environment_obj)

# Main method for Flask server
if __name__ == '__main__':
  # app.run(host = '10.5.129.6', port = 8080, debug = True) #school
  app.run(host = '192.168.0.105', port = 8080, debug = True) #thuis
