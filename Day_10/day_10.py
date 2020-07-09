import requests
import re

url = input('Enter a URL (Example : google.com): ')
abs_url = 'http://www.' + url

website = requests.get(abs_url)

html = website.text

links = re.findall('"((http|ftp)s?://.*?)"', html)

for link in links:
    print(link[0])
