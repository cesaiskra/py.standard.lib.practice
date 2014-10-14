
import string

values = {'var':'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
	print 'substitude()	:', t.substitute(values)
except KeyError, err:
	print 'ERROR:', str(err)

print 'safe_substitute():', t.safe_substitute(values)


print t
print t.pattern
print t.pattern.pattern
