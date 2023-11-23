"""
This module contains Flask routes for managing a shopping cart.

Endpoints:
- GET '/': Retrieve all items in the cart.
- GET '/<int:item_id>': Retrieve a specific item in the cart by its ID.
- POST '/add': Add a new item to the cart.
- PUT '/<int:item_id>': Update an item in the cart.
- DELETE '/<int:item_id>': Delete an item from the cart.
"""
from flask import jsonify, request
from app import app
from app.services.cart_service import (
    add_item_to_cart,
    get_cart_items,
    get_cart_item_by_id,
    update_cart_item,
    delete_cart_item,
)

@app.route('/', methods=['GET'])
def get_cart():
    """Route to retrieve all items in the cart."""
    try:
        cart_items = get_cart_items()
        return jsonify({'cart_items': cart_items}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/<int:item_id>', methods=['GET'])
def get_cart_item(item_id):
    """Route to retrieve a specific item in the cart by its ID."""
    try:
        cart_item = get_cart_item_by_id(item_id)
        if not cart_item:
            return jsonify({'error': 'Item not found'}), 404
        return jsonify({'cart_item': cart_item}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/add', methods=['POST'])
def add_to_cart():
    """Route to add a new item to the cart."""
    try:
        data = request.get_json()
        product_name = data.get('product_name')
        quantity = data.get('quantity')
        price = data.get('price')

        if not all([product_name, quantity, price]):
            return jsonify({'error': 'Missing data'}), 400

        new_item = add_item_to_cart(product_name, quantity, price)
        return jsonify({'message': 'Item added to cart successfully', 'item': new_item}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/<int:item_id>', methods=['PUT'])
def update_cart(item_id):
    """Route to update an item in the cart."""
    try:
        data = request.get_json()
        updated_item = update_cart_item(item_id, data)
        if not updated_item:
            return jsonify({'error': 'Item not found'}), 404
        return jsonify({'message': 'Item updated successfully', 'item': updated_item}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/<int:item_id>', methods=['DELETE'])
def delete_from_cart(item_id):
    """Route to delete an item from the cart."""
    try:
        deleted_item = delete_cart_item(item_id)
        if not deleted_item:
            return jsonify({'error': 'Item not found'}), 404
        return jsonify({'message': 'Item deleted successfully', 'deleted_item': deleted_item}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
