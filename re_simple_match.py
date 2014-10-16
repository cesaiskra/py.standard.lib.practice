
import re
pattern = 'this'
text = 'does this text match the pattern ?'
match = re.search(pattern, text)
s = match.start()
e = match.end()

print 'found "%s"\nin "%s"\nfrom %d to %d ("%s")' % \
	(match.re.pattern, match.string, s, e, text[s:e])


regexes = [ re.compile(p)
			for p in [ 'this', 'that' ]
		  ]
print regexes
print 'text: %r\n' % text
for regex in regexes:
	print 'seeking "%s" ->' % regex.pattern,
	if regex.search(text):
		print 'match!'
	else:
		print 'no match'
