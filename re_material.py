
import re


text = """
Welcome to RegExr v2.0 by gskinner.com!

Edit the Expression & Text to see matches. Roll over matches or the expression for details. Undo mistakes with ctrl-z. Save & Share expressions with friends or the Community. A full Reference & Help is available in the Library, or watch the video Tutorial.

Sample text for testing:
abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 +-.,!@#$%^&*();\/|<>"'
12345 -98.7 3.141 .6180 9,000 +42
555.123.4567	+1-(800)-555-2468
foo@demo.net	bar.ba@test.co.uk
www.demo.com	http://foo.co.uk/
http://www.jonas.no/~webs(i)der/jon_as.php 
http://www.yahoo.com/net//ore
http://regexr.com/foo.html?q=bar
3SquareBand.com 
asp.net  
rmy.mil
"""
url_pattern =re.compile(r'http://([a-zA-Z0-9_\-]+)([\.][a-zA-Z0-9_\-]+)+([/][a-zA-Z0-9\~\(\)_\-]*)+([\.][a-zA-Z0-9\(\)_\-]+)*$')

host_pattern =re.compile(r'^[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU)$')

d = re.compile(r'[0-9]{4}')

match = d.search(text)
for match in re.findall(text):
	print  match


