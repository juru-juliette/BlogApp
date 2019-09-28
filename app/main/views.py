from flask import render_template,request,redirect,url_for, abort
from . import main
from .forms import CommentForm,UpdateProfile,AddPostForm,UpdatePostForm
from .. import db,photos
from ..models import User,Post,Comment
from flask_login import login_required, current_user
from ..email import mail_message

@main.route('/', methods = ['GET', 'POST'])
def index():
  '''
    View root page function that returns the index page and its data
    '''
  

#   return redirect(url_for('main.index'))
  
  posts=Post.get_posts()
  title="Home| Welcome to MeBlog"

  return render_template('index.html',title=title,posts=posts)

@main.route('/post/<int:id>')
def single_post(id):
    post=Post.query.filter_by(id=id).first()
    comments=Comment.get_comments(id=id)
    return render_template('single_post.html',post=post,comments=comments)

@main.route('/delete/comment/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_comment(id):
    comment=Comment.query.filter_by(id=id).first()
 

    if comment is not None:
       comment.delete_comment()
       return redirect(url_for('main.index'))

@main.route('/delete/post/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_post(id):
    post=Post.query.filter_by(id=id).first()
 

    if post is not None:
       post.delete_post(id)
       return redirect(url_for('main.index'))

 

@main.route('/post/new', methods = ['GET', 'POST'])
@login_required
def add_post():
    form = AddPostForm()
    
    if form.validate_on_submit():
        title = form.title.data

        post= form.content.data

        new_post = Post(content=post, title = title)
        new_post.save_post()

        
        return redirect(url_for('main.index'))

    

    title = 'Add Post| MeBlog'    
    return render_template('post.html', title = title, post_form = form)


@main.route('/new/comment/<int:id>', methods = ['GET','POST'])
def add_comment(id):
  post=Post.query.filter_by(id=id).first()
  if post is None:
    abort(404)

  form=CommentForm()
  if form.validate_on_submit():
     name=form.username.data
     comment=form.comment.data
     new_comment=Comment(content=comment ,post=post,username=name)
     db.session.add(new_comment)  
     db.session.commit() 
     
     return redirect(url_for('main.index'))
  return render_template('comment.html', comment_form=form)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/edit/post/<int:id>',methods= ['GET','POST'])
@login_required
def update_post(id):
   post=Post.query.filter_by(id=id).first()
   if post is None:
        abort(404)

   form=UpdatePostForm()
#    form.title.data=post.title
#    form.content.data=post.content
#    post1=Post.query.filter_by(id=id).first()
   if form.validate_on_submit():
         post.title=form.title.data
         post.content=form.content.data

         db.session.add(post)
         db.session.commit()

         return redirect(url_for('main.index'))
   return render_template('update_post.html',form=form)
