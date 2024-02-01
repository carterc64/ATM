class encryption():

    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.s_box = self.sboxSetup()
        self.key = 'northwestsoutheast'


    def sboxSetup(self):
        s_box = [['']*26 for i in range(26)]
     
        i = 0
        x = 0
        for x in range(26):
            i = x
            for z in range(26):
                s_box[x][z] = self.alphabet[i]
                if i == 25:
                    i = 0
                else:
                    i += 1
        return s_box
    
    def substitute(self, text):
        cipher = ''
        text = text.lower()
        text = list(text)
        key = list(self.key)
        kindex = 0
        cindex = 0
        for letter in text:
            if letter.isalpha():
                cipher += self.s_box[self.alphabet.index(key[kindex])][self.alphabet.index(letter)]

        return cipher
                
       



e = encryption()
text = 'apple'
print(e.substitute(text))