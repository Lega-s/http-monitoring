from flask import Flask, request, jsonify

srv = Flask(__name__)

@srv.route('/log', methods=['POST'])
def add_log():
    data = request.json
    with open("data.csv", "a") as file:
        file.write(f"{data['timestamp']},{data['latency_ms']},{data['error']}\n")
    return jsonify({"response": "Created Log"}), 201

if __name__ == "__main__":
    srv.run(host="0.0.0.0", port=5000, debug=True)