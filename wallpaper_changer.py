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

	GSETTINGS_COMMAND = 'gsettings set org.gnome.desktop.background picture-uri "file://{0}"'

	# Only Gnome3 based desktop environments are supported
	def change_wallpaper(uri):
		s(GSETTINGS_COMMAND.format(uri))