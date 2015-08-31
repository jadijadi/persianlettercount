import xml.etree.ElementTree as etree
import re
import random

inFile = '/home/jadi/w/wikipedia/fawiki-20150807-pages-articles.xml'

random.seed()
counter = 0

for event, elem in etree.iterparse(inFile, events=('start', 'end', 'start-ns', 'end-ns')):
    if random.random() < 0.9: #only work on 10% of articles
        try:
            elem.clear()
        except:
            pass
        continue

    thisTxt = None
    try:
        if elem.tag.endswith('/}text'):
            thisTxt = elem.text
            elem.clear()
    except:
        continue
        
    if not thisTxt:
        elem.clear()
        continue
        
print thisTxt
