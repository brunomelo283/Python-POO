from classes.Conexao import *

class Marcas():
    def __init__(self):
        self.__id = 0
        self.__marca = ''
        self.__conn = Conexao()

    def set_id(self, id):
        if id > 0:
            self.__id = id
    def get_id(self):
        return self.__id
    def set_marca(self,marca):
        if len(marca) > 0:
            self.__marca = marca
    def get_marca(self):
        return self.__marca
    
    def CreateMarca(self):
        sql = "insert into Marcas(marca) values(':marca')"
        sql = sql.replace(':marca', self.__marca)
        return self.__conn.execSql(sql)
    def UpdateMarca(self):
        sql = "update Marcas set marca = ':marca' where id = :id "
        sql = sql.replace(':marca', self.__marca)
        sql = sql.replace(':id', str(self.__id))
        return self.__conn.execSql(sql)
    def DeleteMarca(self):
        sql = "delete from Marcas where id = :id "
        sql = sql.replace(':id', str(self.__id))
        return self.__conn.execSql(sql)
    def ReadMarca(self,id = 0):
        if id != 0:
            self.__id = id
        sql = "select * from Marcas where id = :id"
        sql = sql.replace(':id', str(self.__id))
        return self.__conn.execSelect(sql)

    def ReadMarcas(self, id = 0):
        sql = "select * from Marcas"
        return self.__conn.execSelect(sql)

    
