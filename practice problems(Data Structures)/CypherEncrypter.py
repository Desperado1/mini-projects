"""Shift characters by the given key"""


def caesarCipherEncryptor(string, key):
    # Write your code here.
	if key > 26:
		key = key%26
	string1 = ""
	for i in range(len(string)):
		value = ord(string[i]) + key
		if value <= 122:
			string1 += chr(value)
		else:
			string1 += chr(value - 122 + 96)
	return string1
