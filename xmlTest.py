import re
str = "<customer>1</customer>"
data = re.search('<([a-z])+>(.*)</\1>',str)
print data.group(1) + ": " + data.group(2)
