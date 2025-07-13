from mongoengine import Document, StringField, IntField, ListField

class Producto(Document):
    meta = {'collection': 'productos'}  
    nombre = StringField(required=True, max_length=100)
    descripcion = StringField()
    precio = IntField()
    caracteristicas = ListField(StringField())

    def __str__(self):
        return self.nombre
