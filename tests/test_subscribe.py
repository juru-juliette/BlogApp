import unittest
from app.models import Subscription

class SubscriptionModelTest(unittest.TestCase):

    def setUp(self):
        self.new_subscriber = Subscription(id =123,name = 'banana',email='bellaxbx@gmail.com')

    
    def tearDown(self):
        Subscription.query.delete()
       


    def test_instance(self):
        self.assertTrue(isinstance(self.new_subscriber,Subscription))

    def test_init_(self):
        
        self.assertEqual(self.new_subscriber.id,123)
        self.assertEqual(self.new_subscriber.name,"banana")
        self.assertEqual(self.new_subscriber.email,"bellaxbx@gmail.com")
       