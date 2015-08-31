f = open('/home/jadi/w/wikipedia/wiki_only_farsi_chars.txt', 'r')
alltext = f.read()
alltext = alltext.decode("utf-8")

allchars = {}
for i in range(0, len(alltext)):
    allchars[alltext[i]] = allchars.get(alltext[i], 0) + 1

allwordsnum = allchars[' ']
totalcharsnum = len(alltext) - allchars[' ']
del allchars[' ']
del allchars['\n']

import numpy as np
from matplotlib import pyplot as plt

letters = u'آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
lettervals =  []
letterlist = []
for letter in list(letters):
    print letter, allchars[letter]
    lettervals.append(allchars[letter]*1.0/totalcharsnum*100)

width = 1/1.5
plt.figure(figsize=(20,10))
plt.bar( range(len(lettervals)), lettervals, width)
plt.xticks([x+0.3 for x in range(len(lettervals))], list(letters), fontsize=18 )
plt.title(u'Percentage of persian letters\n10% of wikipedia articles are tested', fontsize=34)
plt.ylabel('Percent', fontsize=20)
plt.xlabel('Letter', fontsize=20)
plt.show()
