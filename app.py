from flask import Flask, jsonify, render_template
import psutil
import platform
import socket

app = Flask(__name__,template_folder='system')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/system_info', methods=['GET','POST'])
def system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    net_io = psutil.net_io_counters()
    network_usage = {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv
    }
    
    system_info = {
        'processor_name': platform.processor(),
        'os_version': platform.platform(),
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'network_usage': network_usage
    }
    
    return jsonify(system_info)


if __name__ == '__main__':
    app.run(debug=True, port=5100)
