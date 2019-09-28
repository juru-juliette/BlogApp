from app.models import Post
from app import db
import unittest


class PostModelTest(unittest.TestCase):
   def setUp(self):
        
        self.new_post = Post(id=1234,content='Pitch for movies',title="Tech and Game blog")

   def tearDown(self):
        
        Post.query.delete()


   def test_check_instance_variables(self):
        self.assertEquals(self.new_post.id,1234)
        self.assertEquals(self.new_post.content,'Pitch for movies')
        self.assertEquals(self.new_post.title,"Tech and Game blog")
        

   def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)  

   def test_get_post_by_id(self):

        self.new_post.save_post()
        got_posts = Post.get_post(1234)
        self.assertTrue(len(got_posts) == 1)      