from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os
import time
import sys

# info of API key

key = "91d7d4a2e7e1c8d76de71b03926a99c8"
secret = "7667516871f241b5"

wait_time = .1
animal_name = sys.argv[1]
savedir = "./" + animal_name

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text=animal_name,
    per_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, licence'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    print(i)
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
