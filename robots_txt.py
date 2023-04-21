import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    response = http.request('GET', url)
    soup = str(BeautifulSoup(response.data,features="html.parser"))
    return soup
#print(get_robots_txt('www.youtube.com'))