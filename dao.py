from utilities import Utilities
class DAO:
    def __init__(self,table):
        self.keylist = {'primaryKey':None,'foreignKey':[]}
        self.table = table

    def insert(self,con):
        cursor = con.cursor()
        query = self.insertQuery()
        print(query)
        cursor.execute(query)
        
    def insertQuery(self):
        Utilities.fieldToinsert(self)
        query = "insert into %s values(" % self.table
        i = 0


        self.attrlist.pop(0)
        print((self.attrlist))
        isThereprimaryKey = False
        for field in self.attrlist:
            if(self.keylist['primaryKey']!=None and isThereprimaryKey==False):
                    query+="default"
                    isThereprimaryKey =True
            elif(str(type(self.__getattribute__(field)))=="<class 'str'>"):
                query+="'"+self.__getattribute__(field)+"'"
            else:
                query+=str(self.__getattribute__(field))
            if(i<len(self.attrlist)-1):
                query+=","
            i+=1
        query+=")"
        return query

        
    def update(self,con):
        cursor = con.cursor()
        query = self.updateQuery()
        print(query)
        cursor.execute(query)
        pass

    def updateQuery(self):
        try:
            Utilities.fieldToinsert(self)
            query = "update  %s set " % self.table
            i = 0
            self.attrlist.pop(0)
            primaryKey = Utilities.getPrimaryKey(self)
            primaryKey = Utilities.getPrimaryKey(self)
            for update in self.attrlist:
                query+=Utilities.query(self,update)
                if(i<len(self.attrlist)-1):
                    query+=' , '
                i+=1
            query+=" where "+Utilities.query(self,primaryKey)
            return query
        except Exception as e:
            print('error occured')
            print(e.with_traceback)

    def delete(self,con):
        cursor = con.cursor()
        query = self.deleteQuery()
        print(query)
        cursor.execute(query)
        pass

    def deleteQuery(self):
        primaryKey = Utilities.getPrimaryKey(self)
        query = "delete from %s where %s" % (self.table,Utilities.query(self,primaryKey))
        return query

    def select (self,con):
        cursor = con.cursor()
        query = self.selectQuery()
        cursor.execute(query)
        data = cursor.fetchall()
        array = []
        popo = 0.0
        for d in data:
            instance = type(self)
            temp = instance()
            i=1
            dt = Utilities.remove_brackets(d[0])
            for element in dt:
            #    print(element)
                temp.__setattr__(self.attrlist[i],element)
                i+=1
            array.append(temp)
        return array
    
    
    def selectQuery(self):
        fieldToGet = Utilities.objectNotNullfields(self)
        Utilities.fieldToinsert(self)
        query = "select ("
        for i in range(1,len(self.attrlist)):
            query+=self.attrlist[i]
            if (i < len(self.attrlist) - 1):
                query += ','
        query+=") from %s" % self.table
        if(len(fieldToGet)>0):
            query+=" where "
            for i in range (0,len(fieldToGet)):
                if(str(type(self.__getattribute__(fieldToGet[i])))=="<class 'str'>"):
                    query+=fieldToGet[i]+"='"+self.__getattribute__(fieldToGet[i])+"'"
                else:
                    query+=fieldToGet[i]+"="+str(self.__getattribute__(fieldToGet[i]))
                if(i<len(fieldToGet)-1):
                    query+=' and '
            pass
        return query

    def colnbr(self):
        pass
    
    def attrlists(self):
        return Utilities.getAllAttrName(self)