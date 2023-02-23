from dao import *
class Route(DAO):
    def __init__(self,id:int=None,nom:str=None,longueur:float=None):
        super().__init__("rout")
        self.id = id
        self.nom = nom
        self.longueur = longueur
        self.attrlist = super().attrlists()
        self.keylist['primaryKey'] = 'id'
