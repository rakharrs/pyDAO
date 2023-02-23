import dao as dao
class Utilities:
#return an array of the name of a dict
    def __init__(self) -> None:
        pass
    @staticmethod
    def getAllAttrName(list:object):
        var = vars(list)
        fields = []
        for data in var:
            fields.append(data)
        return fields

#maka ny attribut anle objet mi interagir am bdd
    @staticmethod
    def fieldToinsert(object):
        if(isinstance(object,dao.DAO)==False):
            raise Exception('A none DAO object can not use this function')
        object.attrlist.pop(0)

        
#return the none null field of an object
    @staticmethod
    def objectNotNullfields(object):
        if(isinstance(object,dao.DAO)==False):
            raise Exception('A none DAO object can not use this function')
        fieldtoInsert = object.attrlists()
        array = []
        for field in fieldtoInsert:
            if(field!="table" and field!="keylist" and field!="attrlist"):
                if(object.__getattribute__(field)!=None):
                    array.append(field)
        return array

    @staticmethod
    def getPrimaryKey(object):
        if(isinstance(object,dao.DAO)==False):
            raise Exception('A none DAO object can not use this function')
        keylist = object.keylist
        if(keylist['primaryKey']==None):
            raise Exception('No primary key found')
        
        return keylist['primaryKey']
    
    @staticmethod
    def getForeignKey(object):
        if(isinstance(object,dao.DAO)==False):
            raise Exception('A none DAO object can not use this function')
        keylist = object.keylist
        if(len(keylist['foreignKey'])==0):
            raise Exception('No foreign key found ')
        
        return keylist['foreignKey']


    @staticmethod
    def query(object, field):
        if (isinstance(object, dao.DAO) == False):
            raise Exception('A none DAO object can not use this function')

        if (str(type(object.__getattribute__(field))) == "<class 'str'>"):
            return field + "='" + object.__getattribute__(field) + "'"
        else:
            return field + "=" + str(object.__getattribute__(field))

    @staticmethod
    def insertPk(object):
        if (isinstance(object, dao.DAO) == False):
            raise Exception('A none DAO object can not use this function')
        pk = Utilities.getPrimaryKey(object)
        if(object.__getattribute__(pk)==None):
            return "default"
        else:
            return object.__getattribute__(pk)

    @staticmethod
    def remove_brackets(tup):
        str_tup = str(tup).replace('(', '').replace(')', '')
        return str_tup.split(',')
