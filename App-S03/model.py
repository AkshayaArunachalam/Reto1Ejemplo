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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import tabulate as tabulate
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(decision):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }
    if int(decision) == 1:
        data_structs["data"] = lt.newList(datastructure="SINGLE_LINKED",
                                     cmpfunction=compare)
    elif int(decision) == 2:
        data_structs["data"] = lt.newList(datastructure="ARRAY_LIST",
                                     cmpfunction=compare)
    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #d = new_data(data["id"], data["info"])
    lt.addLast(data_structs["data"], data)


# Funciones para creacion de datos
def get_First_And_Last_Three(data_structs):
    lista1 = lt.newList("ARRAY_LIST")
    f = lt.getElement(data_structs["data"], 1)
    lt.addLast(lista1, f)
    s = lt.getElement(data_structs["data"], 2)
    lt.addLast(lista1, s)
    t = lt.getElement(data_structs["data"], 3)
    lt.addLast(lista1, t)
    lf = lt.getElement(data_structs["data"], lt.size(data_structs["data"]))
    lt.addLast(lista1, lf)
    ls = lt.getElement(data_structs["data"], lt.size(data_structs["data"]) -1)
    lt.addLast(lista1, ls)
    lst = lt.getElement(data_structs["data"], lt.size(data_structs["data"])-2)
    lt.addLast(lista1, lst)
    lista2 = lt.newList("ARRAY_LIST")
    for n in lt.iterator(lista1):
        m = {}
        m["Año"] = n["Año"]
        m["Código sector económico"] = n["Código sector económico"]
        m["Nombre sector económico"] = n["Nombre sector económico"]
        m["Código subsector económico"] = n["Código subsector económico"]
        m["Nombre subsector económico"] = n["Nombre subsector económico"]
        m["Código actividad económica"] = n["Código actividad económica"]
        m["Nombre actividad económica"] = n["Nombre actividad económica"]
        m["Total ingresos netos"] = n["Total ingresos netos"]
        m["Total costos y gastos"] = n["Total costos y gastos"]
        m["Total saldo a pagar"] = n["Total saldo a pagar"]
        m["Total saldo a favor"] = n["Total saldo a favor"]
        
        lt.addLast(lista2, m)
    return lista2

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(a_poranios):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    """
    Separamos en un diccionario los años para comparar cada actividad primero por años
    Despues 
    """
    mayores = lt.newList("ARRAY_LIST")
    for Anios in  a_poranios.keys():
        mayor = {}
        merg.sort(a_poranios[Anios],CMP_ValActEcon)
        x = lt.getElement(a_poranios[Anios], 1)
        mayor["Año"] = x["Año"]
        mayor["Código actividad económica"] = x["Código actividad económica"]
        mayor["Nombre actividad económica"] = x["Nombre actividad económica"]
        mayor["Código sector económico"] = x["Código sector económico"]
        mayor["Nombre sector económico"]= x["Nombre sector económico"]
        mayor["Código subsector económico."]= x["Código subsector económico"]
        mayor["Nombre subsector económico"]= x["Nombre subsector económico"]
        mayor["Total ingresos netos"]= x["Total ingresos netos"]
        mayor["Total costos y gastos"]= x["Total costos y gastos"]
        mayor["Total saldo a pagar"]= x["Total saldo a pagar"]
        mayor["Total saldo a favor"]= x["Total saldo a favor"]
        lt.addLast(mayores, mayor)
    merg.sort(mayores, sort_criteria)
    return mayores

    
def req_2(a_poranios):
    """
    Función que soluciona el requerimiento 2
    """
    mayores = lt.newList("ARRAY_LIST")
    for Anios in  a_poranios.keys():
        mayor = {}
        merg.sort(a_poranios[Anios],CMP_saf)
        x = lt.getElement(a_poranios[Anios], 1)
        mayor["Año"] = x["Año"]
        mayor["Código actividad económica"] = x["Código actividad económica"]
        mayor["Nombre actividad económica"] = x["Nombre actividad económica"]
        mayor["Código sector económico"] = x["Código sector económico"]
        mayor["Nombre sector económico"]= x["Nombre sector económico"]
        mayor["Código subsector económico."]= x["Código subsector económico"]
        mayor["Nombre subsector económico"]= x["Nombre subsector económico"]
        mayor["Total ingresos netos"]= x["Total ingresos netos"]
        mayor["Total costos y gastos"]= x["Total costos y gastos"]
        mayor["Total saldo a pagar"]= x["Total saldo a pagar"]
        mayor["Total saldo a favor"]= x["Total saldo a favor"]
        lt.addLast(mayores, mayor)
    merg.sort(mayores, sort_criteria)
    return mayores


