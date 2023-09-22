class Pile:
    
    def __init__(self):
        self.__pile = []
    
    def empiler(self, arg):
        self.__pile.append(arg)
    
    def depiler(self):
        elt = self.__pile[-1]
        del self.__pile[-1]
        return elt
    
    def sommet(self):
        return self.__pile[-1]
    
    def est_vide(self):
        return len(self.__pile) == 0
    
    def __str__(self):
        return str(self.__pile)


class File:
    
    def __init__(self):
        self.__file = []
    
    def ajouter(self, arg):
        self.__file.append(arg)
    
    def enlever(self):
        elt = self.__file[0]
        del self.__file[0]
        return elt
    
    def sommet(self):
        return self.__file[0]
    
    def est_vide(self):
        return len(self.__file) == 0
    
    def __str__(self):
        return str(self.__file)