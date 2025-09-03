from datetime import datetime, timedelta
import requests
import time
import os

sleep_time = 120

client_id = 'w00mp3'

proxies = {
    "http": "http://userproxy.pnet.ch:3128",
    "https": "http://userproxy.pnet.ch:3128",
}

def measure_load_time():
    global sleep_time
    log = {}

    start_time = time.time()
    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=10)
        if response.status_code == 200:
            latency = int((time.time() - start_time) * 1000)
            error = None
        else:
            latency = 0
            error = f"HTTP Error {response.status_code}"

        log = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "latency_ms": latency,
            "error": error,
            "client_id": client_id
        }

        try:
            post_response = requests.post("http://10.226.0.166:5000/log", json=log)
            post_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Fehler beim Senden des Logs: {e}")

    except requests.exceptions.RequestException as e:
        log = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "latency_ms": 0,
            "error": str(e),
            "client_id": client_id
        }
        try:
            requests.post("http://10.226.0.166:5000/log", json=log)
        except Exception as post_error:
            print(f"Fehler beim Senden des Fehler-Logs: {post_error}")

    if log["latency_ms"] > 500 or log["error"] is not None:
        sleep_time = 5
    else:
        try:
            with open("interval.txt", "r") as file:
                file_interval = file.read()

            sleep_time = int(file_interval) / 1000
        except:
            print("Fehler bei der interval.txt Datei")

    print(log)
    return sleep_time




while True:
    sleep_time = measure_load_time()
    time.sleep(sleep_time)
