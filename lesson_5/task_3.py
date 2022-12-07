words = ("abba", "word", "type", "oppo")
polindroms = tuple(filter(lambda x: x == x[::-1], words))

assert polindroms == ("abba", "oppo")
