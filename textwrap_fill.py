
import textwrap
from textwrap_example import sample_text as text

print 'No dedent:\n'
print textwrap.fill(text,width=50)

print 'dedent:\n'
print textwrap.dedent(text)


dedented_text = textwrap.dedent(text).strip()
for width in [45,70]:
	print '%d columns:\n' % width
	print textwrap.fill(dedented_text, width=width)
	print


d = dedented_text
print textwrap.fill(d,
					initial_indent='',
					subsequent_indent=' ' * 4,
					width = 50,
					)
