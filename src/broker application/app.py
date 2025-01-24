from flask import Flask, render_template
import paho.mqtt.client as mqtt

PORT_MQTT_WS = 8081
IP_HOST_MQTT_WS = '192.168.0.100'
TVs_NAME = ['L1C0','L1C1','L1C2','L1C3','L1C4',
            'L2C0','L2C1','L2C2','L2C3','L2C4']

app = Flask(__name__)

INDEX_DA_TV = 0
@app.route('/'+TVs_NAME[INDEX_DA_TV])
def L1C0():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV]
            )


INDEX_DA_TV1 = 1
@app.route('/'+TVs_NAME[INDEX_DA_TV1])
def L1C1():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV1]
            )

INDEX_DA_TV2 = 2
@app.route('/'+TVs_NAME[INDEX_DA_TV2])
def L1C2():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV2]
            )

INDEX_DA_TV3 = 3
@app.route('/'+TVs_NAME[INDEX_DA_TV3])
def L1C3():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV3]
            )


INDEX_DA_TV4 = 4
@app.route('/'+TVs_NAME[INDEX_DA_TV4])
def L1C4():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV4]
            )

#-----------------///------------------///------------------///---------------------------------

INDEX_DA_TV5 = 5
@app.route('/'+TVs_NAME[INDEX_DA_TV5])
def L2C0():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV5]
            )
INDEX_DA_TV6 = 6
@app.route('/'+TVs_NAME[INDEX_DA_TV6])
def L2C1():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV6]
            )


INDEX_DA_TV7 = 7
@app.route('/'+TVs_NAME[INDEX_DA_TV7])
def L2C2():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV7]
            )


INDEX_DA_TV8 = 8
@app.route('/'+TVs_NAME[INDEX_DA_TV8])
def L2C3():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV8]
            )


INDEX_DA_TV9 = 9
@app.route('/'+TVs_NAME[INDEX_DA_TV9])
def L2C4():
    return render_template(
                'index.html', 
                PORT_MQTT_WS    = PORT_MQTT_WS,
                IP_HOST_MQTT_WS = IP_HOST_MQTT_WS,
                TV_NAME = TVs_NAME[INDEX_DA_TV9]
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
