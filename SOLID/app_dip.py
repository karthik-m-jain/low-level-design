from abc import ABC, abstractmethod

class FrontEnd():
    def __init__(self, data_source):
        self.data_source = data_source
        
    def display_data(self):
        print(f"Data is from {self.data_source.get_data()}")
        
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass
    
class Database(DataSource):
    def get_data(self):
        return "Database"
    
class API(DataSource):
    def get_data(self):
        return "API Call"
    
obj = FrontEnd(Database())
obj.display_data()

obj = FrontEnd(API())
obj.display_data()