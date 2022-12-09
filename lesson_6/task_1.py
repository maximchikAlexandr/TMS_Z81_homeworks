INPUT_STR = b"r\xc3\xa9sum\xc3\xa9".decode()
LATIN_ENCODED_BYTES = INPUT_STR.encode("Latin1")
LATIN_DECODED_STR = LATIN_ENCODED_BYTES.decode("Latin1")

print(INPUT_STR, LATIN_ENCODED_BYTES, LATIN_DECODED_STR, sep="\n")

assert isinstance(INPUT_STR, str)
assert isinstance(LATIN_ENCODED_BYTES, bytes)
assert isinstance(LATIN_DECODED_STR, str)
