# 練習建構一個筆記本應用程式
# Create date : 2021/09/15
# Create by Jian Cheng Chang

# 筆記是存在筆記本上的小記錄
# 每個筆記要能記錄撰寫時間
# 標籤
# 要能修改
# 搜尋筆記

# 此時需要有兩個物件
# 一個是筆記本 Notebook
# 一個是筆記 Note

import datetime

# 儲存新筆記編號
last_id = 0

class Note():
    '''代表筆記本中的一個筆記，可用字串搜尋並儲存標籤'''

    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.created_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, filter):
        '''
        判斷筆記是否與搜尋文字相符
        相符回傳 True
        否則 False
        搜尋要區分大小且且同時尋找文字和標籤
        '''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''待表一群可以被標記、修改與搜尋的筆記'''

    def __init__(self) -> None:
        '以空清單初始化筆記本'
        self.notes = []
    
    def new_note(self, memo, tags=''):
        '建構新的筆記並加入到清單中'
        self.notes.append(Note(memo, tags))

    # def modify_memo(self, note_id, memo):
    #     '找出特定編號的筆記，並修改其內容'
    #     for note in self.notes:
    #         if note.id == note_id:
    #             note.memo = memo
    #             break

    # def modify_tags(self, note_id, tags):
    #     '找出特定編號的筆記，並修改其標籤'
    #     for note in self.notes:
    #         if note.id == note_id:
    #             note.tags = tags
    #             break     

    def search(self, filter):
        '找出所有與指定條件字串相符的筆記'
        return [note for note in self.notes if note.match(filter)]   
    
    # modify_memo 和 modify_tags 功用差不多
    # 試著改善

    def _find_note(self, note_id):
        '找出特定id的筆記'
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        '找出特定編號的筆記，並修改其標籤'
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False 