from flask import Flask, jsonify, request

app = Flask(__name__)

toys = [
    {"id": 1, "name": "Action Figure", "type": "Figure"},
    {"id": 2, "name": "Lego Set", "type": "Building"},
    {"id": 3, "name": "Doll", "type": "Doll"}
]

@app.route('/')
def home():
    return "Welcome to the Toybox API!"

@app.route('/toys', methods=['GET'])
def get_toys():
    return jsonify(toys)

@app.route('/toys/<int:id>', methods=['GET'])
def get_toy(id):
    toy = next((toy for toy in toys if toy["id"] == id), None)
    if toy is None:
        return jsonify({"error": "Toy not found"}), 404
    return jsonify(toy)

@app.route('/toys', methods=['POST'])
def add_toy():
    new_toy = request.get_json()
    toys.append(new_toy)
    return jsonify(new_toy), 201

@app.route('/toys/<int:id>', methods=['PUT'])
def update_toy(id):
    toy = next((toy for toy in toys if toy["id"] == id), None)
    if toy is None:
        return jsonify({"error": "Toy not found"}), 404
    data = request.get_json()
    toy.update(data)
    return jsonify(toy)

@app.route('/toys/<int:id>', methods=['DELETE'])
def delete_toy(id):
    global toys
    toys = [toy for toy in toys if toy["id"] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
