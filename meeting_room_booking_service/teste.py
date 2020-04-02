from mongoengine import *

connect(
    db="demo-db",
    username="root",
    password="example",
    authentication_source="admin",
    host="localhost",
    port=27017
)

class Address(EmbeddedDocument):
    address = StringField()

class User(Document):
    
    def __init__(self,*args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.addr = Address()
        
    username = StringField()
    email = EmailField()
    password = BinaryField()
    addr = EmbeddedDocumentField(Address)

