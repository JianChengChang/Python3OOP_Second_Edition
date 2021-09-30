from zip_processor import ZipProcessor
import sys
import os

class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string) -> None:
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string
    
    def process_files(self):
        '''對臨時目錄下的檔案執行搜尋文字與替換'''
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open('w') as file:
                file.write(contents)

if __name__ == '__main__':
    ZipReplace(*sys.argv[1:4]).process_zip()