# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

nums_and_types = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)]

pprint(nums_and_types)
