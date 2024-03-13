from flask import Flask
from threading import Thread
import platform
import time

app = Flask('')



@app.route('/')
def home():
    print_computer_specs()

def get_computer_specs():
    specs = {}

        # Retrieving system information
    specs['System'] = platform.system()
    specs['Node'] = platform.node()
    specs['Release'] = platform.release()
    specs['Version'] = platform.version()
    specs['Machine'] = platform.machine()
    specs['Processor'] = platform.processor()

        # Retrieving additional hardware information
    try:
        import psutil
        specs['CPU Cores'] = psutil.cpu_count(logical=False)
        specs['Total CPU Threads'] = psutil.cpu_count(logical=True)
        specs['RAM'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3), 2)) + " GB"
    except ImportError:
        specs['CPU Cores'] = "N/A"
        specs['Total CPU Threads'] = "N/A"
        specs['RAM'] = "N/A"

    return specs

def print_computer_specs():
    while True:
        specs = get_computer_specs()
        print("Computer Specifications:")
        for key, value in specs.items():
            print(f"{key}: {value}")
        print("\n")
        time.sleep(5)  # Adjust interval as needed

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
