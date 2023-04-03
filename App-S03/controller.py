"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tabulate as tab
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(decision):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(decision)
    return control


# Funciones para la carga de datos

def load_data(control, filename, cmp_func):
    """
    Carga los datos del reto
    """
    if filename in ["small", "5pct", "20pct", "30pct", "50pct", "80pct", "large"]:
        datafile = cf.data_dir + "DIAN/Salida_agregados_renta_juridicos_AG-" + filename +".csv"
        data = csv.DictReader(open(datafile, encoding="utf-8"))
        for row in data:
            model.add_data(control["model"], row)
        delta_t = sort(control["model"], 1, cmp_func)
        primeros_y_ultimos = model.get_First_And_Last_Three(control["model"])
        size = model.data_size(control["model"])
        return size, primeros_y_ultimos, delta_t
    else:
        return False, False, False

def organizar_por_anio(control):
    return model.organizar_por_anios(control["model"])

# Funciones de ordenamiento

def sort(control, algoritmo, cmp_func):
    """
    Ordena los datos del modelo
    """
    if int(algoritmo) in [1,2,3,4,5]:
        start_time = get_time()
        model.sort(control["data"], int(algoritmo), cmp_func)
        end_time = get_time()
        delta_t = delta_time(start_time, end_time)
        return delta_t
    else:
        return False


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data

def organizar_por_anio(control):
    return model.organizar_por_anios(control["model"])

def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    req_1 = model.req_1(control)
    return req_1


def req_2(por_anios):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    req_2 = model.req_2(por_anios)
    return req_2


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    x = model.req_3(control)
    return x


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    
    final, act_econ, headers = model.req_4(control["model"])
    
    return final, act_econ, headers



def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    def req_1(control):
    req_1, headers = model.req_1(control["model"])
    return req_1, headers
    """
    # TODO: Modificar el requerimiento 5
    req_5, final_act_econ, headers= model.req_5(control)
    #model.sort(req_5, 5, 1)
    return req_5, final_act_econ, headers


def req_6(control, anio):
    """
    Retorna el resultado del requerimiento 6
    """
    x = model.req_6(control, anio)
    return x


def req_7(control, top, anio1, anio2):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    req_7 = model.req_7(control["model"], top, anio1, anio2)
    return req_7["elements"]


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req_8 = model.req_8(control["model"])
    return req_8

def req_9(control, top, anio1, anio2):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req_9 = model.req_8(control["model"], top, anio1, anio2)    
    return req_9


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
