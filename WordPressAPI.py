import math
import requests
from typing import List


class WordPressAPI(object):
    def __init__(self, wp_url: str, results_per_page: int = 20):
        self.wp_api_url = wp_url + "/wp-json/wp/v2"
        self.results_per_page = results_per_page

    def get_posts(self) -> List:
        api_function = "/posts"
        number_of_elements = self.get_number_of_posts()
        return self.get_elements(api_function, number_of_elements)

    def get_number_of_posts(self) -> int:
        r = requests.get(self.wp_api_url + "/posts")
        return int(r.headers["X-WP-Total"])

    def get_number_of_categories(self) -> int:
        r = requests.get(self.wp_api_url + "/categories")
        return int(r.headers["X-WP-Total"])

    def get_number_of_posts_per_category(self, category):
        api_function = "/posts?categories=" + str(category)
        r = requests.get(self.wp_api_url + api_function)
        return int(r.headers["X-WP-Total"])

    def get_categories(self) -> List:
        api_function = "/categories"
        number_of_elements = self.get_number_of_categories()
        return self.get_elements(api_function, number_of_elements)

    def get_elements(self, api_function, number_of_elements):
        number_of_pages = math.ceil(number_of_elements / self.results_per_page)
        results = []
        for page in range(1, number_of_pages + 1):
            query_string = "".join((api_function, "?per_page=", str(self.results_per_page), "&page=", str(page)))
            url = "".join((self.wp_api_url, query_string))
            r = requests.get(url)
            json_data = r.json()
            results += json_data
        return results
