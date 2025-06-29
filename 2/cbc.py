# Ci = (Ci-1 ^ plain_text) 
# Ei = encrypt(Ci)

def encrypt_block(key='hieee',block_data):
    # data and key must be 16 bytes
    # reg ecb block encryption


def encrypt_string(IV,string_data):
    # len of string_data must be div by 16(block size)
