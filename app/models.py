"""Defines the CartItem model for a shopping cart."""

from app import db

class CartItem(db.Model):
    """Model representing items in a shopping cart."""
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the CartItem object.
        """
        return f"<CartItem {self.id}: {self.product_name}>"
