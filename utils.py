import json

def get_posts_all() -> list[dict]:
    """
    Функция получения постов из JSON файла
    :return: словарь с постами
    """
    with open('data/data.json', 'r', encoding = 'utf8') as file:
        posts = json.load(file)
        return posts

def get_posts_by_user(user_name: object) -> object:
    """
    Функция получения поста по имени автора
    :param user_name: имя автора поста
    :return: пост
    """
    post_by_user = get_posts_all()
    posts_by_user = []
    try:
        for post in post_by_user:
            if post['poster_name'] == user_name:
                posts_by_user.append(post)
        return posts_by_user
    except ValueError:
        return 'Ошибка'


def get_comments_by_post_id(post_id) -> object:
    """
    Функция получения комментария по ID поста
    :param post_id: ID поста к которому написан комментарий
    :return: комментарий к посту
    """
    with open('data/comments.json', 'r', encoding='utf8') as file:
        comments_from_json = json.load(file)
        comments = []
        for comment in comments_from_json:
            if comment['post_id'] == post_id:
                comments.append(comment)
        return comments

def search_for_posts(query):
    """
    Функция возвращает список постов по ключевому слову
    :param query:
    :return: пост или сообщение, что пост не найден
    """
    all_posts = get_posts_all()
    search_posts = []
    for post in all_posts:
        if query.lower() in post['content'].lower():
            search_posts.append(post)
    return search_posts

def get_post_by_pk(pk):
    """
    Функция получает пост по порядковому номеру (pk)
    :param pk: pk from JSON
    :return: post
    """
    post_by_pk = get_posts_all()
    for post in post_by_pk:
        if post['pk'] == pk:
            return post

