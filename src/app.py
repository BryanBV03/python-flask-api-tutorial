from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False},
    {"label": "My third task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    print("Incoming request with the following body", request_body)
    todos.append(request_body)  # Agrega el nuevo elemento a la lista
    return jsonify(todos)  # Devuelve la lista actualizada con un código de estado 201 (Created)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):  # Verificar si la posición es válida
        todos.pop(position)  # Eliminar la tarea de la lista
        return jsonify(todos)  # Retornar la lista actualizada
    else:
        return jsonify({"error": "Position out of range"}) # Retornar error si la posición es inválida

if __name__ == '__main__':
    app.run(debug=True)
