from dao import DAO
class Road(DAO):
    def __init__(self,id:int=None,roadno:str=None,start_km:int=None,end_km:int=None):
        super().__init__("madagascar_roads_version4")
        self.id = id
        self.roadno = roadno
        self.start_km = start_km
        self.end_km = end_km
        self.attrlist = super().attrlists()
        self.keylist['primaryKey'] = 'id'

