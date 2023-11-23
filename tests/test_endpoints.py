import os
import unittest
from app import app, db

class TestShoppingCartRoutes(unittest.TestCase):

    def setUp(self):
        """Set up a test environment."""
        app.config.from_pyfile('config.py')
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def test_get_cart(self):
        with app.app_context():
            response = self.app.get('/cart')
            self.assertEqual(response.status_code, 200)

    def test_get_cart_item_not_found(self):
        with app.app_context():
            response = self.app.get('/cart/999')
            self.assertEqual(response.status_code, 404)

    def test_add_to_cart_missing_data(self):
        with app.app_context():
            data = {
                'product_name': 'Test Product',
                'quantity': 2
            }
            response = self.app.post('/cart/add', json=data)
            self.assertEqual(response.status_code, 400)

    def test_update_cart_item_not_found(self):
        with app.app_context():
            data = {
                'product_name': 'Updated Test Product',
                'quantity': 3,
                'price': 15.99
            }
            response = self.app.put('/cart/999', json=data)
            self.assertEqual(response.status_code, 404)

    def test_delete_from_cart_item_not_found(self):
        with app.app_context():
            response = self.app.delete('/cart/999')
            self.assertEqual(response.status_code, 404)

    def test_add_and_retrieve_item(self):
        with app.app_context():
            data = {
                'product_name': 'New Test Product',
                'quantity': 5,
                'price': 20.50
            }
            add_response = self.app.post('/cart/add', json=data)
            self.assertEqual(add_response.status_code, 201)

            item_id = add_response.json['item']['id']
            get_response = self.app.get(f'/cart/{item_id}')
            self.assertEqual(get_response.status_code, 200)
            self.assertEqual(get_response.json['cart_item']['product_name'], 'New Test Product')

            delete_response = self.app.delete(f'/cart/{item_id}')
            self.assertEqual(delete_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
