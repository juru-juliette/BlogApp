from app.models import Post,User,Comment
from app import db
import unittest


class CommentModelTest(unittest.TestCase):
   def setUp(self):
      
        self.new_post = Post(id=12,content='blog',title='juru')
        self.new_comment=Comment(id=1233,content="deal",post=self.new_post)

   def tearDown(self):
        Comment.query.delete()

        Post.query.delete()

   

   def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,1233)
        self.assertEquals(self.new_comment.content,'deal')
        
        self.assertEquals(self.new_comment.post,self.new_post)
        

   def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)  

   def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12)
        self.assertTrue(len(got_comments) == 1)      