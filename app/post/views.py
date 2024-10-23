from flask import Blueprint, flash, render_template
from app import db
from app.post.forms import PostForm
from app.post.models import Posts
from slugify import slugify

post = Blueprint('post', __name__, url_prefix='/post')

@post.route('/add-post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, body=form.body.data, author=form.author.data)
        post.slug = slugify(post.title)
        # Очистка формы
        form.title.data = ''
        form.author.data = ''
        form.body.data = ''
        # Добавление поста в БД
        db.session.add(post)
        db.session.commit()

        flash('Заметка создана успешно')
    return render_template('post/add_post.html', title="Записи", form=form)

@post.route('/<slug>')
def post_detail(slug):
    post = Posts.query.filter(Posts.slug == slug).first()
    return render_template('post/detail_post.html', post=post)
