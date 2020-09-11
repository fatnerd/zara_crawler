from js_crawler import Crawler
from line_notify import Notify
import datetime

link = input('plz paste url:')
c = Crawler()
scraped = c.scrape(link)

token = 'lIL6AbXccBARkhlrGuM6QS1PsmVuh5Oy6WeNPdilpxl'
notify = Notify(token)
notify.send(scraped)
