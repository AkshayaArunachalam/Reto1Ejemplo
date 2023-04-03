"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 
 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from tabulate import tabulate
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    print ('Antes de continuar con el programa escoge el tipo de E. de datos que deseas')
    decision  = input("1.) Single linked list 2.) Array List \n")    
    control = controller.new_controller(decision)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información o añadir de un archivo diferente")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Cambiar algoritmo de ordenamiento")
    print("11- Obtener dato dado un ID")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    print("Puede elegir los siguientes archivos: \n small, 5pct, 20pct, 30pct, 50pct, 80pct, large")
    archivo = input("Por favor escriba el sufijo del archivo que quiere cargar (E.j. small): \n")
    print("Cargando información de los archivos ....\n")
    data = controller.load_data(control, archivo, None)
    if data[0] == False:
        print("opción erronea, vuelva a intentar \n")
    else:
        print(f"hay un total de {data[0]} filas  \n ")
        print(tabulate(data[1]["elements"], headers="keys", tablefmt="fancy_grid",maxcolwidths=[4,9,11,12,12,12,12,12,12,10], maxheadercolwidths=[4,9,8,9,12,12,12,12,12,10]))
        print(f"el programa duró {data[2]} en correr")
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)


def print_req_1(por_anios):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    

    
    x = controller.req_1(por_anios)
    print(tabulate(x["elements"], headers="keys", tablefmt="fancy_grid",maxcolwidths=[4,9,11,12,12,12,12,12,12,10,10,10], maxheadercolwidths=[4,9,8,9,12,12,12,12,12,10,10,10]))


def print_req_2(por_anios):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    x = controller.req_2(por_anios)
    print(tabulate(x["elements"], headers="keys", tablefmt="fancy_grid",maxcolwidths=[4,9,11,12,12,12,12,12,12,10,10,10], maxheadercolwidths=[4,9,8,9,12,12,12,12,12,10,10,10]))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    x = controller.req_3(control)
    a = x[0]
    b = x[1]
    print("\n Los subsectores que menos aportaron al total de retenciones de cada año son: \n")
    print(tabulate(a["elements"], headers="keys", tablefmt="fancy_grid",maxcolwidths=[4,9,11,12,12,12,12,12,12,10,10,10], maxheadercolwidths=[4,9,8,9,12,12,12,12,12,10,10,10]))
    print("\n las actividades economicas que más(3) y menos(3) aportaron a dichos subsectores fueron: \n ")
    print(tabulate(b["elements"], headers="keys", tablefmt="fancy_grid",maxcolwidths=[4,9,11,12,12,12,12,12,12,10,10,10], maxheadercolwidths=[4,9,8,9,12,12,12,12,12,10,10,10]))
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    
    final, act_econ, headz = controller.req_4(control)
    final_tabbed = tabulate(final['elements'], headers='keys')
    print ('\n\n')
    print(final_tabbed)
    print ('\n\n')
    print("\n Las 3 actividades económicas que más aportaron y las 3 actividades que menos aportaron al valor total de costos y gastos de nómina en cada año, son los siguientes (de menor a mayor aporte): \n ")
    act_econ_tabbed = tabulate(act_econ, headers=headz)

    print (act_econ_tabbed)
    print("\n")
    


def print_req_5(control):
    """
    Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    
    final, act_econ, headz = controller.req_5(control)
    final_tabbed = tabulate(final['elements'], headers='keys')
    print ('\n\n')
    print(final_tabbed)
    print ('\n\n')
    print("\n Las 3 actividades económicas que más aportaron y las 3 actividades que mas aportaron en descuento tributario, son los siguientes (de menor a mayor aporte): \n ")
    act_econ_tabbed = tabulate(act_econ, headers=headz)
    print (act_econ_tabbed)
    print("\n")
    #print(controller.req_5(control))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    print("escriba el año del cual quiere ver la mayor actividad economica para cada sector: \n")
    anio = input()
    x = controller.req_6(control, anio)
    a = x[0]
    b = x[1]
    c = x[2]
    print("\n la info de cada sector es: \n")
    print(tabulate(a["elements"], headers="keys", tablefmt="fancy_grid", maxcolwidths=[4,9,11,12,12,12,12,12,12], maxheadercolwidths=[4,9,8,9,12,12,12,12,12]))
    print("\n la info de cada subsector es: \n")
    print(tabulate(b["elements"], headers="keys", tablefmt="fancy_grid"))
    print("\n la info de cada actividad es: \n")
    print(tabulate(c["elements"], headers="keys", tablefmt="fancy_grid", maxcolwidths=[4,9,11,12,12,12,12,12,12], maxheadercolwidths=[9,9,8,9,12,12,12,12,12]))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    print("\n por favor indique el top N de elementos que desea ver: \n")
    top = input()
    print("\n por favor indique el año por el cual quiere empezar el periodo de busqueda: \n")
    anio1 = input()
    print("\n por favor indique el año por el cual quiere terminar el periodo de busqueda: \n")
    anio2 = input()
    final = controller.req_7(control , top, anio1, anio2)
    print(tabulate(final, headers="keys", tablefmt="fancy_grid", maxcolwidths=[4,9,11,12,12,12,12,12,12], maxheadercolwidths=[4,9,8,9,12,12,12,12,12]))
    #print(final)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    print(controller.req_8(control))
    
def print_req_9(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    
    print("\n por favor indique el top N de elementos que desea ver: \n")
    top = input()
    print("\n por favor indique el año por el cual quiere empezar el periodo de busqueda: \n")
    anio1 = input()
    print("\n por favor indique el año por el cual quiere terminar el periodo de busqueda: \n")
    anio2 = input()
    final = controller.req_9(control, top, anio1, anio2)
    #print(tabulate(final, headers="keys", tablefmt="fancy_grid", maxcolwidths=[4,9,11,12,12,12,12,12,12], maxheadercolwidths=[4,9,8,9,12,12,12,12,12]))
    print (final)


      
# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) in [2,3,4,6,7]:
                por_anios = controller.organizar_por_anio(control)
            if int(inputs) == 1:
                load_data(control)

            elif int(inputs) == 2:
                print_req_1(por_anios)

            elif int(inputs) == 3:
                print_req_2(por_anios)

            elif int(inputs) == 4:
                print_req_3(por_anios)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(por_anios)

            elif int(inputs) == 7:
                print_req_6(por_anios)

            elif int(inputs) == 8:
                print_req_7(control)
                
            elif int(inputs) == 9:
                print_req_9(control)

            elif int(inputs) == 10:
                algoritmo = input("Ingrese el tipo de algoritmo con el cual quiere ordenar los datos\
                    \n Algoritmos iterativos \n 1. Shell sort \n 2. Insertion sort \n 3. Selectionsort \n\n \
                        Algoritmos recursivos \n 4. Merge sort \n 5. Quick sort \n")
                tiempo = controller.sort(control["model"], algoritmo, None)
                print(f"el programa duró {tiempo} ms")
                if tiempo != False:
                    print_req_8(control)
                else:
                    print("opción incorrecta, vuelva a intentar")

            elif int(inputs) == 11:
                id = input("Ingrese un id: ")
                print_data(control, id)
            
            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")       
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)
