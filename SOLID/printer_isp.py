from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass
    
class Scan(ABC):
    @abstractmethod
    def scan(self, document):
        pass
    
class OldPrinter(Printer):
    def print(self, document):
        print(f"{document} is printed")
        
class NewPrinter(Printer, Fax, Scan):
    def print(self, document):
        print(f"{document} is printed")
    
    def fax(self, document):
        print(f"{document} is faxed")
    
    def scan(self, document):
        print(f"{document} is scanned")
        
oldmac = OldPrinter()
oldmac.print("Resume")

newmac = NewPrinter()
newmac.scan("Resume")
newmac.fax("Resume")
newmac.print("Resume")