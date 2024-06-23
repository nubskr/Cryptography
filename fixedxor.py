def gogo(s1,s2):
    shit = bytearray([])
    assert(len(s1)==len(s2))
    for i in range(len(s1)):
        shit.append(s1[i]^s2[i])
    return shit.hex()

s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'
b1 = bytes.fromhex(s1)
b2 = bytes.fromhex(s2)
assert(gogo(b1,b2)=='746865206b696420646f6e277420706c6179')
