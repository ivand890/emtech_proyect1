def login(users, passwords):
    """[Implementación simple de inicio de sesión devuelve siempre un string que 
    contine el nombre del usuario logueado correctamente; en otro caso el string 
    estará vacío. Imprime en pantalla información relacionada con el proceso 
    de loggin.]

    Args:
        users ([list]): [Lista con los nombres de usuario]
        passwords ([list]): [Lista con las contraseñas de usuario]

    Returns:
        [str]: [string con el nombre del usuario correctamente logueado]
    """
    user = input("Usuario: ")
    pas = input("Contraseña: ")
    try:
        user_index = users.index(user)
        if pas == passwords[user_index]:
            print(f"\n#### Sesión iniciada como: {user}.")
            return user
        else:
            print("\n#### ERROR: Contraseña incorrecta.")
            return ""
    except ValueError:
        print("\n#### ERROR: El usuario no esta registrado.")
        return ""

def get_column(obj, index=0):
    """[Extrae una columna de la list dada.]

    Args:
        obj ([list]): [lista de listas para extraer]
        index (int, optional): [indice de la columna a extraer]. Defaults to 0.

    Returns:
        [list]: [Lista que contiene los datos de la columna correspondiente]
    """
    return [row[index] for row in obj]

#%%
def summarize_sort(sales, index=1, reverse=False, extend=True):
    """[Reduce la información en la list pasada como primer argumente, agrupando los datos e sus id unicos]

    Args:
        sales ([list]): [lista de entrada con la información a extraer]
        index (int, optional): [Indice de la posición de referencia para el ordenmiento]. Defaults to 1.
        reverse (bool, optional): [False de menor a mayor. True de mayor a menor]. Defaults to False.
        extend (bool, optional): [Flag especifico para diferenciar ente la lista de ventas y la de busquedas]. Defaults to True.

    Returns:
        [lista]: [Dependiendo del valor de extend = True: 
                una lista con los elementos unicos y la información id, ventas, reseña(avg), devoluciones
                extend = False:
                una lista con los elementos unicos y la información de id, conteo de busquedas.]
    """
    column = get_column(sales, 1)
    unique_items = list(set(column))
    unique_items_counted = [[item, column.count(item)] for item in unique_items]
    if extend:
        for idx, item in enumerate(unique_items):
            filtered = list(filter(lambda x:x[1]==item, sales))
            avg_review = round(sum(get_column(filtered, 2))/len(filtered), 1)
            count_return = sum(get_column(filtered, 4))
            unique_items_counted[idx].extend([avg_review, count_return])
    return sorted(unique_items_counted, key=lambda x: x[index], reverse=reverse)
#%%
def profits(products, sales, index, time_unit):
    """[Calcula las ganancias en determinada unidad de tiempo, años, meses o dias.]

    Args:
        products ([list]): [lista de entrada con la información de id y precio de cada producto]
        sales ([list]): [lista de entrada con la información de ventas a extraer]
        index ([int]): [0 para dias, 1 para meses, 2 para años]
        time_unit ([lista]): [lista con las unidades de tiempo a utilizar para el calculo, 
        está determinado por el valor de index: EX: si index = 0 time_unit sera una lista con los enteros de 1 a 30
        EX: si index = 1 time_unit sera una lista con los enteros de 1 a 12]

    Returns:
        [list]: [lista que contine cada unidad de tiempo y los ingresos acumulados]
    """
    result = [] 
    for time in time_unit:
        filtered = list(filter(lambda x:x[3].split('/')[index]==time, sales))
        items = summarize_sort(filtered)
        price_list = [products[item[0] -1][2] for item in items]
        acumulated = sum([item[1]*price for (item, price) in zip(items, price_list)])
        result.append([time, acumulated])
    return result
    
#%%
def print_list(printable, head='', fmt='{}\t{}\t{}'):
    """[permite que se muestren las listas en pantalla de una forma mas amigable y flexible]

    Args:
        printable ([list]): [lista a mostrar en pantalla]
        head (str, optional): [Cabecera de los datos a imprimir]. Defaults to ''.
        fmt (str, optional): [cadena especial que describe el formato deseado]. Defaults to '{}\t{}\t{}'.
    """
    if head:
        print(head)
    for row in printable:
        print(fmt.format(*row))
#%%
def zero_match(items, products):
    """[Devuelve todos los elementos de products que no se encuentran en items]

    Args:
        items ([list]): [Lista de elementos a excluir]
        products ([list]): [lista con el total de elementos]

    Returns:
        [lista]: [devuelve una lista que contiene los elementos de products que no se encuentran en items]
    """
    return [[product[0], product[1].split(',')[0]] for product in products if product[0] not in items]
