import sys
from PIL import Image
from zip_processor import ZipProcessor

class ScaleZip(ZipProcessor):
    def process_files(self):
        '''將目錄下的圖檔全部改為 640 X 480'''
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(str(filename))

if __name__ == '__main__':
    ScaleZip(*sys.argv[1:4]).process_zip()