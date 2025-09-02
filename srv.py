from flask import Flask, request, jsonify
import os
import csv

srv = Flask(__name__)
csv_file = 'data.csv'

if not os.path.isfile(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'latency_ms', 'error', 'client_id'])

@srv.route('/log', methods=['POST'])
def add_log():
    data = request.json
    with open("data.csv", "a") as file:
        file.write(f"{data['timestamp']},{data['latency_ms']},{data['error']},{data['client_id']}\n")
    return jsonify({"response": "Created Log"}), 201

@srv.route('/log', methods=['GET'])
def get_logs():
    try:
        with open("data.csv", "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = ""

    return content, 200, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    srv.run(host="0.0.0.0", port=5000, debug=True)
