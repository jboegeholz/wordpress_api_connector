import datetime
from csv_export import write_csv
from WordPressAPI import WordPressAPI
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
