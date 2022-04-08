from wordpress_api_connector import WordPressAPI

WP_BLOG_URL = "https://creatronix.de"

def test_create_connector():

    wp_connector = WordPressAPI(WP_BLOG_URL)
    assert wp_connector

def test_get_number_of_posts():
    wp_connector = WordPressAPI(WP_BLOG_URL)
    number_of_posts = wp_connector.get_number_of_posts()
    print(f"Number of posts: {number_of_posts}")
    assert number_of_posts >= 100

def test_get_categories():
    wp_connector = WordPressAPI(WP_BLOG_URL)
    categories = wp_connector.get_categories()
    print(categories)
    assert categories[0]["slug"] == "3d-printing"

def test_list_posts_without_featured_image():
    wp_connector = WordPressAPI(WP_BLOG_URL)
    pwfi = wp_connector.list_posts_without_featured_image()
    assert len(pwfi) != 0
