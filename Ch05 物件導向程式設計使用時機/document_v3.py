# 重新製作 Cursor
# 連接鍵盤的字母、方向鍵、Home、End
# 讓文字具有粗體、斜體、底線的功能，重新建構一個文字的物件
# 修改 document 的 insert，讓其 characters 屬性加入 Character 物件
# 修改 cursor，因為 document.characters 裡全部改存 Character 物件而非文字

class Character:
    def __init__(self, character, bold=False, italic=False, underline=False) -> None:
        assert len(str(character)) == 1
        self.character = str(character)
        self.bold = bold
        self.italic = italic
        self.underline = underline
    
    def __str__(self) -> str:
        '''__str__是python類別預設方法之一，可以以文字的方式傳回物件裡的屬性內容'''
        bold = "*" if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold + italic + underline + self.character


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
        # self.document.characters 裡目前存的都是 character 物件， 因此最後面要加上.character 回傳文字來判斷是不是 '\n'
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                break
    
    def end(self):
        # 同上
        while self.position < len(self.document.characters) and self.document.characters[self.position].character != '\n':
            self.position += 1



class Document:
    def __init__(self) -> None:
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        '''插入字元'''
        # 檢查 character 物件是否有一個叫做 'character' 的屬性
        if not hasattr(character,'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()
    
    def delete(self):
        '''刪除當前遊標所在字元'''
        del self.characters[self.cursor.position]

    def save(self):
        '''存檔'''
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))
    
    # 目前 self.characters 裡放的都是 Character 物件，利用 str() 就可直接回傳 Character 裡的文字屬性
    @property
    def show_string(self):
        return ''.join(str(c) for c in self.characters)
