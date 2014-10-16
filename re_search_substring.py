import re

text = 'this is some text'
pattern = re.compile(r'\b\w*is\w*\b')

print 'TEXT:', text
print

pos = 0
while True:
	match = pattern.search(text, pos)
	if not match:
		break
	s = match.start()
	e = match.end()
	print ' %2d : %2d = "%s" ' % \
		(s, e-1, text[s:e])
	pos = e

