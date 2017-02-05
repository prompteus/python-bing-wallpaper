from platform import system 

if system() == "Windows":
	import ctypes
	def change_wallpaper(uri):
		print("Windows are not supported.")

elif system() == "Darwin":
	from os import system as s
	def change_wallpaper(uri):
		s('osascript -e \'tell application "Finder" to set desktop picture to POSIX file "{0}"\' && killall Dock'.format(uri))

elif system() == "Linux":
	import subprocess
	import os
	from os import system as s

	def get_output(command):
		p = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		out, err = p.communicate()
		return out 

	GSETTINGS_COMMAND = 'gsettings set org.gnome.desktop.background picture-uri "file://{0}"'

	try:
		if int(get_output("gnome-session --version").split()[-1][0]) == 3:
			def change_wallpaper(uri):
				s(GSETTINGS_COMMAND.format(uri))
	except:
		if os.environ.get('DESKTOP_SESSION') == 'pantheon':
			def change_wallpaper(uri):
				s(GSETTINGS_COMMAND.format(uri))
		else:
			raise OSError("Wallaper change is only supported in GNOME 3, Unity and Pantheon")