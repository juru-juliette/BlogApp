import unittest
from app.models import Quote
# Movie = movie.Movie

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote(1234,'Fred Brooks','No such faith comforts the software engineer.')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))

    def test_init_(self):
        
        self.assertEqual(self.new_quote.id,1234)
        self.assertEqual(self.new_quote.author,"Fred Brooks")
        self.assertEqual(self.new_quote.content,"No such faith comforts the software engineer.")