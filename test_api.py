import unittest
from api import app

class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_add(self):
        response = self.client.get("/add?a=10&b=20")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 30)
        print("Addition test passed")

    def test_subtract(self):
        response = self.client.get("/subtract?a=20&b=20")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 0)  # Verifica che 20 - 20 sia uguale a 0
        print("Subtraction test passed")

    def test_multiply(self):
        response = self.client.get("/multiply?a=5&b=4")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 20)
        print("Multiplication test passed")

    def test_divide(self):
        response = self.client.get("/divide?a=20&b=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 4)
        print("Division test passed")

    def test_power(self):
        response = self.client.get("/power?a=2&b=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 8)
        print("Power test passed")

    def test_square_root(self):
        response = self.client.get("/square_root?a=16")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 4)
        print("Square root test passed")

    def test_modulus(self):
        response = self.client.get("/modulus?a=10&b=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], 1)
        print("Modulus test passed")

if __name__ == "__main__":
    unittest.main()
