from flask import Blueprint, flash, render_template
from app import db
from app.post.forms import PostForm
from app.post.models import Posts

post = Blueprint('post', __name__)

@post.route('/add-post', methods=['GET', 'POST'])
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
    return render_template('post/add_post.html', title="Записи", form=form)