# converts a given text to an array of numbers from 0-25
def toNumArray(text):
    return [ord(character)-97 for character in text.lower()]

# adds number value of the key to every character in text and returns as a string
def encrypt(text, key):
    numArr = toNumArray(text)
    encryptedArr = [(num + key)%26 for num in numArr]
    return ''.join(chr(num+65) for num in encryptedArr)

# removes number value of the key from every character in text and returns as a string
def decrypt(text, key):
    numArr = toNumArray(text)
    encryptedArr = [(num - key)%26 for num in numArr]
    return ''.join(chr(num+97) for num in encryptedArr)

