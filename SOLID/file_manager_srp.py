# A class should have only one reason to change
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)
    
    def read(self, encoding = "UTF-8"):
        return self.path.read_text(encoding)
    
    def write(self, data, encoding = "UTF-8"):
        self.path.write_text(data, encoding)
        
class ZipFilemanager:
    def __init__(self, pathname):
        self.path = pathname
        
    # compress the file into a .zip archive by opening the file in write mode
    def compress(self):
        with ZipFile(self.path.with_suffix('.zip'), mode = "w") as archive:
            archive.write(self.path)
            
    # extracts the contents of the .zip file
    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode = 'r') as archive:
            # extracts all files present in zip archive into the current directory
            archive.extractall()