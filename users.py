# importar la función que devolverá una instancia de una conexión
from models.connection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios.users;"
        results = connectToMySQL('usuarios').query_db(query)
        users = []
        for usuario in results:
            users.append( cls(usuario) )
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios.users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('usuarios.users').query_db( query, data )

