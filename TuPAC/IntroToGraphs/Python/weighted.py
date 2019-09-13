#-*-coding:utf-8-*-

graph = {
    "A":[
            {"B":{"weight":13}}, 
            {"C":{"weight":8}},
            {"E":{"weight":5}}
        ],

    "B":[
            {"A":{"weight":13}},
            {"C":{"weight":7}},
            {"D":{"weight":15}}
        ],

    "C":[
            {"A":{"weight":8}},
            {"B":{"weight":7}},
            {"E":{"weight":10}}
        ],

    "D":[
            {"B":{"weight":15}}
        ],

    "E":[
            {"A":{"weight":5}},
            {"C":{"weight":10}}
        ]
}

for vertex in graph:
    edges = ""
    for edge in graph[vertex]:
        for key,value in edge.items():
         edges += "%s(%s) "%(key, value.get("weight"))
    print("%s: %s"%(vertex, edges))

print("\n")


#Función para encontrar todos los caminos entre dos vertices, aun en pruebas
def findPaths(graph, vertex, destination, path = [], visited = [], weight = 0):
    #Agrego el vertice actual a la ruta y lo marco como visitado(para evitar ciclos)
    visited.append(vertex)
    path.append(vertex)

    #Si el vertice actual es mi destino, imprimo la ruta seguida
    if (vertex == destination):
        print("La ruta: %s con el peso %s"%(path, weight))

    #Si no es el destino, se iteran las aristas del vertice actual
    else:
        for edge in graph[vertex]:
            #Si la arista actual no se encuentra en los visitados, se llama recursivamente la función 
            #para seguir avanzando
            for key, value in edge.items():
                if(not key in visited):
                    findPaths(graph, key, destination, path, visited, weight+(value.get("weight")))

    #Luego de encontrar el destino, se retrocede un paso para poder buscar mas posibles caminos
    path.pop()
    visited.pop()

print("Todos los posibles caminos entre E y D:")
findPaths(graph, "E", "D")