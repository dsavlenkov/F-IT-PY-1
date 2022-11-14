from pprint import pprint
# TODO решить с помощью list comprehension и распечатать его
pprint([{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(16)])
