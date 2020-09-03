from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
This is the LifeStore-SalesList data:

lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore-products = [id_product, name, price, category, stock]
"""

# Definicion de usuarios y contraseñas, los elementos de las listas users y passw 
# estan relacionados 1 a 1, es decir la contraseña para el usuario que esta en la 
# posicion dos de la lista users sera unicamente la posision dos de la lista passw
users = ("admin", "usuario1")
passw = ("asd", "123")

def login():
    """
    [Implementación simple de inicio de sesión devuelve simepre un string que 
    contine el nombe del usuario loguedo correctamente; en otro caso el string 
    estará vacio. Imprime en pantalla informacián relacionada con el proceso 
    de loggin.]
    Returns:
        [str]: [nombre del usuarion logueado]
    """
    user = input("Usuario: ")
    pas = input("Contraseña: ")
    try:
        user_index = users.index(user)
        if pas == passw[user_index]:
            print(f"Sesión iniciada como: {user}.")
            return user
        else:
            print("Contraseña incorrecta.")
            return ""
    except ValueError:
        print("El usuario no esta registrado.")
        return ""


while True:
    pass