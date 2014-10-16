
import re

def test_patterns(text, patterns=[]):
	#desc means descrpition of patterns
	for pattern, desc in patterns:
		print 'pattern %r (%s)\n' % (pattern,desc)
		print ' %r' % text
		for match in re.finditer(pattern, text):
			s = match.start()
			e = match.end()
			substr = text[s:e]
			n_backslashed = text[:s].count('\\')
			prefix = '.' * (s + n_backslashed)
			print ' %s%r %d:%d' % (prefix, substr, s,e)
		print
	return

if __name__ == '__main__':
	test_patterns('ab 12 cd 222 e 99',
				   [('\d{2}' , "nuberms in two") ]
				)
	
	test_patterns(
			'abbaabbba',
			[ 
			('ab*',	'a fllowed by zero or more b'),
			('ab+', 'a followed one or more b'),
			('ab?', 'a followed by zero or one b'),
			('ab{3}', 'a followed by three b'),
			('ab{2,3}', 'a followd by two or three b'),
			]
				)
			
	test_patterns(
		'this is some text -- with punctuation. -yes!' ,
		[ ('[^-. ]+' , 'sequences without -, ., or space') , ]

				)
