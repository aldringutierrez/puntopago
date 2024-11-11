from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

g_salida = 'Bogota';
g_llegada = 'Barranquilla';
g_arrVuelos = []
g_arrTrasbordos = []

def reservas():
    cargar_vuelos()
    vuelo=vuelo_directo()
    if len(vuelo) >0:
        print(vuelo)
        print('valor total = ' + str(vuelo[2]))
        return
    vuelo=vuelo_transbordo_1()
    if len(vuelo) > 0:
        print(vuelo)
        print('valor total = ' + str(int(vuelo[2]) + int(vuelo[4])))
        return
    vuelo=vuelo_transbordo_2()
    if len(vuelo) > 0:
        print(vuelo)
        print('valor total = ' + str(int(vuelo[2]) + int(vuelo[4]) + int(vuelo[6])))
        return
    print('No se encontraron vuelos')
#    vuelo_transbordo_3()
#    vuelo_transbordo_4()
#    vuelo_transbordo_5()

def cargar_vuelos():
    global g_arrTrasbordos
    try:
        grapho = DiGraph()
        grapho.add_node('Bogota')
        grapho.add_node('Medellin')
        grapho.add_node('Cali')
        grapho.add_node('Barranquilla')
        grapho.add_node('Santa Marta')
        grapho.add_node('Cartagena')
        grapho.add_node('Bucaramanga')
        grapho.add_node('Olaya Herrera')
        #--------------- vuelo directo
        # grapho.add_edge('Bogota', 'Medellin', 30)
        # grapho.add_edge('Bogota', 'Bucaramanga', 35)
        # grapho.add_edge('Bogota', 'Cartagena', 70)
        # grapho.add_edge('Cali', 'Barranquilla', 80)
        # grapho.add_edge('Cali', 'Cartagena', 85)
        # grapho.add_edge('Medellin', 'Cali', 25)
        # grapho.add_edge('Medellin', 'Barranquilla', 50)
        # grapho.add_edge('Bucaramanga', 'Barranquilla', 25)
        # grapho.add_edge('Bogota', 'Barranquilla', 70)
        #--------------- vuelo 1 escala
        # grapho.add_edge('Bogota', 'Medellin', 30)
        # grapho.add_edge('Bogota', 'Bucaramanga', 35)
        # grapho.add_edge('Bogota', 'Cartagena', 70)
        # grapho.add_edge('Cali', 'Barranquilla', 80)
        # grapho.add_edge('Cali', 'Cartagena', 85)
        # grapho.add_edge('Medellin', 'Cali', 25)
        # grapho.add_edge('Medellin', 'Barranquilla', 50)
        # grapho.add_edge('Bucaramanga', 'Barranquilla', 25)
        #--------------- vuelo 2 escalas
        grapho.add_edge('Bogota', 'Medellin', 30)
        grapho.add_edge('Bogota', 'Bucaramanga', 35)
        grapho.add_edge('Bogota', 'Cartagena', 70)
        grapho.add_edge('Cali', 'Barranquilla', 80)
        grapho.add_edge('Cali', 'Cartagena', 85)
        grapho.add_edge('Medellin', 'Cali', 25)

        #plotea el grapho (falla con muchos puntos)
        #g_algo = GraphAlgo(grapho)
        #print(g_algo.centerPoint())
        #print(g_algo.TSP([1, 2, 4]))
        #g_algo.plot_graph()

        for fin, dicts in grapho._inedges.items():
            for ini, weight in dicts.items():
                tmp1 = []
                tmp1.append(ini)
                tmp1.append(fin)
                tmp1.append(str(weight))
                g_arrVuelos.append(tmp1);
        #print(g_arrVuelos)
        for vuelo in g_arrVuelos:
            if vuelo[0] == g_salida:
                g_arrTrasbordos.append(vuelo)
        #print(g_arrTrasbordos)

    except Exception as e:
        print('exc')
        print(e)

def vuelo_directo():
    for vuelo in g_arrVuelos:
        if vuelo[0] == g_salida and vuelo[1] == g_llegada:
            return vuelo
    return []

def vuelo_transbordo_1():
    global g_arrTrasbordos
    arrTrasbordos2=[]
    for vuelo in g_arrTrasbordos:
        if vuelo[0] == g_salida:
            destinos = buscar_intermedias(vuelo[1])
            for item in destinos:
                tmp1 = []
                tmp1.append(vuelo[0])
                tmp1.append(vuelo[1])
                tmp1.append(vuelo[2])
                tmp1.append(item[1])
                tmp1.append(item[2])
                arrTrasbordos2.append(tmp1)

    g_arrTrasbordos=[]
    for item in arrTrasbordos2:
        g_arrTrasbordos.append(item)
    arrTrasbordos2 = buscar_llegada(arrTrasbordos2)
    minimo = buscar_minimo1(arrTrasbordos2);
    return minimo

def vuelo_transbordo_2():
    global g_arrTrasbordos
    arrTrasbordos2=[]
    for vuelo in g_arrTrasbordos:
        destinos = buscar_intermedias(vuelo[3])
        for item in destinos:
            tmp1 = []
            tmp1.append(vuelo[0])
            tmp1.append(vuelo[1])
            tmp1.append(vuelo[2])
            tmp1.append(vuelo[3])
            tmp1.append(vuelo[4])
            tmp1.append(item[1])
            tmp1.append(item[2])
            arrTrasbordos2.append(tmp1)

    arrTrasbordos2 = buscar_llegada(arrTrasbordos2)
    minimo = buscar_minimo2(arrTrasbordos2);
    return minimo

def buscar_intermedias(intermedia):
    arrReturn=[]
    for item in g_arrVuelos:
        if item[0] == intermedia:
            arrReturn.append(item)
    return arrReturn

def buscar_llegada(arrTrasbordos2):
    arrReturn=[]
    for item in arrTrasbordos2:
        for item2 in item:
            if item2 == g_llegada:
                arrReturn.append(item)
    return arrReturn

def buscar_minimo1(arrTrasbordos):
    arrMontos=[]
    for item in arrTrasbordos:
        monto = int(item[2])+int(item[4])
        arrMontos.append(monto)
    for item in arrTrasbordos:
        if int(item[2])+int(item[4])==min(arrMontos):
            return item
    return []

def buscar_minimo2(arrTrasbordos):
    arrMontos=[]
    for item in arrTrasbordos:
        monto = int(item[2])+int(item[4])+int(item[6])
        arrMontos.append(monto)
    for item in arrTrasbordos:
        if int(item[2])+int(item[4])+int(item[6])==min(arrMontos):
            return item
    return []


if __name__ == '__main__':
    reservas()
