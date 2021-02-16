from lxml import html
import requests

page = requests.get('https://firstascentclimbing.com/uptown/yoga-classes/')
tree = html.fromstring(page.content)


teachers = tree.xpath('//div[contains(string(),"bw-session__staff")]')

print(teachers)