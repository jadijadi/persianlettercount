import re

inputText = '/home/jadi/w/wikipedia/wiki_fa.txt'
f = open(inputText, 'r')
alltext = f.read()
text = alltext
text=re.sub("\n", " ", text)
text=re.sub("\[+", "[", text)
text=re.sub("\]+", "]", text)
text=re.sub("\{+", "{", text)
text=re.sub("\}+", "}", text)
text=re.sub("{.*?}", " ", text)
text=re.sub("\<.*?\>", " ", text)
text=re.sub("\[.*?\]", " ", text)
text=re.sub("\s+", " ", text)

# changing some arabic chars to correct persian ones
text=re.sub(u"ي", u"ی", text)
text=re.sub(u"ك", u"ک", text)


print text
