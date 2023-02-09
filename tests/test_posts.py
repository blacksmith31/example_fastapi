from app import schemas
import pytest 


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    def validate(post):
        return schemas.PostOut(**post)
    posts_map = map(validate, res.json())
    # posts_map = list(posts_map)
    # posts_comp = [schemas.PostOut(**post) for post in res.json()]
    # print(f"posts map: {posts_map}")
    # print(f"posts comprehension: {posts_comp}")
    # assert posts_map == posts_comp
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200

def test_unauth_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauth_user_get_one_posts(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/888888")
    assert res.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    print(res.json())
    # post = schemas.PostOut(**res.json())
    # print(post)

@pytest.mark.parametrize("title, content, published",[
    ("awesome new title", "awesome new content", True),
    ("favorite pizza", "pepperoni", False),
    ("tallest skyscrapers", "its in dubai", True)
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    res = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']
    