def req_3(por_anios):
    # 
    """
    Función que soluciona el requerimiento 3
    """
    #primera parte req 3
    temp = por_anios.copy()
    final1 = lt.newList("ARRAY_LIST")
    b = lt.newList("ARRAY_LIST")
    for anio in por_anios.keys():
        sub_menor = 0
        menor = 100000000
        temp[anio] = organizar_por_subsector(temp[anio])
        for subsector in temp[anio].keys():
            total_ret = 0
            total_ing = 0
            total_cyg = 0
            total_sap = 0
            total_saf = 0
            
            for i in temp[anio][subsector]["elements"]:
                total_ret += int(i["Total retenciones"])
                
            if total_ret < menor:
                menor = total_ret
                sub_menor = subsector
                
        for i in lt.iterator(temp[anio][sub_menor]):
            total_ret += int(i["Total retenciones"])
            total_ing += int(i["Total ingresos netos"])
            total_cyg += int(i["Total costos y gastos"])
            total_sap += int(i["Total saldo a pagar"])
            total_saf += int(i["Total saldo a favor"])
            
        temp1 = {}
        sub_temp = lt.getElement(temp[anio][sub_menor], 1)
        subsector = sub_menor
        temp1["Año"] = anio
        temp1["Código sector económico"] = sub_temp["Código sector económico"]
        temp1["Nombre sector económico"] = sub_temp["Nombre sector económico"]
        temp1["Código subsector económico"] = sub_menor
        temp1["Nombre subsector económico"] = sub_temp["Nombre subsector económico"]
        temp1["Total retenciones subsector"] = menor
        temp1["Total ingresos netos subsector"] = total_ing
        temp1["Total costos y gastos subsector"] = total_cyg
        temp1["Total saldo a pagar"] = total_sap
        temp1["Total saldo a favor"] = total_saf
        temp1["subsector con menor retención: "] = sub_menor
        lt.addLast(final1, temp1)
        merg.sort(temp[anio][sub_menor], cmp_retencion_total)
        act_eco_menor_mayor_aporte = lt.newList("ARRAY_LIST")
        if lt.size(temp[anio][sub_menor]) >= 6:
            top1 = lt.getElement(temp[anio][sub_menor], 1)
            lt.addLast(act_eco_menor_mayor_aporte, top1)
            top2 = lt.getElement(temp[anio][sub_menor], 2)
            lt.addLast(act_eco_menor_mayor_aporte, top2)
            top3 = lt.getElement(temp[anio][sub_menor], 3)
            lt.addLast(act_eco_menor_mayor_aporte, top3)
            last1 = lt.getElement(temp[anio][sub_menor], lt.size(temp[anio][sub_menor]))
            lt.addLast(act_eco_menor_mayor_aporte, last1)
            last2 = lt.getElement(temp[anio][sub_menor], lt.size(temp[anio][sub_menor])-1)
            lt.addLast(act_eco_menor_mayor_aporte, last2)
            last3 = lt.getElement(temp[anio][sub_menor], lt.size(temp[anio][sub_menor])-2)
            lt.addLast(act_eco_menor_mayor_aporte, last3)
        else: 
            for element in lt.iterator(temp[anio][sub_menor]):
                lt.addLast(act_eco_menor_mayor_aporte, element)
        for i in lt.iterator(act_eco_menor_mayor_aporte):
            y = {}
            y["Año"] = anio
            y["Código subsector económico"] = sub_menor
            y["Código actividad económica"] = i["Código actividad económica"]
            y["Nombre actividad económica"] = i["Nombre actividad económica"]
            y["Total retenciones"] = i["Total retenciones"]
            y["Total ingresos netos"] = i["Total ingresos netos"]
            y["Total costos y gastos"] = i["Total costos y gastos"]
            y["Total saldo a pagar"] = i["Total saldo a pagar"]
            y["Total saldo a favor"] = i["Total saldo a favor"]
            
            lt.addLast(b, y)
    merg.sort(final1, sort_criteria)
    merg.sort(b, sort_criteria)
        
    return final1, b




