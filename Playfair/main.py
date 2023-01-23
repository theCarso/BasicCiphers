import string

filler = 'X'

def loadMatrix(key):
    # setup matrix and character list
    key = key.upper()
    matrix = [[0 for x in range(5)] for y in range(5)] 
    letters = list(string.ascii_uppercase)
    letters.remove('J')
    i = 0
    j = 0
    # loop through characters in the key
    for character in key:
        if character in letters:
            matrix[i][j] = character
            i+=1
            if i >= 5:
                i=0
                j+=1
            letters.remove(character)
    # loop through remaining characters alphabetically
    for character in letters:
        matrix[i][j] = character
        i+=1
        if i >= 5:
            i=0
            j+=1
    return matrix

# returns index as (x,y)
def findInMatrix(matrix, character):
    for i, x in enumerate(matrix):
        if character in x:
            return (i, x.index(character))

# returns a 2 character encrypted string
def encryptPair(matrix, pair):
    pair=pair.upper().replace("J", "I")

    firstCharIndex = findInMatrix(matrix, pair[0])
    secondCharIndex = findInMatrix(matrix, pair[1])

    # Same row check
    if firstCharIndex[1] == secondCharIndex[1]:
        firstEnc = matrix[(firstCharIndex[0]+1)%5][firstCharIndex[1]]
        secondEnc = matrix[(secondCharIndex[0]+1)%5][secondCharIndex[1]]
        return firstEnc + secondEnc

    # Same column check
    if firstCharIndex[0] == secondCharIndex[0]:
        firstEnc = matrix[(firstCharIndex[0])][(firstCharIndex[1]+1 % 5)]
        secondEnc = matrix[(secondCharIndex[0])][(secondCharIndex[1]+1) % 5]
        return firstEnc + secondEnc
    
    # Different row and column
    firstEnc = matrix[secondCharIndex[0]][firstCharIndex[1]]
    secondEnc = matrix[firstCharIndex[0]][secondCharIndex[1]]
    return firstEnc + secondEnc
    
def encryptString(matrix, str):
    str=str.upper()
    i = 0
    result = ''
    while i < len(str):
        if i+1 >= len(str):
            result = result + encryptPair(matrix, str[i] + filler)
            i+=1
        elif str[i] == str[i+1]:
            result = result + encryptPair(matrix, str[i] + filler)
            i+=1
        else:
            result = result + encryptPair(matrix, str[i] + str[i+1])
            i+=2
    return result

def decryptPair(matrix, pair):
    firstCharIndex = findInMatrix(matrix, pair[0])
    secondCharIndex = findInMatrix(matrix, pair[1])

    # Same row check
    if firstCharIndex[1] == secondCharIndex[1]:
        firstEnc = matrix[(firstCharIndex[0]-1)%5][firstCharIndex[1]]
        secondEnc = matrix[(secondCharIndex[0]-1)%5][secondCharIndex[1]]
        return firstEnc + secondEnc

    # Same column check
    if firstCharIndex[0] == secondCharIndex[0]:
        firstEnc = matrix[(firstCharIndex[0])][(firstCharIndex[1]-1 % 5)]
        secondEnc = matrix[(secondCharIndex[0])][(secondCharIndex[1]-1) % 5]
        return firstEnc + secondEnc
    
    # Different row and column
    firstEnc = matrix[secondCharIndex[0]][firstCharIndex[1]]
    secondEnc = matrix[firstCharIndex[0]][secondCharIndex[1]]
    return firstEnc + secondEnc

def decryptString(matrix, str):
    i = 0
    result = ''
    while i < len(str):
        result = result + encryptPair(matrix, str[i] + str[i+1])
        i+=2
    return result.lower()


while True:
    prompt = input('Encrypt or decrypt (e/d)? ')
    # decrypt the text
    if(prompt.lower() == 'd'):
        key = input('Input your key: ').upper()
        matrix = loadMatrix(key)
        ciphertext = input('Input your ciphertext: ')
        print(ciphertext.upper() + " {" + key + "} -> " + decryptString(matrix, ciphertext))
    # encrypt the text
    elif (prompt.lower() == 'e'):
        key = input('Input your key: ').upper()
        matrix = loadMatrix(key)
        plaintext = input('Input your plaintext: ')
        print(plaintext.lower() + " {" + key + "} -> " + encryptString(matrix, plaintext))
    # invalid input
    else:
        print('Invalid input.')