import change_wallpaper
from urllib.request import urlopen
from urllib.error import URLError
import json


BING_TODAY_JSON_URL = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
BING_BASE_DOMAIN = "http://www.bing.com"


try:
	bing_today_json = urlopen(BING_TODAY_JSON_URL).read().decode("utf-8")
	wallpaper_relative_url = json.loads(bing_today_json)['images'][0]['url']
	wallpaper_url = BING_BASE_DOMAIN + wallpaper_relative_url
	print(wallpaper_url)
except URLError:
	print("No internet connection!")
