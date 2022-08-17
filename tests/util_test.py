import pytest
from json import JSONDecodeError
from utils import *

def test_get_posts_all_file_error():
    with pytest.raises(FileNotFoundError):
        get_posts_all()

def test_get_posts_all_json_error():
    with pytest.raises(JSONDecodeError):
        get_posts_all()

def test_get_comments_file_error():
    with pytest.raises(FileNotFoundError):
        get_comments_by_post_id()

def test_get_comments_json_error():
    with pytest.raises(JSONDecodeError):
        get_comments_by_post_id()