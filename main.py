from urllib.request import urlopen, urlretrieve
from urllib.error import URLError
import json
import os
import errno
from wallpaper_changer import change_wallpaper

BING_TODAY_JSON_URL = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
BING_BASE_DOMAIN = "http://www.bing.com"
LOCAL_WALLPAPER_FILEPATH = os.path.expanduser("~/") + ".bing-wallpaper/"


def make_sure_path_exists(path):
	os.makedirs(path, exist_ok=True)


def clear_folder(folder):
	for file in os.listdir(folder):
		file_path = os.path.join(folder, file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print(e)

def main():
	try:
		bing_today_json = urlopen(BING_TODAY_JSON_URL).read().decode("utf-8")
		wallpaper_relative_url = json.loads(bing_today_json)['images'][0]['url']
		wallpaper_filename = wallpaper_relative_url.split("/")[-1]
		wallpaper_url = BING_BASE_DOMAIN + wallpaper_relative_url
		wallpaper_local_file_pathname = LOCAL_WALLPAPER_FILEPATH + wallpaper_filename
		make_sure_path_exists(LOCAL_WALLPAPER_FILEPATH)
		clear_folder(LOCAL_WALLPAPER_FILEPATH)
		urlretrieve(wallpaper_url, wallpaper_local_file_pathname)
		change_wallpaper(wallpaper_local_file_pathname)
	except:
		raise

if __name__ == "__main__":
	main()
