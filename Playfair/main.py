import string

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
        print(character)
        matrix[i][j] = character
        i+=1
        if i >= 5:
            i=0
            j+=1
    return matrix
