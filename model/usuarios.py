import pymongo

class Usuarios:
    def __init__(self, id=1, username=2, password=3, email=4):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

        #self.telefono = telefono
        #self.direccion= direccion
        #self.puesto=puesto
        #self.ingreso=ingreso
        #self.jefatura=jefatura
    
    def guardar(self):
        #abrir la conxion mediante un objeto cliente
        usuarios=pymongo.MongoClient("mongodb+srv://admin:admin@trespatitosdb.mi0zzv0.mongodb.net/")
        bd=usuarios["TresPatitos"]
        try:
            #definir la tabla a utilizar
            tbl=bd["usuarios"]
            #crear diccionario
            doc={"_id":self.id,
                "username":self.username,
                "password":self.password,
                "email":self.email
                }
            #insertar en la tabla
            tbl.insert_one(doc)
            estado=1
        except Exception:
            print("Error al guardar")
            estado=0
        finally:
            usuarios.close
        return estado
    
    def actualizar(self):
        #abrir la conxion mediante un objeto cliente
        usuarios=pymongo.MongoClient("mongodb+srv://admin:admin@trespatitosdb.mi0zzv0.mongodb.net/")
        bd=usuarios["TresPatitos"]
        try:
            #definir la tabla a utilizar
            tbl=bd["usuarios"]
            #filtro sirve para ver que quiero modificar
            filtro={"_id":self.id}
            #crear diccionario
            doc={"$set":{"username":self.username,
                        "password":self.password,
                        "email":self.email,}
                        }
            #insertar en la tabla
            tbl.update_one(filtro,doc)
            estado=1
        except Exception:
            print("Error al guardar")
            estado=0
        finally:
            usuarios.close
        return estado
    
    def eliminar(self):
        usuarios=pymongo.MongoClient("mongodb+srv://admin:admin@trespatitosdb.mi0zzv0.mongodb.net/")
        bd=usuarios["TresPatitos"]
        try:
            #definir la tabla a utilizar
            tbl=bd["usuarios"]
            #filtro sirve para ver que quiero modificar
            filtro={"_id":self.id}
            tbl.delete_one(filtro)
            estado=1
        except Exception:
            print("Error al Eliminar")
            estado=0
        finally:
            usuarios.close
        return estado
    
    def getUsuarios(self):
        usuarios=pymongo.MongoClient("mongodb+srv://admin:admin@trespatitosdb.mi0zzv0.mongodb.net/")
        bd=usuarios["TresPatitos"]
        tbl=bd["usuarios"]
        return tbl.find()
    
    def getRegistrosUsuarios(self):
        usuarios=pymongo.MongoClient("mongodb+srv://admin:admin@trespatitosdb.mi0zzv0.mongodb.net/")
        bd=usuarios["TresPatitos"]
        size=bd.command("collstats","usuarios") #estadisticas
        return size["count"]