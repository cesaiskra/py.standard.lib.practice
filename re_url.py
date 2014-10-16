
import re
from re_material import *

print host_pattern
url = re.compile(host_pattern)


for match in re.findall(url,text):
	print match
