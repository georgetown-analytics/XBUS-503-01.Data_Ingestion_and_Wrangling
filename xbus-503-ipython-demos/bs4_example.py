import requests
from bs4 import BeautifulSoup


def get_source():
    response = requests.get('http://georgetown.edu')
    return response.text


def main():
    soup = BeautifulSoup(get_source(), "html5lib")
    html_id = 'block-views-v11-related-content-block-3'

    for item in soup.select("p.news-title a"):
        print(item.string)


if __name__ == '__main__':
    main()
