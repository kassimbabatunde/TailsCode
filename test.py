import unittest
from app import app
from flask import Flask

app.testing = True

class MyTestClass(unittest.TestCase):

    
    def setUp(self):
        self.app = app.test_client()

    def test_link_return(self):
        result = self.app.get('/store/hav/')
        self.assertEqual(result.data,b'Newhaven')

    def tearDown(self):
        pass

if __name__ =="__main__":
    unittest.main()