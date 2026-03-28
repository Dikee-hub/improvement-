from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    data = request.args
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    return jsonify({"result": a + b})

@app.route('/subtract', methods=['GET'])
def subtract():
    data = request.args
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    return jsonify({"result": a - b})

@app.route('/multiply', methods=['GET'])
def multiply():
    data = request.args
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    return jsonify({"result": a * b})

@app.route('/divide', methods=['GET'])
def divide():
    data = request.args
    a = float(data.get('a', 0))
    b = float(data.get('b', 1))  # default to 1 to avoid division by zero
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed."}), 400
    return jsonify({"result": a / b})

if __name__ == '__main__':
    app.run(debug=True)