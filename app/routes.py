from app import app, db
from app.forms import PostForm
from flask import render_template, flash
import sqlalchemy as sa
from app.models import Posts

@app.route('/')
def index():
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template('index.html', title="Главная", posts=posts)

@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data, author=form.author.data, slug=form.slug.data)
        # Очистка формы
        form.title.data = ''
        form.content.data = ''
        form.author.data = ''
        form.slug.data = ''
        # Добавление поста в БД
        db.session.add(post)
        db.session.commit()

        flash('Заметка создана успешно')
    return render_template('add_post.html', title="Записи", form=form)