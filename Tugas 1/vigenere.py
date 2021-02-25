import string
from random import shuffle

char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# BUAT KUNCI VIGENERE
def make_key(data,key,mora):
    result = []
    key_count = 0
    for i in range(0,len(data)):
        if data[i] == " ":
            result.append(" ")
        elif mora == 'm':
            j = key_count % len(key)
            result.append(key[j])
            key_count += 1
        elif mora == 'a':
            if i <= len(key):
                j = key_count % len(key)
                result.append(key[j])
            else:
                j = key_count % len(data)
                result.append(data[j])
            key_count += 1
    result = ''.join(str(i) for i in result)
    return result

# VIGENERE STANDAR
def vig(data,key,enorde):
    key_val = make_key(data,key,'m')
    result = ""
    for i in range(0,len(data)):
        if data[i] == " ":
            result += ""
        elif enorde == 'en':
            val = (char.find(data[i]) + char.find(key_val[i])) % 26
            result += char[val]
        elif enorde == 'de':
            val = (char.find(data[i]) - char.find(key_val[i])) % 26
            result += char[val]
    return result

# FULL VIGENERE
def vig_full(data,key,enorde):
    sfchar = list(char)
    shuffle(sfchar)
    charx = ''.join(sfchar)
    key_val = make_key(data,key,'m')
    result = ""
    for i in range(0,len(data)):
        if data[i] == " ":
            result += ""
        elif enorde == 'en':
            val = (char.find(data[i]) + charx.find(key_val[i])) % 26
            result += charx[val]
        elif enorde == 'de':
            val = (char.find(data[i]) - charx.find(key_val[i])) % 26
            result += charx[val]
    return result

# AUTOKEY VIGENERE
def vig_auto(data,key,enorde):
    key_val = make_key(data,key,'a')
    result = ""
    for i in range(0,len(data)):
        if data[i] == " ":
            result += ""
        elif enorde == 'en':
            val = (char.find(data[i]) + char.find(key_val[i])) % 26
            result += char[val]
        elif enorde == 'de':
            val = (char.find(data[i]) - char.find(key_val[i])) % 26
            result += char[val]
    return result

def vig_ascii(data,key,enorde):
    keyint = [ord(i) for i in key]
    dataint = [ord(i) for i in data]
    result = ""
    for i in range(len(data)):
        if enorde == 'en':
            val = (dataint[i] + keyint[i % len(key)] - 32) % 95
        elif enorde == 'de':
            val = (dataint[i] - keyint[i % len(key)] - 32) % 95
        result += chr(val + 32)
    return result