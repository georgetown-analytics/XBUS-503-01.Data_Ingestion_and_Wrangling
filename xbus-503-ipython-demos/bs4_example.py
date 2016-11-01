import requests
from bs4 import BeautifulSoup


def get_source():
    response = requests.get('http://georgetown.edu')
    return response.text


def main():
    soup = BeautifulSoup(get_source())
    html_id = 'block-views-v11-related-content-block-3'

    for h5 in soup.find(id=html_id).find_all('h5'):
        print(h5.find('a').string)


if __name__ == '__main__':
    main()
