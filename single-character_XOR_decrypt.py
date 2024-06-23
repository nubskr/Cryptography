import string
import requests

# we need to score each result of process in some sorted container

# [(score,shit).....]
results = []

def get_score(s):
    # we need to find a way to score each output for its non random characterstics

    # lets just sort it with the frequency of vowels
    vowels = [b'a',b'e',b'i',b'o',b'u']

    score = 0
    denom = 1
    for char in s:
        lol = bytes([char])
        if lol in vowels:
            score = score + 1
        else:
            denom = denom + 1

    return score/denom 

def process(s,key):
    # does shits
    shit = bytearray(len(s)) 
    for i in range(len(s)):
        shit[i] = (s[i]^key)

    # print(shit)
    results.append((get_score(shit),shit))

def brute(s):
    b = bytes.fromhex(s)
    hehe = bytearray(string.printable,"ascii")
    for i in range(len(hehe)):
        process(b,hehe[i])
        # break

url = "https://cryptopals.com/static/challenge-data/4.txt"
response = requests.get(url)

if response.status_code == 200:
    file_content = response.text
    for i in file_content.splitlines():
        s = str(i)
        brute(s)

results.sort(reverse=True)


for result in results[:10]:
    print(result)
    # break