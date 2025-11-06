import unittest
from main import Order  

class TestOrder(unittest.TestCase):
 
    def setUp(self):
        self.order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
 
    def test_add_item(self):
        expected_new_size = len(self.order.items) + 1
        self.order.add_item("Notebook", 3, 5.00)
        self.assertIn(("Notebook", 3, 5.00), self.order.items) #verify item is present
        self.assertEqual(len(self.order.items), expected_new_size) #verify size increased

    def test_remove_item(self):
        expected_new_size = len(self.order.items) - 1
        self.order.remove_item("Pen")
        items = [i[0] for i in self.order.items]
        self.assertNotIn("Pen", items) #verify item is removed
        self.assertEqual(len(self.order.items), expected_new_size) #verify size decreased

    def test_calculate_total(self):
        total = self.order.calculate_total()
        expected_total = (2 * 15.00) + (5 * 1.50)  # 30.00 + 7.50 = 37.50
        self.assertAlmostEqual(total, expected_total) # verify total calculation
        self.assertTrue(isinstance(total, (int, float))) #verify type

    def test_apply_discount(self):
        self.assertEqual(self.order.apply_discount("SAVE10"), 0.1)
        self.assertEqual(self.order.apply_discount("SAVE20"), 0.2)
        self.assertEqual(self.order.apply_discount("SAVE30"), 0.3)
        self.assertEqual(self.order.apply_discount("INVALID"), 0) #an invalid code will add no discount
 
if __name__ == "__main__":
    unittest.main(verbosity=2)