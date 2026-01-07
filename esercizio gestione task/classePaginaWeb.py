"""Parser di pagine web
Creare una classe che abbia le funzioni di parser di pagine web

2 Metodi getter specifici
A richiesta mi dia il numero di ricorrenze delle chiamate di stile, il numero di tag href, ed
il numero di immagini come singoli metodi getter

3 Incapsulamento
Non mi permetta di accedere all'html e non salvi nessun file"""

class PaginaWeb:
    def __init__(self, url):
        self.__url = url
        self.__html = ""
        self.__numStile = 0
        self.__numHref = 0
        self.__numImmagini = 0
        

    def getUrl(self):
        return self.__url
    
    def setUrl(self, newUrl):
        self.__url = newUrl
    
    def getNumStile(self):
        return self.__numStile
    
    def getNumHref(self):
        return self.__numHref
    
    def getNumImmagini(self):
        return self.__numImmagini
    
    def openSite(self):
        pass
    