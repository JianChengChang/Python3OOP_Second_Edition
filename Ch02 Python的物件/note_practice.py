# 練習建構一個筆記本應用程式
# Create date : 2021/09/15
# Create by Jian Cheng Chang

# 筆記是存在筆記本上的小記錄
# 每個筆記要能記錄撰寫時間
# 標籤
# 要能修改
# 搜尋筆記

# 此時需要有兩個物件 在 notebook.py
# 一個是筆記本 Notebook
# 一個是筆記 Note


# first test
from notebook import Note
n1 = Note('Hello first')
n2 = Note('Hello again')
print(n1.id)
print(n2.id)
print(n1.match('Hello'))
print(n2.match('second'))

# second test
from notebook import Note, Notebook

n = Notebook()
n.new_note('hello world')
n.new_note('hello again')
n.notes

# Print note's id
print(n.notes[0].id)
print(n.notes[1].id)

# Print note's content
print(n.notes[0].memo)

# Search
n.search('hello')
n.search('world')

# modify
n.modify_memo(1, 'hi world')
print(n.notes[0].memo)
