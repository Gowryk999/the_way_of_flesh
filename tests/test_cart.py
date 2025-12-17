import pytest

class TestCart:
    
    def test_add_item_to_cart(self):
        cart = []
        cart.append("item1")
        assert len(cart) == 1
        assert "item1" in cart
    
    def test_remove_item_from_cart(self):
        cart = ["item1", "item2", "item3"]
        cart.remove("item2")
        assert len(cart) == 2
        assert "item2" not in cart
    
    def test_cart_total_calculation(self):
        items = [
            {"name": "item1", "price": 10.0, "quantity": 2},
            {"name": "item2", "price": 5.0, "quantity": 1}
        ]
        
        total = sum(item["price"] * item["quantity"] for item in items)
        assert total == 25.0
    
    @pytest.mark.parametrize("items,expected_total", [
        ([{"price": 10, "quantity": 2}], 20),
        ([{"price": 5, "quantity": 3}, {"price": 2, "quantity": 1}], 17),
        ([], 0)
    ])
    def test_cart_with_different_items(self, items, expected_total):
        total = sum(item["price"] * item["quantity"] for item in items)
        assert total == expected_total
