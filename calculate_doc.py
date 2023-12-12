from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/sum', methods=['POST'])
def add():
    data = request.get_json()
    number1 = data['number1']
    number2 = data['number2']
    result = number1 + number2
    return jsonify({'result': result})

@app.route('/min', methods=['POST'])
def subtract():
    data = request.get_json()
    number1 = data['number1']
    number2 = data['number2']
    result = number1 - number2
    return jsonify({'result': result})

@app.route('/multy', methods=['POST'])
def multiply():
    data = request.get_json()
    number1 = data['number1']
    number2 = data['number2']
    result = number1 * number2
    return jsonify({'result': result})

@app.route('/del', methods=['POST'])
def divide():
    data = request.get_json()
    number1 = data['number1']
    number2 = data['number2']
    result = number1 / number2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


    
#sudo docker build -t calculate_doc . 
#sudo docker run -p 5000:5000 calculate_doc
#curl -X POST -H "Content-Type: application/json" -d '{"number1": 10, "number2": 5}' http://127.0.0.1:5000/del