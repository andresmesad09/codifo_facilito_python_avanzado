"""
Tenemos un programa para registrar usuarios, y
queremos validar por medio de decoradores si
los usuarios creados existen en nuestra base de
datos y si su contraseña sigue las mejores
prácticas de la compañía:
● Debe contener al menos 8 caracteres.
● Puede contener letras mayúsculas y
minúsculas de la a a la z.
● Puede contener números del 0 al 9.
● Puede contener caracteres especiales
como: @#$%^&+=
"""

from decorators import authenticate_class, validate_password

@authenticate_class
class MyClass:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def say_hello(self):
        print(f"Hi {self.username}")
    
    @validate_password
    def show_password(self):
        print(f"Hi {self.username}, your pwd starts by {self.password[:4]}{len(self.password)*'*'}")

if __name__ == "__main__":
    my_class = MyClass("andresmesad", "Test1234*")
    my_class.say_hello()
    my_class.show_password()
    # invalid_class = MyClass("andresmesad09", "test123.")