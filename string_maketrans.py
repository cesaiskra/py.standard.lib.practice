
import string
leet = string.maketrans('abcdefghij','0123456789')
s = 'the quick brown fox jumped over the laze dog.'

print s
print s.translate(leet)
