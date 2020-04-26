key = {'A':'R','B':'S','C':'T','D':'U','E':'V','F':'W','G':'X','H':'Y','I':'Z','J':'A','K':'B','L':'C','M':'D','N':'E','O':'F','P':'G','Q':'H','R':'I','S':'J','T':'K','U':'L','V':'M','W':'N','X':'O','Y':'P','Z':'Q',}


def cleanText(userInput):
    userInput = userInput.upper()
    cleanText = ''
    for c in userInput:
        if c.isalpha():
            cleanText += c
    return cleanText


def encipher(cleanText):
    cipherText = ''
    for c in cleanText:
        cipherText += key[c]

    return cipherText


pText = input("What do want to encipher? ")
pText = cleanText(pText)
print("Your input is : {} ".format(pText))
print("Your ciphertext: {}".format(encipher(pText)))

