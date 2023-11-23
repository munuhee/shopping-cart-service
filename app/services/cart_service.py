"""
This module provides functions to manage a shopping cart using CartItem objects.
"""
from app.models import db, CartItem

def serialize_cart_item(cart_item):
    """Serialize a CartItem object into a dictionary."""
    return {
        'id': cart_item.id,
        'product_name': cart_item.product_name,
        'quantity': cart_item.quantity,
        'price': cart_item.price
    }

def add_item_to_cart(product_name, quantity, price):
    """Add a new item to the cart."""
    new_item = CartItem(product_name=product_name, quantity=quantity, price=price)
    db.session.add(new_item)
    db.session.commit()
    return serialize_cart_item(new_item)

def get_cart_items():
    """Retrieve all items in the cart."""
    cart_items = CartItem.query.all()
    return [serialize_cart_item(item) for item in cart_items]

def get_cart_item_by_id(item_id):
    """Retrieve a cart item by its ID."""
    cart_item = db.session.get(CartItem, item_id)
    return serialize_cart_item(cart_item) if cart_item else None

def update_cart_item(item_id, data):
    """Update a cart item with new data."""
    cart_item = db.session.get(CartItem, item_id)
    if not cart_item:
        return None

    for key, value in data.items():
        setattr(cart_item, key, value)

    db.session.commit()
    return serialize_cart_item(cart_item)

def delete_cart_item(item_id):
    """Delete a cart item by its ID."""
    cart_item = db.session.get(CartItem, item_id)
    if not cart_item:
        return None

    db.session.delete(cart_item)
    db.session.commit()
    return serialize_cart_item(cart_item) if cart_item else None
