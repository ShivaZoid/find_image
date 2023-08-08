import os

from dotenv import load_dotenv
from google_images_search import GoogleImagesSearch
import urllib.parse


load_dotenv()

DEV_API_KEY = os.getenv('API_KEY')
CX_CODE = os.getenv('CX')


def search_image_by_name(query):
    gis = GoogleImagesSearch(DEV_API_KEY, CX_CODE)

    encoded_query = urllib.parse.quote(query, safe='')

    _search_params = {
        'q': encoded_query,
        'num': 1,
        'safe': 'off',
    }

    gis.search(search_params=_search_params)

    if gis.results():
        image_url = gis.results()[0].url
        return image_url

    return None


query = 'Dog'
image_url = search_image_by_name(query)


if image_url:
    print('Link to the image:', image_url)
else:
    print('Image not found')
