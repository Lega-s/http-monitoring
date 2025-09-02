from datetime import datetime, timedelta
import requests
import time

sleep_time = 120

proxies = {
    "http": "http://userproxy.pnet.ch:3128",
    "https": "http://userproxy.pnet.ch:3128",
}

def measure_load_time():
    global sleep_time
    log = {};
    start_time = time.time()

    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=10)
        latency = int((time.time() - start_time) * 1000)
        log = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "latency_ms": latency,
            "error": None
        }

        requests.post("http://10.226.0.166:5000/log", json=log)
    
    except requests.exceptions.RequestException as e:
        log = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "latency_ms": 0,
            "error": str(e)
        }

        requests.post("http://10.226.0.166:5000/log", json=log)

    if log["latency_ms"] > 500 or log["error"] is not None:
        sleep_time = 5
    else:
        sleep_time = 120
    print(log)
    return;

while (True):
    measure_load_time()
    time.sleep(sleep_time)

