class HashTable:
    def __init__(self):
        self.MAX = 100
        self.array = [[] for i in range(self.MAX)]

    def getHash(self, key):
        h = 0
        for letter in key:
            h += ord(letter)
        return h % self.MAX
    
    def addKeyValue(self, key, value):
        h = self.getHash(key)
        
        found = False
        for idx, element in enumerate(self.array[h]):
            if element == 2 and element[0] == key:
                self.array[h][idx] = ((key, value))
                found = True
                break   
            if not found:
                self.array[h].append((key, value))
    
    def getValue(self, key):
        h = self.getHash(key)
        print(self.array[h])
    
    
    
        

new_hash = HashTable()
new_hash.addKeyValue("Property 1", "7% ROI")
new_hash.addKeyValue("Property 2", "9% ROI")
new_hash.array