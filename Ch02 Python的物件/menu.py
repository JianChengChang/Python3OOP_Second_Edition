# 練習建構一個筆記本應用程式
# Create date : 2021/09/15
# Create by Jian Cheng Chang

import sys
from notebook import Notebook, Note

class Menu:
    '''顯示選單並回應選擇'''

    def __init__(self) -> None:
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }
    
    def display_menu(self):
        print('''
            Notebook Menu

            1. Show all Notes
            2. Search Notes
            3. Add Note
            4. Modify Note
            5. Quit
        ''')
    
    def run(self):
        '''顯示清單並給予回應'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} is not a valid choice.')
        
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f'{note.id}: {note.tags}\n{note.memo}')
    
    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    
    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your memo has been added.")

    def modify_note(self):
        id = input('Enter a node id: ')
        memo = input('Enter a memo: ')
        tags = input('Enter tags: ')
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print('Thank you for using your notebook today')
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
