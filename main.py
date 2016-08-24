import requests
from lxml import html
from urlparse import urljoin
import chardet
from excel import xls

convert = lambda t: t.decode('GB2312').encode('latin1')  # .decode('gb2312')

URL = "http://www.sda.gov.cn/WS01/CL0091/index_1.html"
# URL = "http://www.sda.gov.cn/WS01/CL0006/index.html"
titles = []
urls = []

next = URL
while next:
  r = requests.get(next)
  r.encoding = "GB2312"
  tree = html.fromstring(r.text)
  tds = tree.xpath('//td')
  for td in tds:
    try:
      c = td.attrib['class']
    except KeyError:
      continue

    if not c.endswith("content"):
      continue

    items = td.xpath('//table/tbody/tr/td[@class="ListColumnClass15"]/a')

    for i in items:
      titles.append(i.text_content())
      urls.append(urljoin(next, i.attrib["href"]))

    abs_next = td.xpath('//table/tbody/tr/td[@class="pageTdE15"]/a/@href')
    if next.endswith(abs_next[0]):
      next = None
    else:
      next = urljoin(next, abs_next[0])

    break


xls(titles, urls)
