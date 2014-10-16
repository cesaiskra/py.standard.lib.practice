import re
from re_material import text,url_pattern 

pattern = re.compile('[A-Z]+')

for match in re.findall(pattern, text):
	print 'found "%s" ' % match



###finditer() returns an iterator that produces match instances 
###instead of the strings returned by findall()
for match in re.finditer(pattern, text):
	s = match.start()
	e = match.end()
	print match
	print 'found "%s" at %d:%d' % (text[s:e], s,e)