def req_4(data_structs): 
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    
    #final
    
    dicc_year = {}
    
    for dta in lt.iterator(data_structs["data"]):
        if dta ['Año'] not in dicc_year:
            dicc_year[dta ['Año']]=lt.newList("ARRAY_LIST")
            lt.addLast( dicc_year[dta ['Año']] ,dta)
        else:
            lt.addLast( dicc_year[dta ['Año']] ,dta)
            
    
    hold = dicc_year.copy()
    final = lt.newList("ARRAY_LIST")
    for year in dicc_year.keys():
        holdON = {}
        hold[year] = organizar_por_subsector(hold[year])
        sub_mayor = 0
        menor = 100000000
        
        for subsector in hold[year].keys():
            total_cygnom = 0
            total_ingnet = 0
            total_cyg = 0
            total_sapagar = 0
            total_safavor = 0
   
            for i in hold[year][subsector]["elements"]:
                total_cygnom += int(i["Costos y gastos nómina"])
                
            if total_cygnom < menor:
                menor = total_cygnom
                sub_mayor = subsector
                
        for elemento in hold[year][sub_mayor]["elements"]:
            total_ingnet += int(elemento["Total ingresos netos"])
            total_cyg += int(elemento["Total costos y gastos"])
            total_sapagar += int(elemento["Total saldo a pagar"])
            total_safavor += int(elemento["Total saldo a favor"])

        sub_temp = lt.getElement(hold[year][sub_mayor], 1)
        subsector = sub_mayor
        holdON["Año"] = year
        holdON["Código sector económico"] = sub_temp["Código sector económico"]
        holdON["Nombre sector económico"] = sub_temp["Nombre sector económico"]
        holdON["Código subsector económico"] = sub_mayor
        holdON["Nombre subsector económico"] = sub_temp["Nombre subsector económico"]
        holdON["Costos y gastos nómina"] = total_cygnom  
        holdON["Total ingresos netos subsector"] = total_ingnet
        holdON["Total costos y gastos subsector"] = total_cyg
        holdON["Total saldo a pagar"] = total_sapagar
        holdON["Total saldo a favor"] = total_safavor
        holdON["subsector con menor retención: "] = sub_mayor
        lt.addLast(final, holdON)
        print (final)
    act_econ = lt.newList("ARRAY_LIST")
    
    for year in dicc_year:
        merg.sort(dicc_year[year], cmp_costos_gastos_nomina)
        size = lt.size(dicc_year[year])
        if size > 6:
            lt.addLast(act_econ, lt.getElement(dicc_year[year], 1))
            lt.addLast(act_econ, lt.getElement(dicc_year[year], 2))
            lt.addLast(act_econ, lt.getElement(dicc_year[year], 3))
            lt.addLast(act_econ, lt.getElement(dicc_year[year], lt.size(dicc_year[year])))
            lt.addLast(act_econ, lt.getElement(dicc_year[year], lt.size(dicc_year[year])-1))
            lt.addLast(act_econ, lt.getElement(dicc_year[year], lt.size(dicc_year[year])-2))
        else:
            for i in lt.iterator(dicc_year[year]):
                lt.addLast(act_econ, i)
    headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Costos y gastos nómina', 
                'Total ingresos netos', 'Total costos y gastos','Total saldo a pagar', 'Total saldo a favor']
    final_act_econ = [[x[headers[0]], x[headers[1]], x[headers[2]], x[headers[3]], x[headers[4]], 
                    x[headers[5]], x[headers[6]], x[headers[7]]] 
                    for x in act_econ['elements']]
            
    return final, final_act_econ, headers
        
    #try 2
    
    '''subsectores = {'0': 0, '1':0, '2':0, '3':0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9':0, '10': 0,
                        '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18':0, '19': 0, '20': 0, '21': 0}      
    dic_final= {}
    for year in dicc_year:
        dic_final[year]=subsectores
        for valores in lt.iterator(dicc_year[year]):
            if (valores['Año'] == year) and (subsectores[valores['Código subsector económico']] == 0):
                subsectores[valores['Código subsector económico']] = lt.newList('ARRAY_LIST')
                lt.addLast(subsectores[valores['Código subsector económico']], valores)
            elif (valores['Año'] == year) and (subsectores[valores['Código subsector económico']] != 0):
                lt.addLast(subsectores[valores['Código subsector económico']], valores)'''
    
    #try 1 /  lo tenia mal porque no estaba regresando el SUBSECTOR (ni su info) con mayor costo y gasto en nomina por ano,
    # estaba regresando las ACTIVIDADES ECONOMICAS con mayor costo y gasto en nomina
        
    '''
    headers = ['Año', 'Código actividad económica', 'Nombre sector económico','Código subsector económico', 
               'Nombre subsector económico', 'Total ingresos netos','Costos y gastos nómina', 
               'Total saldo a pagar', 'Total saldo a favor']
    for otherdta in dicc_year.keys():
        merg.sort(dicc_year[otherdta], cmp_gastosnomina)
        if lt.size(dicc_year[otherdta]) <= 6:
            exception = dicc_year[otherdta]
        #else: 
        final_mayor[otherdta]= [lt.getElement(dicc_year[otherdta], lt.size(dicc_year[otherdta])), 
                                lt.getElement(dicc_year[otherdta], lt.size(dicc_year[otherdta]) -1),
                                lt.getElement(dicc_year[otherdta], lt.size(dicc_year[otherdta]) -2)]
        
        final_menor[otherdta] = [lt.getElement(dicc_year[otherdta], 1), 
                                lt.getElement(dicc_year[otherdta], 2),
                                lt.getElement(dicc_year[otherdta], 3)]
        
        
    lista_final_mayor = [[[x[headers[0]], x[headers[1]], x[headers[2]], x[headers[3]], x[headers[4]], 
                           x[headers[5]], x[headers[6]], x[headers[7]], x[headers[8]]] 
                          for x in final_mayor[aja]]
                         for aja in final_mayor]
    
    lista_final_menor = [[[x[headers[0]], x[headers[1]], x[headers[2]], x[headers[3]], x[headers[4]], 
                           x[headers[5]], x[headers[6]], x[headers[7]], x[headers[8]]] 
                          for x in final_mayor[ootherdta]]
                         for ootherdta in final_menor]'''

def cmp_costos_gastos_nomina (data1, data2):
    return int(data1['Costos y gastos nómina']) < int(data2['Costos y gastos nómina'])


def organizar_por_subsector(data_structs):
    por_subsector = {}
    for i in lt.iterator(data_structs):
            if i ['Código subsector económico'] not in por_subsector:
                por_subsector[i ['Código subsector económico']]=lt.newList(datastructure= "ARRAY_LIST") #data_structs["datastructure"]
                lt.addLast( por_subsector[i['Código subsector económico']] ,i)            
            else:
                lt.addLast( por_subsector[i['Código subsector económico']] ,i)
    return por_subsector
     


