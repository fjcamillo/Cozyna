from serial import Serial
import json
import requests

data = {}

arduino = Serial('/dev/ttyACM0', 9600, timeout=.1)

def segregate(config):
    if config == 'sit':
        url = '127.0.0.1:8080/api/sitCounter'
        return url

while 1:
    if arduino.readline():
        inputData = arduino.readline()[:-2]
        ArrayData = inputData.split(' ')
        print(str(ArrayData))
        Datapayload = {
            "configuration": ArrayData[0],
            "Data": ArrayData[1]
        }
        payload = json.dumps(Datapayload)

        r = requests.post('http://localhost:8000/api/sitCounter', data=payload)
