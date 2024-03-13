import platform
import time

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

if __name__ == "__main__":
    print_computer_specs()
