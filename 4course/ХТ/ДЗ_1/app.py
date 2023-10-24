from flask import Flask, request, jsonify, render_template
import pyodbc

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

connection_string = "mssql+pyodbc://CloudSA1bf0d0cc:RbCw]~3ozA7,^_8@basegs.database.windows.net:1433/Dbase?driver=ODBC+Driver+18+for+SQL+Server"
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))

@app.route('/items/', methods=['POST'])
def create_item():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    item = Item(name=name, description=description)
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description})

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    data = request.json
    item.name = data['name']
    item.description = data['description']
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description})

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return '', 204

@app.route('/items/', methods=['GET'])
def get_items():
    items = Item.query.all()
    items_list = [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]
    return jsonify(items_list)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
