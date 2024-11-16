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
with open('python\\temp\\destructs.txt', 'r') as f:
    with open('python\\temp\\encoded_destructs.txt', 'w') as f2:
        for line in f:
            treeID, variation, x, y, z, angle, scale = line.split()
            #if len(variation) == 1:
            #    variation = "0" + variation
            #A, B, C, D = tileset
            #tileset = ord(A) * 256**3 + ord(B) * 256**2 + ord(C) * 256 + ord(D)
            x = str(int(x) + 20000)
            y = str(int(y) + 20000)
            z = str(int(z) + 20000)
            angle = str(int(float(angle) * 100))
            scale = str(int(float(scale) * 100))
            if len(angle) == 1:
                angle = "00" + angle
            if len(angle) == 2:
                angle = "0" + angle
            if len(scale) == 1:
                scale = "00" + scale
            if len(scale) == 2:
                scale = "0" + scale

            #tileset = num_encode(tileset)
            f2.write(treeID
                    + variation
                    + x
                    + y
                    + z
                    + angle
                    + scale)
            #f2.write(tileset + " " + variance + "\n")