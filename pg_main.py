
import re
from WordPressAPI import WordPressAPI
WP_BLOG_URL = "https://prestissimo-guitar.com"


def clean_html(raw_html):
    clean_regex = re.compile('<.*?>')
    clean_text = re.sub(clean_regex, '', raw_html)
    return clean_text


if __name__ == '__main__':
    # https://prestissimo-guitar.com/wp-json/wp/v2/posts?categories=94
    wp_api = WordPressAPI(WP_BLOG_URL)
    posts = wp_api.get_all_posts_from_category(94)
    for post in posts:
        print(post["title"]["rendered"])
        print(clean_html(post["content"]["rendered"]))
    with open("articels.txt", "w+", encoding="utf-8") as f:
        for post in posts:
            f.write(post["title"]["rendered"])
            f.write(clean_html(post["content"]["rendered"]))


