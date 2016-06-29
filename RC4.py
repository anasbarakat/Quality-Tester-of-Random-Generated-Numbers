# RC4 générateur de bits pseudo-aléatoires 

class WikipediaARC4:
    def __init__(self, key = None): # self pour l'instance en cours 
        self.state = list(range(256)) # initialisation de la table de permutation
        self.x = self.y = 0 # les index x et y, au lieu de i et j
 
        if key is not None:
            self.init(key)
 
    # Key schedule: génération de la permutation à partir de la clé key
    def init(self, key):
        for i in range(256):
            self.x = (ord(key[i % len(key)]) + self.state[i] + self.x) & 0xFF # ord() Unicode code point of the caracter
            self.state[i], self.state[self.x] = self.state[self.x], self.state[i]
        self.x = 0
 
    # Générateur (du flot pseudo-aléatoire à partir de l'entrée à coder)
    def crypt(self, input):
        output = [None]*len(input)
        for i in range(len(input)):
            self.x = (self.x + 1) & 0xFF
            self.y = (self.state[self.x] + self.y) & 0xFF
            self.state[self.x], self.state[self.y] = self.state[self.y], self.state[self.x]
            output[i] = chr((ord(input[i]) ^ self.state[(self.state[self.x] + self.state[self.y]) & 0xFF]))# chr is the character corresponding to a code 
        return ''.join(output)
# pour la conversion de l'hexadécimal au binaire 
conv = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}
 
def hex2bin(d, nb = 0):
    return ''.join([conv[ch] for ch in d]).zfill(nb) 
 
import base64
def encode(sh):
   #print(base64.b16encode(bytes(sh, 'latin')).upper())
   return base64.b16encode(bytes(sh, 'latin')).upper()

#if __name__ == '__main__':
#    test_vectors = [['Key', 'Plaintext'], \
#                   ['Wiki', 'pedia'], \
#                   ['Secret', 'Attack at dawn']]
    #test= ['Key', ]
#    for i in test_vectors:
#        encode(WikipediaARC4(i[0]).crypt(i[1]))
#        print(hex2bin(str(encode(WikipediaARC4(i[0]).crypt(i[1])).decode('ascii'))))
#        hex2bin(str(encode(WikipediaARC4(i[0]).crypt(i[1])).decode('ascii')))
        #print(hex2bin(str(encode(WikipediaARC4('Key').crypt('01110001101')).decode('ascii'))))
        
        


        