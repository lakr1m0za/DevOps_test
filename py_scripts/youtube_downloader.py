#YouTube Dowloader

import webbrowser

url = input("Input link to YouTube video: ")
url = url[:12] + 'ss' + url[12:]
webbrowser.open(url)