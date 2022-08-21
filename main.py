import logging
from json import JSONDecodeError

from utils import get_posts_all, get_post_by_pk, get_posts_by_user, get_comments_by_post_id, search_for_posts
from flask import Flask, render_template, request, abort, jsonify
api_logger = logging.getLogger("api_logger")

app = Flask(__name__)

logging.basicConfig(filename='basic.log', level=logging.INFO)

@app.route('/')
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>/')
def post_page(post_id):
    post_by_id = get_post_by_pk(post_id)
    if post_by_id is None:
        abort(404)
    comments = get_comments_by_post_id(post_id)
    comment_num = len(comments)
    return render_template('post.html', post_by_id=post_by_id, comments=comments, comment_num=comment_num)


@app.route('/search/')
def search_page():
    search_query = request.args['s']
    try:
        posts = search_for_posts(search_query)
        search_post_num = len(posts)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('search.html', query=search_query, posts=posts, search_post_num=search_post_num)


@app.route('/users/<username>/')
def user_page(username):
    posts_by_user = get_posts_by_user(username)
    return render_template('user-feed.html', posts_by_user=posts_by_user)


@app.errorhandler(404)
def page_error_404(error):
    return f'Такой страницы не существует {error}', 404

@app.errorhandler(500)
def page_error_500(error):
    return f'На сервере произошла ошибка {error}', 500

@app.route('/api/posts/')
def api_posts_all():
    all_posts = get_posts_all()
    api_logger.debug('Запрошены все посты')
    return jsonify(all_posts)

@app.route('/api/posts/<int:pk>/')
def api_posts_single(pk):
    post = get_post_by_pk(pk)

    if post is None:
        api_logger.debug('Обращение к несуществующему посту')
        abort(404)
    api_logger.debug(f'Обращение к посту {pk}')
    return jsonify(post)

if __name__ == '__main__':
    app.run()