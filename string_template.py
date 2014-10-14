
import string

values = {'var':'foo'}

t = string.Template("""
Variable 			: $var
Escape				: $$
Variable in text	: ${var}iable
""")

print 'Template:', t.substitute(values)

s = """
Variable 			:%(var)s
Escape				:%%
variable in text	: %(var)siable
"""

print 'INTERPOLATION:', s % values

v = {'name':'cesa'}
template = string.Template("""
my name is $name
""")
print template.substitute(v)
