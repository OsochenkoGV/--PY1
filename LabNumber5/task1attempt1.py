# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
list_numbers = [{'bin': str(bin(x)), 'dec': x, 'hex': str(hex(x)), 'oct': str(oct(x))} for x in range(0, 16)]
pprint(list_numbers)
