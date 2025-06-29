from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import requests
import base64

if (__name__ == "__main__"):
    url = "https://cryptopals.com/static/challenge-data/7.txt"
    response = requests.get(url)
    key = b"YELLOW SUBMARINE"
if response.status_code == 200:
        # decode the base64 shit
        file_content = base64.b64decode(response.text)

        print(file_content)
        # now you have binary raw aes encrypted data shit,decrypt it with the aes key that you have
        cipher = AES.new(key,AES.MODE_ECB)

        shit = unpad(cipher.decrypt(file_content),16)
        
        print(shit)

