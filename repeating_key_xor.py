def encode_string(s,key):
    shit = bytearray(len(s)) 
    for i in range(len(s)):
        shit[i] = s[i]^key[i%len(key)]
    return shit

if (__name__ == "__main__"): 
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'
    s = encode_string(s.encode('utf-8'),key)
    s = s.hex()
    expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    print(s==expected)