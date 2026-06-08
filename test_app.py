#test_app.py
import unittest  # 1. unittest इम्पोर्ट किया
from app import hello_world

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        # 3. स्ट्रिंग को app.py के मुताबिक बदला (या app.py में बदलाव करें)
        self.assertEqual(hello_world(), "Hello , World") 

if __name__ == '__main__':  # 2. यहाँ स्पेस दिया
    unittest.main()