class CezarCode:
    key = 0

    def __init__(self, key):
        self.key = key

    def setKey(self, key):
        self.key = key

    def encrypt(self, text):
        code = ""
        text = text.lower()
        for i in range(len(text)):
            if ord(text[i]) > 122 - self.key:
                code += chr(ord(text[i]) + self.key - 26)
            else:
                code += chr(ord(text[i]) + self.key)
        return code

    def decrypt(self, text):
        decoded = ""
        text = text.lower()
        key = self.key % 26
        for i in text:
            if ord(i) - key < 97:
                decoded += chr(ord(i) - key + 26)
            else:
                decoded += chr(ord(i) - key)
        return decoded


C = CezarCode(6)
code = C.encrypt("Mushrooms")
print(code)
print(C.decrypt(code))

