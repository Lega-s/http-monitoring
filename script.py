import requests
import time
from datetime import datetime
import csv
import os

csv_file = 'data.csv'
sleep_time = 120

proxies = {
    "http": "http://userproxy.pnet.ch:3128",
    "https": "http://userproxy.pnet.ch:3128",
}

if not os.path.isfile(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'latency_ms', 'error'])

def measure_load_time():
    start_time = time.time()
    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=10)
        latency = int((time.time() - start_time) * 1000)
        
        if (latency > 500):
            sleep_time = 5
            
        else:
            sleep_time = 120
            
        return {
            "latency_ms": latency,
            "error": None
        }
    
    except requests.exceptions.RequestException as e:
        latency = int((time.time() - start_time) * 1000)
        return {
            "latency_ms": 0,
            "error": str(e)
        }

while (True):
    result = measure_load_time()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(result)

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, result['latency_ms'], result['error']])

    time.sleep(sleep_time)