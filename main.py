from helper import clean_html
from wordpress_api_connector.WordPressAPI import WordPressAPI

WP_BLOG_URL = "https://creatronix.de"


if __name__ == '__main__':
    wp_api = WordPressAPI(WP_BLOG_URL)
    number_of_posts = wp_api.get_number_of_posts()
    print("Number of posts: " + str(number_of_posts))
    categories = wp_api.get_categories()
    print("Number of categories: " + str(len(categories)))
    category_names = []
    for cat in categories:
        category_names.append((cat['id'], cat['name']))
    print("Number of posts per category: ")
    for cat in category_names:
        print(cat[1] + " " + str(wp_api.get_number_of_posts_per_category(cat[0])))

    posts = wp_api.get_all_posts_from_category(150)
    for post in posts:
        print(post["title"]["rendered"])
        print(clean_html(post["content"]["rendered"]))
    with open("data_science_articles.txt", "w+", encoding="utf-8") as f:
        for post in posts:
            f.write(post["title"]["rendered"])
            f.write(clean_html(post["content"]["rendered"]))
