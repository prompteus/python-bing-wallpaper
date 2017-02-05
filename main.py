import change_wallpaper
from urllib.request import urlopen
from urllib.error import URLError
import json

try:
	response = urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
	data = response.read().decode("utf-8")
	print(json.loads(data))
except URLError:
	print("No internet connection!")