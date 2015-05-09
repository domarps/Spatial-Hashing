import sys

coord = (1.23, 4.56)
#The X an Y co-ordinates,(1.23,4.56) must yield strings “1_4”, “12_45”, “123_456”

def get_coord(coord):
   coord_str = map(lambda x: str(x).replace('.', ''), coord)
   for level in range(1, len(coord_str[0])+1):
      yield reduce(lambda x, y: (x[:level]+'_'+y[:level]), coord_str)

print list(get_coord(coord))
