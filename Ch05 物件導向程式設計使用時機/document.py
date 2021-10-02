# 此案例研究中
# 更進一步探討我何時應該選擇物件還是內建型別

class Document:
    def __init__(self) -> None:
        self.characters = []
        self.cursor = 0
        self.filename = ''

    def insert(self, character):
        '''插入字元'''
        self.characters.insert(self.cursor, character)
        self.cursor += 1
    
    def delete(self):
        '''刪除當前遊標所在字元'''
        del self.characters[self.cursor]

    def save(self):
        '''存檔'''
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    def forward(self):
        '''遊標往後移'''
        self.cursor += 1
    
    def backward(self):
        '''游標往後移'''
        self.cursor -= 1
    
    