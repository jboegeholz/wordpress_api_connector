import requests


def get_posts():
    url = "https://creatronix.de/wp-json/wp/v2/posts"
    r = requests.get(url + "?per_page=100")
    posts = r.json()
    for post in posts:
        print(post["title"]["rendered"] + " " + post["link"])


def create_schedule():
    pass


if __name__ == '__main__':
    get_posts()
    create_schedule()
