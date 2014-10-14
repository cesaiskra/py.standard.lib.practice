
import string

template_text = '''
delimiter 	: %%
replaced	: %with_underscore
ignored		: %notunderscored
'''

d = { 'with_underscore':'replaced',
	  'notunderscored':'not replaced',
		}

class MyTemplate(string.Template):
	delimiter = '%'
	idpattern = '[a-z]+_[a-z]+'

t = MyTemplate(template_text)
print 'modified Id pattern:'
print t.safe_substitute(d)


print t
print t.pattern
print t.pattern.pattern



