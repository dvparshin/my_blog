from flask import Blueprint, render_template
from app.post.models import Posts

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template('main/index.html', title="Главная", posts=posts)