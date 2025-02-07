# Factory Design pattern

class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette", "cycle":"cyclette"}
        
    def localize(self, msg):
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
        
    def localize(self, msg):
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    def localize(self, msg):
        return msg
    
def Factory(language = "English"):
    objectMap = {"French" : FrenchLocalizer(), "English" : EnglishLocalizer(), "Spanish" : SpanishLocalizer()}
    
    return objectMap[language]

if __name__ == '__main__':
    f = Factory("French")
    s = Factory("Spanish")
    e = Factory()
    
    message = ["car", "cycle"]
    
    for msg in message:
        print(f.localize(msg))
        print(s.localize(msg))
        print(e.localize(msg))