def req_5(annios):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    
    copiaanios = annios.copy()
    f1 = lt.newList("ARRAY_LIST")
    #mayor=0
    for anio in annios.keys():
        m1 = {}
        copiaanios[anio] = organizar_por_subsector(copiaanios[anio])
        sub_mayor = 0
        mayor = 100
        
        for subsector in copiaanios[anio].keys():
            total_desctribu = 0
            total_ingrenest = 0
            total_saldapag = 0
            total_saldafav = 0
            total_costygastnom = 0

        
            for i in copiaanios[anio][subsector]["elements"]:
                total_desctribu += int(i["Descuentos tributarios"])
            sub_mayor=subsector
            
            if total_desctribu > mayor:
                mayor = total_desctribu
                sub_mayor = subsector

                
        for elemento in copiaanios[anio][sub_mayor]["elements"]:
            total_ingrenest += int(elemento["Total ingresos netos"])
            total_costygastnom += int(elemento["Total costos y gastos"])
            total_saldapag += int(elemento["Total saldo a pagar"])
            total_saldafav += int(elemento["Total saldo a favor"])
            total_desctribu += int(elemento["Descuentos tributarios"])

        sub_temp = lt.getElement(copiaanios[anio][sub_mayor], 1)
        subsector = sub_mayor
        m1["Año"] = anio
        m1["Código sector económico"] = sub_temp["Código sector económico"]
        m1["Nombre sector económico"] = sub_temp["Nombre sector económico"]
        m1["Código subsector económico"] = sub_mayor
        m1["Nombre subsector económico"] = sub_temp["Nombre subsector económico"]
        m1["Total descuentros tributarios del subsector"] = total_desctribu
        m1["Total ingresos netos subsector"] = total_ingrenest
        m1["Costos y gastos nómina"] = total_costygastnom  
        m1["Total saldo a pagar"] = total_saldapag
        m1["Total saldo a favor"] = total_saldafav
        lt.addLast(f1, m1)
        
    econact = lt.newList("ARRAY_LIST")
    
    for anio in annios:
        merg.sort(annios[anio], cmp_dtribu)
        size = lt.size(annios[anio])
        if size > 6:
            lt.addLast(econact, lt.getElement(annios[anio], 1))
            lt.addLast(econact, lt.getElement(annios[anio], 2))
            lt.addLast(econact, lt.getElement(annios[anio], 3))
            lt.addLast(econact, lt.getElement(annios[anio], lt.size(annios[anio])))
            lt.addLast(econact, lt.getElement(annios[anio], lt.size(annios[anio])-1))
            lt.addLast(econact, lt.getElement(annios[anio], lt.size(annios[anio])-2))
        else:
            for i in lt.iterator(annios[anio]):
                lt.addLast(econact, i)
    headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Costos y gastos nómina', 
                'Total ingresos netos', 'Total costos y gastos','Total saldo a pagar', 'Total saldo a favor']
    factecon = [[x[headers[0]], x[headers[1]], x[headers[2]], x[headers[3]], x[headers[4]], 
                    x[headers[5]], x[headers[6]], x[headers[7]]] 
                    for x in econact['elements']]
            
    return f1, factecon, headers
        
def cmp_dtribu (data1, data2):
    return int(data1['Descuentos tributarios']) > int(data2['Descuentos tributarios'])



def req_6(data_structs, anio):
    """
    Función que soluciona el requerimiento 6
    """
    elem_anio = data_structs[anio].copy()
    merg.sort(elem_anio, cmp_CSE)
    elem_anio = organizar_por_sector(elem_anio)
    infos_sectores = lt.newList("ARRAY_LIST")
    infos_subsectores = lt.newList("ARRAY_LIST")
    infos_actividades_eco = lt.newList("ARRAY_LIST")
    for sector in elem_anio.keys():
        info_sector = {}
        total_in = 0
        total_cyg = 0
        total_sap = 0
        total_saf = 0

        for i in lt.iterator(elem_anio[sector]):
            total_in += int(i["Total ingresos netos"])
            total_cyg += int(i["Total costos y gastos"])
            total_sap += int(i["Total saldo a pagar"])
            total_saf += int(i["Total saldo a favor"])
        info_sector["Código sector económico"] = sector
        info_sector["Nombre sector económico"] = (lt.getElement(elem_anio[sector], 1))["Nombre sector económico"]
        info_sector["Total ingresos netos de sector"] = total_in
        info_sector["Total costos y gastos de sector"] = total_cyg
        info_sector["Total saldo a pagar de sector"] = total_sap
        info_sector["Total saldo a favor de sector"] = total_saf
        elem_anio[sector] = organizar_por_subsector(elem_anio[sector])
        menor = 1000000000000
        mayor = -1
        sub_menor = 0
        sub_mayor = 0
        for subsector in elem_anio[sector].keys():
            total_ret = 0
            total_ing = 0
            total_cyg = 0
            total_sap = 0
            total_saf = 0
            
            for i in elem_anio[sector][subsector]["elements"]:
                total_ing += int(i["Total ingresos netos"])
                
            if total_ret < menor:
                menor = total_ing
                sub_menor = subsector
            if total_ret > mayor:
                mayor = total_ing
                sub_mayor = subsector
        info_sector["Subsector que más aportó"] = sub_mayor
        info_sector["Subsector que menos aportó"] = sub_menor
        lt.addLast(infos_sectores, info_sector)
        #sub menor
        for i in lt.iterator(elem_anio[sector][sub_menor]):
            total_ret += int(i["Total retenciones"])
            total_ing += int(i["Total ingresos netos"])
            total_cyg += int(i["Total costos y gastos"])
            total_sap += int(i["Total saldo a pagar"])
            total_saf += int(i["Total saldo a favor"])
            
        temp1 = {}
        sub_temp = lt.getElement(elem_anio[sector][sub_menor], 1)
        subsector = sub_menor
        temp1["Código sector económico"] = sub_temp["Código sector económico"]
        temp1["Nombre sector económico"] = sub_temp["Nombre sector económico"]
        temp1["Código subsector económico qué menos aportó"] = sub_menor
        temp1["Nombre subsector económico qué menos aportó"] = sub_temp["Nombre subsector económico"]
        temp1["Total ingresos netos subsector"] = total_ing
        temp1["Total costos y gastos subsector"] = total_cyg
        temp1["Total saldo a pagar"] = total_sap
        temp1["Total saldo a favor"] = total_saf
        temp1["subsector con menor retención: "] = sub_menor
        
        merg.sort(elem_anio[sector][sub_menor], cmp_ingresos_netos)
        act_eco_menor_mayor_aporte = lt.newList("ARRAY_LIST")
        top1 = lt.getElement(elem_anio[sector][sub_menor], 1)
        lt.addLast(act_eco_menor_mayor_aporte, top1)
        last1 = lt.getElement(elem_anio[sector][sub_menor], lt.size(elem_anio[sector][sub_menor]))
        lt.addLast(act_eco_menor_mayor_aporte, last1)
        for i in lt.iterator(act_eco_menor_mayor_aporte):
            y = {}
            y["Código subsector económico qué menos aportó"] = sub_menor
            y["Código actividad económica"] = i["Código actividad económica"]
            y["Nombre actividad económica"] = i["Nombre actividad económica"]
            y["Total ingresos netos"] = i["Total ingresos netos"]
            y["Total costos y gastos"] = i["Total costos y gastos"]
            y["Total saldo a pagar"] = i["Total saldo a pagar"]
            y["Total saldo a favor"] = i["Total saldo a favor"]
        lt.addLast(infos_actividades_eco, y)
        lt.addLast(infos_subsectores, temp1)
        #sub mayor
        for i in lt.iterator(elem_anio[sector][sub_mayor]):
            total_ret += int(i["Total retenciones"])
            total_ing += int(i["Total ingresos netos"])
            total_cyg += int(i["Total costos y gastos"])
            total_sap += int(i["Total saldo a pagar"])
            total_saf += int(i["Total saldo a favor"])
        temp1 = {}
        sub_temp = lt.getElement(elem_anio[sector][sub_mayor], 1)
        subsector = sub_mayor
        temp1["Código sector económico"] = sub_temp["Código sector económico"]
        temp1["Nombre sector económico"] = sub_temp["Nombre sector económico"]
        temp1["Código subsector económico qué más aportó"] = sub_mayor
        temp1["Nombre subsector económico qué más aportó"] = sub_temp["Nombre subsector económico"]
        temp1["Total ingresos netos subsector"] = total_ing
        temp1["Total costos y gastos subsector"] = total_cyg
        temp1["Total saldo a pagar"] = total_sap
        temp1["Total saldo a favor"] = total_saf
        temp1["subsector con menor retención: "] = sub_mayor
        
        merg.sort(elem_anio[sector][sub_mayor], cmp_ingresos_netos)
        act_eco_menor_mayor_aporte = lt.newList("ARRAY_LIST")
        merg.sort(elem_anio[sector][sub_mayor], cmp_ingresos_netos)
        act_eco_menor_mayor_aporte = lt.newList("ARRAY_LIST")
        top1 = lt.getElement(elem_anio[sector][sub_mayor], 1)
        lt.addLast(act_eco_menor_mayor_aporte, top1)
        last1 = lt.getElement(elem_anio[sector][sub_mayor], lt.size(elem_anio[sector][sub_mayor]))
        lt.addLast(act_eco_menor_mayor_aporte, last1)
        for i in lt.iterator(act_eco_menor_mayor_aporte):
            y = {}
            y["Código subsector económico qué menos aportó"] = sub_mayor
            y["Código actividad económica"] = i["Código actividad económica"]
            y["Nombre actividad económica"] = i["Nombre actividad económica"]
            y["Total ingresos netos"] = i["Total ingresos netos"]
            y["Total costos y gastos"] = i["Total costos y gastos"]
            y["Total saldo a pagar"] = i["Total saldo a pagar"]
            y["Total saldo a favor"] = i["Total saldo a favor"]
        lt.addLast(infos_actividades_eco, y)
        lt.addLast(infos_subsectores, temp1)
    return infos_sectores, infos_subsectores, infos_actividades_eco

        
