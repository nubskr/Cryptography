from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import requests
import base64

results = []    

def get_score(s):
    # count the number of consecutive 16 byte chunks which come exactly once among all 16 byte chunks

    chunks = [s[i:i+16] for i in range(0, len(s), 16)]
    
    # Get the unique chunks by converting the list into a set
    unique_chunks = set(chunks)
    
    # Return the number of unique chunks
    if len(unique_chunks)!=0:
        return len(chunks)/len(unique_chunks)
    else:
        return 1e18

def get_unique_chunks(s):
    chunks = [s[i:i+16] for i in range(0, len(s), 16)]
    
    # Get the unique chunks by converting the list into a set
    unique_chunks = set(chunks)

    return (len(unique_chunks),len(chunks))

def process(s):
    results.append((get_score(s),s))

if (__name__ == "__main__"):
    url = "https://cryptopals.com/static/challenge-data/8.txt"
    response = requests.get(url)
    # key = b"YELLOW SUBMARINE"
    if response.status_code == 200:
        # decode the base64 shit
        file_content = response.text.split('\n')

        for i in file_content:
            s = bytes.fromhex(i)
            if(len(s)%16==0):
                process(s)


        results.sort(reverse = True)

        for result in results[0:10]:
            # print(get_unique_chunks(result[1]))
            print(result)
    

