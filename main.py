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
usrs = ("admin", "usuario1")
passw = ("asd", "123")
welcome_msg = """
    ######################## LifeStore ########################
            Sistema de análisis de ventas e inventario
    ###########################################################
    
    Menu principal:
    1  -> Iniciar sesión.
    2  -> Salir.

                                              by  ivand890 2020

    Opción:
"""
analysis_msg = """
    ######################## LifeStore ########################
            Sistema de análisis de ventas e inventario
    ###########################################################
    
    Menu análisis:
    ----> Productos más vendidos y productos rezagados:
    1  -> Productos con mayores ventas.
    2  -> Productos con mayores busquedas.
    3  -> Productos con menores ventas.
    4  -> Productos con menores busquedas.
    
    ----> Productos por reseña en el servicio: 
    5  -> Productos con las mejores reseñas.
    6  -> Productos con las peores reseñas.
    
    ----> Resumenes:
    7  -> Total de ingresos.
    8  -> Total anual.
    9  -> Ventas promedio mensuales.
    10 -> Meses con más ventas al año.

    11 -> Atras.


    Opción:
"""


def login(users, passwords):
    """[Implementación simple de inicio de sesión devuelve siempre un string que 
    contine el nombe del usuario loguedo correctamente; en otro caso el string 
    estará vacio. Imprime en pantalla informacián relacionada con el proceso 
    de loggin.]

    Args:
        users ([list]): [Lista con los nombres de usuario]
        passwords ([list]): [Lista con las contraseñas de usuario]

    Returns:
        [str]: [string con el nombre del usuario correctamnete logueado]
    """
    user = input("Usuario: ")
    pas = input("Contraseña: ")
    try:
        user_index = users.index(user)
        if pas == passwords[user_index]:
            print(f"Sesión iniciada como: {user}.")
            return user
        else:
            print("Contraseña incorrecta.")
            return ""
    except ValueError:
        print("El usuario no esta registrado.")
        return ""

#%%
def sort_by_index(products, sales, index, reverse=False):
    only_sales = [row[index] for row in sales]
    products_sold = list(set(only_sales))
    total_sales_products = [[product, only_sales.count(product)] for product in products_sold]
    total_sales_products.sort(key=lambda x: x[1], reverse=reverse)
    return [[row[1], row[0], products[row[0]-1][1].split(',')[0]] for row in total_sales_products] 

#%%
while True:
    """
    [Ciclo principal para controlar la ejecución del programa.]
    """
    choice1 = input(welcome_msg)
    if choice1 == '1':
        user_loged = login(usrs, passw)
        if user_loged:
            while True:
                choice2 = input(analysis_msg)
                if choice2 == "1":
                    sort_by_index(lifestore_products, lifestore_sales, 1, reverse=True)[:20]
                    input("pausa")
                    #TODO agregar formato
                elif choice2 == "2":
                    sort_by_index(lifestore_products, lifestore_searches, 1, reverse=True)[:20]
                elif choice2 == "3":
                    sort_by_index(lifestore_products, lifestore_sales, 1)
                elif choice2 == "4":
                    sort_by_index(lifestore_products, lifestore_searches, 1)
                elif choice2 == "5":
                    sort_by_index(lifestore_products, lifestore_products, 2, reverse=True)[:20]
                elif choice2 == "6":
                    sort_by_index(lifestore_products, lifestore_products, 2)[:20]
                elif choice2 == "7":
                    pass
                elif choice2 == "8":
                    pass
                elif choice2 == "9":
                    pass
                elif choice2 == "10":
                    pass
                elif choice2 == "11":
                    break
                else:
                    continue
        else:
            continue
    elif choice1 == '2':
        print('Bye Bye')
        break