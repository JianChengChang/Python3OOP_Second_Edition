# 重新製作 Cursor
# 連接鍵盤的字母、方向鍵、Home、End

class Cursor:
    def __init__(self, document) -> None:
        self.document = document
        self.position = 0
    
    def forward(self):
        if self.position == len(self.document.characters):
            return
        self.position += 1
    
    def back(self):
        if self.position == 0:
            return
        self.position -= 1
    
    def home(self):
        while self.document.characters[self.position-1] != '\n':
            self.position -= 1
            if self.position == 0:
                break
    
    def end(self):
        while self.position < len(self.document.characters) and self.document.characters[self.position] != '\n':
            self.position += 1



class Document:
    def __init__(self) -> None:
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        '''插入字元'''
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()
    
    def delete(self):
        '''刪除當前遊標所在字元'''
        del self.characters[self.cursor.position]

    def save(self):
        '''存檔'''
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))
    
    @property
    def show_string(self):
        return ''.join(self.characters)