#approach 2 de req6 (no está implementado)
def req6_beta(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    sectores = lt.newList("ARRAY_LIST")
    for i in lt.iterator(data_structs):
        if i["Código sector económico"] not in sectores["elements"]:
            lt.addLast(sectores, i["Código sector económico"])
    total_ingresos_sector = lt.newList("ARRAY_LIST")
    total_cyg = lt.newList("ARRAY_LIST")
    total_sap = lt.newList("ARRAY_LIST")
    total_saf = lt.newList("ARRAY_LIST")
    for j in lt.iterator(sectores):
        lt.addLast(total_ingresos_sector, 0)
        lt.addLast(total_cyg, 0)
        lt.addLast(total_sap, 0)
        lt.addLast(total_saf, 0)
    for j in range(0, lt.size(sectores)+1):
        for i in lt.iterator(data_structs):
            if lt.getElement(sectores, j) == i["Código sector económico"]:
                lt.changeInfo(total_ingresos_sector, j, (int(lt.getElement(total_ingresos_sector, j)) + int(i["Total ingresos netos"])))
                lt.changeInfo(total_cyg, j, (int(lt.getElement(total_cyg, j)) + int(i["Total costos y gastos"])))
                lt.changeInfo(total_sap, j, (int(lt.getElement(total_sap, j)) + int(i["Total saldo a pagar"])))
                lt.changeInfo(total_saf, j, (int(lt.getElement(total_saf, j)) + int(i["Total saldo a favor"])))
    
    #segunda parte:
    subsectores = lt.newList("ARRAY_LIST")
    for i in lt.iterator(data_structs):
        if i["Código subsector económico"] not in subsectores["elements"]:
            lt.addLast(subsectores, i["Código subsector económico"])
    total_subsector = lt.newList("ARRAY_LIST")
    nombre_subsector = lt.newList("ARRAY_LIST")
    sub_cyg = lt.newList("ARRAY_LIST")
    sub_sap = lt.newList("ARRAY_LIST")
    sub_saf = lt.newList("ARRAY_LIST")
    act_eco = lt.newList("ARRAY_LIST")
    for i in range (0, lt.size(subsectores)+1):
        lt.addLast(total_subsector, 0)
        lt.addLast(nombre_subsector, " ")
        lt.addLast(sub_cyg, 0)
        lt.addLast(sub_sap, 0)
        lt.addLast(sub_saf, 0)
    for j in range (0, lt.size(subsectores)+1):
        act_eco_sub = lt.newList("ARRAY_LIST")
        for i in lt.iterator(data_structs):
            if lt.getElement(subsectores, j) == i["Código subsector económico"]:
                lt.changeInfo(nombre_subsector, j, i["Nombre subsector económico"])
                lt.changeInfo(total_subsector, j, (int(lt.getElement(total_subsector, j)) + int(i["Total ingresos netos"])))
                lt.changeInfo(sub_cyg, j, (int(lt.getElement(sub_cyg, j)) + int(i["Total costos y gastos"])))
                lt.changeInfo(sub_sap, j, (int(lt.getElement(sub_sap, j)) + int(i["Total saldo a pagar"])))
                lt.changeInfo(sub_saf, j, (int(lt.getElement(sub_saf, j)) + int(i["Total saldo a favor"])))
                lt.addLast(act_eco_sub, i)
        quk.sort(act_eco_sub, cmp_ingresos_netos)
        lt.addLast(act_eco, act_eco_sub)
        
    temp = {}
    for j in lt.iterator(sectores):
        x = lt.newList("ARRAY_LIST")
        for k in lt.iterator(subsectores):
            for i in lt.iterator(data_structs):
                if j == i["Código sector económico"] and k == i["Código subsector económico"] and k not in x["elements"]:
                    lt.addLast(x,k)
        temp[j] = x
    
    datos_sector = lt.newList("ARRAY_LIST")
    #><
    for sector in temp.keys():
        datos = lt.newList("ARRAY_LIST")
        menor = 10000000
        mayor = -1
        pos_mayor = 0
        pos_menor = 0
        pos_sector = 0
        u = 0
        encontrado1 = False
        while encontrado1 == False and u < lt.size(sectores):
            if lt.getElement(sectores, u) == sector:
                pos_sector = u
                encontrado1 = True
            else:
                u+=1
        for subsector in lt.iterator(temp[sector]):
            pos_sub = 0
            i = 0
            encontrado = False
            while i > lt.size(subsectores) and encontrado == False:
                if subsector == lt.getElement(subsectores, i):
                    encontrado = True
                    pos_sub = i
                else:
                    i+=1
            if lt.getElement(total_subsector, pos_sub) > mayor:
                mayor = lt.getElement(total_subsector, pos_sub)
                pos_mayor = pos_sub
            elif lt.getElement(total_subsector, pos_sub) < menor:
                menor = lt.getElement(total_subsector, pos_sub)
                pos_menor = pos_sub
        mayor_menos = lt.getElement((lt.getElement(act_eco, pos_mayor)), lt.size(lt.getElement(act_eco, pos_mayor)))
        mayor_mas = lt.getElement((lt.getElement(act_eco, pos_mayor)), 1)
        menor_menos = lt.getElement((lt.getElement(act_eco, pos_menor)), lt.size(lt.getElement(act_eco, pos_menor)))
        menor_mas = lt.getElement((lt.getElement(act_eco, pos_menor)), 1)
    
        #datos finales necesarios 1
        cod_sector = sector
        total_ingresos_sector1 = lt.getElement(total_ingresos_sector, pos_sector)
        total_cyg1 = lt.getElement(total_cyg, pos_sector)
        total_sap1= lt.getElement(total_sap, pos_sector)
        total_saf1 = lt.getElement(total_saf, pos_sector)
    
        sector_m = {}
        sector_m["Código de sector"] = cod_sector
        sector_m["Total ingresos sector"] = total_ingresos_sector1
        sector_m["Total costos y gastos sector"] = total_cyg1
        sector_m["Total saldo a pagar sector"] = total_sap1
        sector_m["Total saldo a favor sector"] = total_saf1
    
        #datos finales necesarios 2
    
        #sub mayor
        codigo_subsector_mayor = lt.getElement(subsectores, pos_mayor)
        nombre_subsector_mayor = lt.getElement(nombre_subsector, pos_mayor)
        total_subsector1 = lt.getElement(total_subsector, pos_mayor)
        sub_cyg1 = lt.getElement(sub_cyg, pos_mayor)
        sub_sap1= lt.getElement(sub_sap, pos_mayor)
        sub_saf1 = lt.getElement(sub_saf, pos_mayor)
    
        subsector_mayor = {}
        subsector_mayor["Código subsector"]= codigo_subsector_mayor
        subsector_mayor["Nombre subsector"]= nombre_subsector_mayor
        subsector_mayor["Total ingresos subsector"]= total_subsector1
        subsector_mayor["Total costos y gastos subsector"]= sub_cyg1
        subsector_mayor["Total saldo a pagar subsector"]= sub_sap1
        subsector_mayor["Total saldo a favor subsector"]= sub_saf1
    
        #sub mayor actividad que más aportó
        act_cod_mayor_mas = mayor_mas["Código actividad económica"]
        act_nom_mayor_mas = mayor_mas["Nombre actividad económica"]
        act_tin_mayor_mas = mayor_mas["Total ingresos netos"]
        act_sap_mayor_mas = mayor_mas["Total saldo a pagar"]
        act_saf_mayor_mas = mayor_mas["Total saldo a favor"]
    
        sub_mayor_mas = {}
        sub_mayor_mas["Código actividad económica"] = act_cod_mayor_mas
        sub_mayor_mas["Nombre actividad económica"] = act_nom_mayor_mas
        sub_mayor_mas["Total ingresos netos"] = act_tin_mayor_mas
        sub_mayor_mas["Total saldo a pagar"] = act_sap_mayor_mas
        sub_mayor_mas["Total saldo a favor"] = act_saf_mayor_mas
    
        #sub mayor actividad que menos aportó
        act_cod_mayor_menos = mayor_menos["Código actividad económica"]
        act_nom_mayor_menos = mayor_menos["Nombre actividad económica"]
        act_tin_mayor_menos = mayor_menos["Total ingresos netos"]
        act_sap_mayor_menos = mayor_menos["Total saldo a pagar"]
        act_saf_mayor_menos = mayor_menos["Total saldo a favor"]
    
        sub_mayor_menos = {}
        sub_mayor_menos["Código actividad económica"] = act_cod_mayor_menos
        sub_mayor_menos["Nombre actividad económica"] = act_nom_mayor_menos
        sub_mayor_menos["Total ingresos netos"] = act_tin_mayor_menos
        sub_mayor_menos["Total saldo a pagar"] = act_sap_mayor_menos
        sub_mayor_menos["Total saldo a favor"] = act_saf_mayor_menos

        #sub menor
        codigo_subsector_mayor2 = lt.getElement(subsectores, pos_menor)
        nombre_subsector_mayor2 = lt.getElement(nombre_subsector, pos_menor)
        total_subsector2 = lt.getElement(total_subsector, pos_menor)
        sub_cyg2 = lt.getElement(sub_cyg, pos_menor)
        sub_sap2 = lt.getElement(sub_sap, pos_menor)
        sub_saf2 = lt.getElement(sub_saf, pos_menor)

        subsector_menor = {}
        subsector_menor["Código subsector menor"] = codigo_subsector_mayor2
        subsector_menor["Nombre subsector menor"] = nombre_subsector_mayor2
        subsector_menor["Total ingresos subsector menor"] = total_subsector2
        subsector_menor["Total costos y gastos subsector menor"] = sub_cyg2
        subsector_menor["Total saldo a pagar subsector menor"] = sub_sap2
        subsector_menor["Total saldo a favor subsector menor"] = sub_saf2

        #sub menor actividad que más aportó
        act_cod_menor_mas = menor_mas["Código actividad económica"]
        act_nom_menor_mas = menor_mas["Nombre actividad económica"]
        act_tin_menor_mas = menor_mas["Total ingresos netos"]
        act_sap_menor_mas = menor_mas["Total saldo a pagar"]
        act_saf_menor_mas = menor_mas["Total saldo a favor"]
    
        sub_menor_mas = {}
        sub_menor_mas["Código actividad económica"] = act_cod_menor_mas
        sub_menor_mas["Nombre actividad económica"] = act_nom_menor_mas
        sub_menor_mas["Total ingresos netos"] = act_tin_menor_mas
        sub_menor_mas["Total saldo a pagar"] = act_sap_menor_mas
        sub_menor_mas["Total saldo a favor"] = act_saf_menor_mas
    
        #sub menor actividad que menos aportó
        act_cod_menor_menos = menor_menos["Código actividad económica"]
        act_nom_menor_menos = menor_menos["Nombre actividad económica"]
        act_tin_menor_menos = menor_menos["Total ingresos netos"]
        act_sap_menor_menos = menor_menos["Total saldo a pagar"]
        act_saf_menor_menos = menor_menos["Total saldo a favor"]
    
        sub_menor_menos = {}
        sub_menor_menos["Código actividad económica"] = act_cod_menor_menos
        sub_menor_menos["Nombre actividad económica"] = act_nom_menor_menos
        sub_menor_menos["Total ingresos netos"] = act_tin_menor_menos
        sub_menor_menos["Total saldo a pagar"] = act_sap_menor_menos
        sub_menor_menos["Total saldo a favor"] = act_saf_menor_menos

        lt.addLast(datos, sector_m)
        lt.addLast(datos, subsector_mayor)
        lt.addLast(datos, sub_mayor_mas)
        lt.addLast(datos, sub_mayor_menos)
        lt.addLast(datos, subsector_menor)
        lt.addLast(datos, sub_menor_mas)
        lt.addLast(datos, sub_menor_menos)
        lt.addLast(datos_sector, datos)
    
    return datos
    


def req_7(data_structs, top, anio1, anio2):
    """
    Función que soluciona el requerimiento 7
    """
    datos_en_rango = lt.newList("ARRAY_LIST")
    for datos in lt.iterator(data_structs["data"]):
        if int(datos["Año"]) in range(int(anio1), int(anio2)+1):
            lt.addLast(datos_en_rango, datos)
    sa.sort(datos_en_rango, cmp_tcyg)
    final = lt.newList("ARRAY_LIST")
    rango = 1
    if int(top)> lt.size(datos_en_rango):
        rango = range(1, lt.size(datos_en_rango))
    else:
        rango = range(1, int(top)+1)
    for n in rango:
        x = lt.getElement(datos_en_rango, n)
        temp1 = {}
        temp1["Año"] = x["Año"]
        temp1["Código actividad económica"] = x["Código actividad económica"]
        temp1["Nombre actividad económica"] = x["Nombre actividad económica"]
        temp1["Código sector económico"] = x["Código sector económico"]
        temp1["Nombre sector económico"] = x["Nombre sector económico"]
        temp1["Total ingresos netos consolidados para periodo"] = x["Total ingresos netos"]
        temp1["Total costos y gastos a pagar para periodo consolidado"] = x["Total costos y gastos"]
        temp1["Total saldo a pagar para periodo consolidado"] = x["Total saldo a pagar"]
        temp1["Total saldo a favor para periodo consolidado"] = x["Total saldo a favor"]
        lt.addLast(final, temp1)
    return final



def req_8(data_structs, top, anio1, anio2):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    datos_en_rango = lt.newList("ARRAY_LIST")
    for datos in lt.iterator(data_structs["data"]):
        if int(datos["Año"]) in range(int(anio1), int(anio2)+1):
            lt.addLast(datos_en_rango, datos)
    sa.sort(datos_en_rango, cmp_tic)
    final = lt.newList("ARRAY_LIST")
    rango = 1
    if int(top)> lt.size(datos_en_rango):
        rango = range(1, lt.size(datos_en_rango))
    else:
        rango = range(1, int(top)+1)
    for n in rango:
        x = lt.getElement(datos_en_rango, n)
        temp1 = {}
        temp1["Año"] = x["Año"]
        temp1["Código actividad económica"] = x["Código actividad económica"]
        temp1["Nombre actividad económica"] = x["Nombre actividad económica"]
        temp1["Código sector económico"] = x["Código sector económico"]
        temp1["Nombre sector económico"] = x["Nombre sector económico"]
        temp1["Total ingresos netos consolidados para periodo"] = x["Total ingresos netos"]
        temp1["Total costos y gastos a pagar para periodo consolidado"] = x["Total costos y gastos"]
        temp1["Total saldo a pagar para periodo consolidado"] = x["Total saldo a pagar"]
        temp1["Total saldo a favor para periodo consolidado"] = x["Total saldo a favor"]
        lt.addLast(final, temp1)
    return final

def cmp_tic(data1, data2):
    return int(data1["Total Impuesto a cargo"]) < int(data2["Total Impuesto a cargo"])

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort(data_structs, algoritmo, cmp_func):
    """
    Función encargada de ordenar la lista con los datos
    """
    if cmp_func == None:
        cmp_func = cmp_impuestos_by_anio_CAE
    elif cmp_func == 1:
        cmp_func = sort_criteria
    if algoritmo == 1:
        sa.sort(data_structs, cmp_func)
    elif algoritmo == 2:
        ins.sort(data_structs, cmp_func)
    elif algoritmo == 3:
        se.sort(data_structs, cmp_func)
    elif algoritmo == 4:
        merg.sort(data_structs, cmp_func)
    elif algoritmo == 5:
        quk.sort(data_structs, cmp_func)
    else:
        sa.sort(data_structs, cmp_func)
        
def organizar_por_anios(data_structs):
    a_poranios={}
    for i in lt.iterator(data_structs["data"]):
        if i ['Año'] not in a_poranios:
            a_poranios[i ['Año']]=lt.newList(datastructure= "ARRAY_LIST")
            lt.addLast( a_poranios[i ['Año']] ,i)            
        else:
            lt.addLast( a_poranios[i ['Año']] ,i)
    return a_poranios

def organizar_por_subsector(data_structs):
    por_subsector = {}
    for i in lt.iterator(data_structs):
            if i ['Código subsector económico'] not in por_subsector:
                por_subsector[i ['Código subsector económico']]=lt.newList(datastructure= "ARRAY_LIST") #data_structs["datastructure"]
                lt.addLast( por_subsector[i['Código subsector económico']] ,i)            
            else:
                lt.addLast( por_subsector[i['Código subsector económico']] ,i)
    return por_subsector

def organizar_por_sector(data_structs):
    por_sector = {}
    for i in lt.iterator(data_structs):
            if i ['Código sector económico'] not in por_sector:
                por_sector[i ['Código sector económico']]=lt.newList(datastructure= "ARRAY_LIST") #data_structs["datastructure"]
                lt.addLast( por_sector[i['Código sector económico']] ,i)            
            else:
                lt.addLast( por_sector[i['Código sector económico']] ,i)
    return por_sector

#Funciones de Comparación
def cmp_tcyg(data1, data2):
    return int(data1["Total costos y gastos"]) < int(data2["Total costos y gastos"])
def cmp_impuestos_by_anio_CAE(data_1, data_2): 
    """
    Devuelve verdadero (True) si el año de impuesto1 es menor que el de impuesto2, en caso de que sean iguales tenga en cuenta 
    el código de la actividad económica, de lo contrario devuelva falso (False).
    Args:
    impuesto1: información del primer registro de impuestos que incluye el “Año” y el
    “  Código
        actividad económica”
        impuesto2: información del segundo registro de impuestos que incluye el “Año” y el
        “Código actividad económica”
    """
    codigo_1 = data_1["Código actividad económica"].replace("y"," ").replace("/"," ").replace("*","")
    codigo_2 = data_2["Código actividad económica"].replace("y"," ").replace("/"," ").replace("*","")
    codigo_1 = codigo_1.split()
    codigo_2 = codigo_2.split()
    x = (int (data_1["Año"]) < int (data_2["Año"]))
    if x == False:
        x = (int (codigo_1[0])) < (int (codigo_2[0]))
    return x


def cmp_ingresos_netos(data_1,data_2):
    return int(data_1["Total ingresos netos"]) > int(data_2["Total ingresos netos"])
def cmp_CSE(data1, data2):
    return int(data1["Código sector económico"]) < int(data1["Código sector económico"])
def CMP_ValActEcon(data1, data2):
    return (int (data1["Total saldo a pagar"]) > int (data2["Total saldo a pagar"]))
def CMP_saf(data1, data2):
    return (int (data1["Total saldo a favor"]) > int (data2["Total saldo a favor"]))

def cmp_retencion_total(data_1, data_2):
    return int (data_1["Total retenciones"]) < int (data_2["Total retenciones"])

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    return int (data_1["Año"]) > int (data_2["Año"])

#def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    return int (data_1["Año"]) > int (data_2["Año"])



