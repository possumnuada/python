from Crypto.Cipher import AES
import binascii
import re

iv = binascii.unhexlify('aabbccddeeff00998877665544332211')
ct = binascii.unhexlify('764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2')

f = open('words.txt', 'r')

# read each line in word list
for line in f:

    line = line.strip()
    linelen = len(line)

    # if word is too long, ignore
    if(linelen > 16): continue

    # if line needs to be padded, pad line
    if(linelen < 16):
        for i in range(16-linelen):
            line += '#'

    # make word into key
    key = bytes(line, 'utf-8')
    aes = AES.new(key, AES.MODE_CBC, IV=iv)

    # decrypt ciphertext
    plaintext = aes.decrypt(ct).decode('utf-8', 'ignore')

    # if plaintext matched expected plaintext
    if(re.search('This is a top secret.', plaintext)):

        # print key and stop searching
        print("The key is: " + line)
        break

f.close()
