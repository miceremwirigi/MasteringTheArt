import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)
# print(doc)
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
# print(new_releases)
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
print(titles)
