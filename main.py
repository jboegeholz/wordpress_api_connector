import datetime
from csv_export import write_csv
from WordPressAPI import WordPressAPI
WP_BLOG_URL = "https://creatronix.de"

DATE_FORMAT = '%d/%m/%Y %H:%M'




def create_schedule(start_date):
    # csv format
    # tt/mm/jjjj hh:mm, message, url
    print(start_date.strftime(DATE_FORMAT))
    write_csv("schedule", ["tt/mm/jjjj hh:mm", "message", "url"])


if __name__ == '__main__':
    wp_api = WordPressAPI(WP_BLOG_URL)
    number_of_posts = wp_api.get_number_of_posts()
    #posts = wp_api.get_posts()
    categories = wp_api.get_categories()
    print(categories)
    #create_schedule(datetime.datetime.now())
