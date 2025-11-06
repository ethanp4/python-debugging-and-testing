import unittest
from main import Order  

class TestOrder(unittest.TestCase):
 
    def setUp(self):
        self.order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
 
    def test_add_item(self):
        self.order.add_item("Notebook", 3, 5.00)
        self.assertIn(("Notebook", 3, 5.00), self.order.items)
 
    def test_remove_item(self):
        self.order.remove_item("Pen")
        items = [i[0] for i in self.order.items]
        self.assertNotIn("Pen", items)
 
    def test_calculate_total(self):
        total = self.order.calculate_total()
        self.assertTrue(isinstance(total, (int, float)))
 
    def test_apply_discount(self):
        self.assertEqual(self.order.apply_discount("SAVE10"), 0.1)
        self.assertEqual(self.order.apply_discount("SAVE20"), 0.2)
        self.assertEqual(self.order.apply_discount("SAVE30"), 0.3)
        self.assertEqual(self.order.apply_discount("INVALID"), 0)
 
if __name__ == "__main__":
    unittest.main(verbosity=2)