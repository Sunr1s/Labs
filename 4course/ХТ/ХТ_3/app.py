from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

items = []

@app.route('/items/', methods=['POST'])
def create_item():
    data = request.json
    item_id = len(items) + 1
    name = data.get('name')
    description = data.get('description')
    item = {'id': item_id, 'name': name, 'description': description}
    items.append(item)
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    data = request.json
    item['name'] = data['name']
    item['description'] = data['description']
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    items = [item for item in items if item['id'] != item_id]
    return '', 204

@app.route('/items/', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
