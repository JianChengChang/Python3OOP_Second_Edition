import sys
import os
import shutil
import zipfile
from pathlib import Path

class ZipReplace:
    def __init__(self, filename, search_string, replace_string) -> None:
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path(f"unzipped-{filename}")
    
    def zip_find_replace(self):
        '''管理員方法，依序執行下面方法'''
        self.unzip_files()
        self.find_replace()
        self.zip_files()
    
    def unzip_files(self):
        '''
        建立一個暫存資料夾
        將檔案解壓縮到裡面
        '''
        if not os.path.exists(self.temp_directory):
            self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))
    

    def find_replace(self):
        '''
        到暫存資料夾中開啟每一個檔
        讀取文中的內文
        並把每一個 search_string 換成 replace_string
        寫回文件
        '''
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open('w') as file:
                file.write(contents)
        
    def zip_files(self):
        '''
        將暫存資料夾內的檔案寫進壓縮檔
        並刪除暫存資料夾
        '''
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        #shutil.rmtree(str(self.temp_directory))

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace()