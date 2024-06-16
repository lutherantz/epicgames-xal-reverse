from json     import dumps
from base64   import b64encode
from datetime import datetime

def _0x420d7c(a):
    xxx = "FZMÛSê/·V«xÞhí¢³4<`ô2ª,µ¦Yû"
    
    xxx = [ord(char) for char in xxx]

    b = ""
    c = dumps(a).encode("utf-8")
    d = list(range(256))
    e = 0
    f = ""

    for h in range(256):
        e = (e + d[h] + xxx[h % len(xxx)]) % 256
        b = d[h]
        d[h] = d[e]
        d[e] = b

    i = 0
    e = 0

    for j in range(len(c)):
        i = (i + 1) % 256
        e = (e + d[i]) % 256
        b = d[i]
        d[i] = d[e]
        d[e] = b
        f += chr(c[j] ^ d[(d[i] + d[e]) % 256])

    return b64encode(f.encode()).decode()

print(_0x420d7c(
    {
        "JSON": "REPLACE BRACKETS WITH XAL JSON"
    }
))