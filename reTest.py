import re
str = "Edureka"
m = re.match('(..)+',str)
print m.group(1)
print m.group(0)
