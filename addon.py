from xbmcswift2 import Plugin
import urllib 
from BeautifulSoup import BeautifulSoup as BS

plugin = Plugin()

BASE_URL = 'http://www.gamekings.tv/videos/' 
STREAM_URL = 'http://stream.gamekings.tv/large/'


def get_video_link(page):
    src = urllib.urlopen(page)
    html = BS(src)
    video_url = html.find('meta',{"property" : 'og:video'}).get('content')
    video_image = html.find('meta',{"property" : 'og:image'}).get('content')
    video_description = html.find('meta',{"property" : 'og:description'}).get('content')
    video_title = html.find('meta',{"property" : 'og:title'}).get('content')
    video = {
            'path': video_url,
            'label' : video_title, 
            'info' : {video_description,},
            'thumbnail' : video_image,
            'is_playable': True,
    }
    return video



@plugin.route('/')
def main_menu():
    items = []
    src = urllib.urlopen(BASE_URL)
    html = BS(src)
    for video in html.findAll('article'):
        video_link = video.find('a').get('href')
        items.append(get_video_link(video_link))

    return items

if __name__ == '__main__':
    plugin.run()
