import math
import requests
from typing import List


class WordPressAPI(object):
    def __init__(self, wp_url: str, posts_per_page: int=20):
        self.wp_api_url = wp_url + "/wp-json/wp/v2"
        self.posts_per_page = posts_per_page

    def get_posts(self)-> List:
        number_of_pages = math.ceil(self.get_number_of_posts() / self.posts_per_page)
        posts = []
        for page in range(1, number_of_pages + 1):
            query_string = "/posts?per_page=" + str(self.posts_per_page) + "&page=" + str(page)
            r = requests.get(self.wp_api_url + query_string)
            json_data = r.json()
            posts += json_data
        return posts

    def get_number_of_posts(self)-> int:
        r = requests.get(self.wp_api_url + "/posts")
        return int(r.headers["X-WP-Total"])

    def get_number_of_categories(self) -> int:
        r = requests.get(self.wp_api_url + "/categories")
        return int(r.headers["X-WP-Total"])

    def get_categories(self) -> List:
        query_string = "/categories?per_page=20"
        categories = requests.get(self.wp_api_url + query_string)
        return categories.json()
