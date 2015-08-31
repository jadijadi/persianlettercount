f = open('/home/jadi/w/wikipedia/wiki_only_farsi_chars.txt', 'r')
alltext = f.read()
alltext = alltext.decode("utf-8")
allwords = alltext.split()

initialchars = {}
for word in allwords:
    initialchars[word[0]] = initialchars.get(word[0], 0) + 1

import numpy as np
from matplotlib import pyplot as plt

letters = u'آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
lettervals =  []
letterlist = []
print 'Initial letters'
for letter in list(letters):
    print letter, allchars[letter]
    lettervals.append(initialchars[letter]*1.0/allwordsnum*100)

width = 1/1.5
plt.figure(figsize=(20,10))
plt.bar( range(len(lettervals)), lettervals, width)
plt.xticks([x+0.3 for x in range(len(lettervals))], list(letters) , fontsize=18)
plt.title(u'Percentage of persian initial letters\n10% of wikipedia articles are tested', fontsize=34)
plt.ylabel('Percent', fontsize=20)
plt.xlabel('Initial Letter', fontsize=20)
plt.show()
