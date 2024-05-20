from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

# In-memory data store
items = []


@api.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello, Flask!',
        'status': 'success',
        'data': [1, 2, 3, 4, 5]
    }
    return jsonify(data)


@api.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)


@api.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is not None:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404


@api.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201


@api.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is not None:
        data = request.json
        item.update(data)
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404


@api.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})
