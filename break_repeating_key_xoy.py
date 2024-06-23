import string
import requests

def bytes_to_bits(byte_string):
    return ''.join(format(byte, '08b') for byte in byte_string)

def get_dis(s1,s2):
    s1 = bytes_to_bits(s1)
    s2 = bytes_to_bits(s2)
    
    # returns the hamming distance between two strings
    ret = 0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            ret = ret + 1
    return ret 

def find_one(s):
    # try everything and find a single key that works the best, maybe just use no. of vowels as a reward function or smth
    
    # what exactly did they mean by "take the histogram which looks best duh, no idea"
    
    return 1

def process(s,key_size):
    # deal with each s[i]%key_size separately


    return 1

if (__name__ == "__main__"):
    url = "https://cryptopals.com/static/challenge-data/6.txt"
    response = requests.get(url)
    if response.status_code == 200:
        file_content = response.text
        raw_bytes = file_content.encode('utf-8')

        scores = []

        # guess the KEYSIZE
        for i in range(2,40):
            s1 = raw_bytes[0:i] # the first i bytes in this 0,i
            s2 = raw_bytes[i+1:2*i + 1] # the second i bytes in this, i+1,2*i

            dis = get_dis(s1,s2)/i
            scores.append((dis/i,i))

        scores.sort()

        # Guess the key, check for 5 smallest vals
        for dis,ksize in scores[:5]:
            print(dis)