#%%
if __name__ == "__main__":
    from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

    # Definición de usuarios y contraseñas, los elementos de las listas users y passw 
    # están relacionados 1 a 1, es decir la contraseña para el usuario que esta en la 
    # posición dos de la lista users sera unicamente la position dos de la lista passw
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
        
        ----> Resúmenes:
        7  -> Total de ingresos.
        8  -> Total anual.
        9  -> Ventas promedio mensuales.
        10 -> Meses con más ventas al año.

        11 -> Atrás.


        Opción:
    """

    while True:
        """
        [Ciclo principal para controlar la ejecución del programa.]
        """
        choice1 = input(welcome_msg)
        if choice1 == '1':
            user_logged = login(usrs, passw)
            if user_logged:
                while True: 
                    """
                    [Ciclo principal del menú de análisis.]
                    """
                    choice2 = input(analysis_msg)
                    if choice2 == "1": # Productos con mayores ventas.
                        result = summarize_sort(lifestore_sales, reverse=True)
                        joined_products = [[row[0], row[1], lifestore_products[row[0]-1][1].split(',')[0]] for row in result]
                        print_list(joined_products, head='Id\tVentas\tNombre')
                        input("\nPresione la tecla 'Enter' para regresar.")
                    elif choice2 == "2": # Productos con mayores busquedas.
                        result = summarize_sort(lifestore_searches, reverse=True, extend=False)
                        joined_products = [[row[0], row[1], lifestore_products[row[0]-1][1].split(',')[0]] for row in result]
                        print_list(joined_products, head='Id\tBúsquedas\tNombre', fmt='{}\t{}\t\t{}')
                        input("\nPresione la tecla 'Enter' para regresar.")
                    elif choice2 == "3": # Productos con menores ventas.
                        result = summarize_sort(lifestore_sales)
                        joined_products = [[row[0], row[1], lifestore_products[row[0]-1][1].split(',')[0]] for row in result]
                        print_list(joined_products, head='Id\tVentas\tNombre')
                        choice_zero = input("\nNota: por motivos de claridad se han excluido los productos con 0 ventas.\n"
                        "Presione la tecla 1 para mostrar los productos con 0 ventas.\n"
                        "Presione la tecla 'Enter' para regresar.")
                        if choice_zero == '1':
                            print('Productos con 0 ventas:\n')
                            result_zero = zero_match(get_column(result), lifestore_products)
                            print_list(result_zero, head='Id\tNombre', fmt='{}\t{}')
                            input("\nPresione la tecla 'Enter' para regresar.")
                        else:
                            continue
                    elif choice2 == "4": # Productos con menores busquedas.
                        result = summarize_sort(lifestore_searches, extend=False)
                        joined_products = [[row[0], row[1], lifestore_products[row[0]-1][1].split(',')[0]] for row in result]
                        print_list(joined_products, head='Id\tBúsquedas\tNombre', fmt='{}\t\t{}\t{}')
                        choice_zero = input("\nNota: por motivos de claridad se han excluido los productos con 0 búsquedas.\n"
                        "Presione la tecla 1 para mostrar los productos con 0 búsquedas.\n"
                        "Presione la tecla 'Enter' para regresar.")
                        if choice_zero == '1':
                            print('Productos con 0 ventas:\n')
                            result_zero = zero_match(get_column(result), lifestore_products)
                            print_list(result_zero, head='Id\tNombre', fmt='{}\t{}')
                            input("\nPresione la tecla 'Enter' para regresar.")
                    elif choice2 == "5": # Productos con las mejores reseñas.
                        result = summarize_sort(lifestore_sales, index=2, reverse=True)[:20]
                        joined_products = [[row[0], row[2], row[3], lifestore_products[row[0]-1][1].split(',')[0]] for row in result]
                        print_list(joined_products, head='Id\tReseña(AVG)\tDevoluciones\tNombre', fmt='{}\t{}\t\t{}\t\t{}')
                        input("\nPresione la tecla 'Enter' para regresar.")
                    elif choice2 == "6": # Productos con las peores reseñas.
                        result = summarize_sort(lifestore_sales, index=2)[:20]
                        joined_products = [[row[0], row[2], row[3], lifestore_products[row[0]-1][1].split(',')[0]] for row in result]
                        print_list(joined_products, head='Id\tReseña(AVG)\tDevoluciones\tNombre', fmt='{}\t{}\t\t{}\t\t{}')
                        input("\nPresione la tecla 'Enter' para regresar.")
                    elif choice2 == "7": # Total de ingresos.
                        total = profits(lifestore_products, lifestore_sales, 2, time_unit=['2019', '2020'])
                        print(f"Ingresos totales: {sum(get_column(total, 1))} MXN")
                        input("\nPresione la tecla 'Enter' para regresar.")
                    elif choice2 == "8": # Total anual.
                        total = profits(lifestore_products, lifestore_sales, 2, time_unit=['2019', '2020'])
                        print_list(total, head='Año\tIngresos(MXN)', fmt='{}\t{}')
                        input("\nPresione la tecla 'Enter' para regresar.")
                    elif choice2 == "9": # Ventas promedio mensuales.
                        total = profits(lifestore_products, lifestore_sales, 1, 
                                        time_unit=[str(month).zfill(2) for month in range(1, 13)])
                        months_avg = sum(get_column(total, 1))/len(total)
                        print(f"Ingresos promedio mensual: {round(months_avg, 2)} MXN")
                        input("\nPresione la tecla 'Enter' para regresar.")
                    elif choice2 == "10": # Meses con más ventas al año.
                        total = profits(lifestore_products, lifestore_sales, 1, 
                                        time_unit=[str(month).zfill(2) for month in range(1, 13)])
                        print_list(sorted(total, key=lambda x:x[1], reverse=True), head='Mes\tIngresos(MXN)', fmt='{}\t{}')
                        input("\nPresione la tecla 'Enter' para regresar.")
                    elif choice2 == "11": # Atrás.
                        break
                    else:
                        continue
            else:
                continue
        elif choice1 == '2':
            print('Bye Bye')
            break
# %%
