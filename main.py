import requests
import math
import datetime
from csv_export import write_csv

WP_BLOG_URL = "https://creatronix.de/wp-json/wp/v2/posts"
POSTS_PER_PAGE = 100
DATE_FORMAT = '%d/%m/%Y %H:%M'


def get_posts(url, number_of_pages):
    for page in range(1, number_of_pages+1):
        query_string = "?per_page=" + str(POSTS_PER_PAGE) + "&page=" + str(page)
        r = requests.get(url + query_string)
        posts = r.json()
        for post in posts:
            print(post["title"]["rendered"] + " " + post["link"])


def create_schedule(start_date):
    # csv format
    # tt/mm/jjjj hh:mm, message, url
    print(start_date.strftime(DATE_FORMAT))
    write_csv("schedule", ["tt/mm/jjjj hh:mm", "message", "url"])


def get_number_of_posts(url):
    r = requests.get(url)
    return r.headers["X-WP-Total"]


if __name__ == '__main__':
    #number_of_posts = get_number_of_posts(url=WP_BLOG_URL)
    #print("Number of Articles", number_of_posts )
    #number_of_pages = math.ceil(int(number_of_posts) / POSTS_PER_PAGE)
    #get_posts(url=WP_BLOG_URL, number_of_pages=number_of_pages)

    create_schedule(datetime.datetime.now())
