import string
ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz?!*<=>@"
ALPHABET_REVERSE = dict((c, i) for (i, c) in enumerate(ALPHABET))
BASE = len(ALPHABET)
SIGN_CHARACTER = '-'

def num_encode(n):
    if n < 0:
        return SIGN_CHARACTER + num_encode(-n)
    s = []
    while True:
        n, r = divmod(n, BASE)
        s.append(ALPHABET[r])
        if n == 0: break
    return ''.join(reversed(s))

def num_decode(s):
    if s[0] == SIGN_CHARACTER:
        return -num_decode(s[1:])
    n = 0
    for c in s:
        n = n * BASE + ALPHABET_REVERSE[c]
    return n

MAGICNUM = 142578010

encoded_string = ""
with open('python\\temp\\tiles.txt', 'r') as f:
    with open('python\\temp\\encoded_tiles.txt', 'w') as f2:
        for line in f:
            tileset, variation = line.split()
            if len(variation) == 1:
                variation = "0" + variation
            #A, B, C, D = tileset
            #tileset = ord(A) * 256**3 + ord(B) * 256**2 + ord(C) * 256 + ord(D)
            #tileset = num_encode(tileset)
            f2.write(tileset + variation)
            #f2.write(tileset + " " + variation + "\n")