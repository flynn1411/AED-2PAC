#-*-coding:utf-8-*-

graph = {
    "A":["B", "C", "E"],
    "B":["A","C", "D"],
    "C":["A", "B", "E"],
    "D":["B"],
    "E":["A", "C"]
}

for vertex in graph:
    edges = ""
    for edge in graph[vertex]:
        edges += "%s "%(edge)
    print("%s: %s"%(vertex, edges))

print("\n")

#Función para encontrar todos los caminos entre dos vertices, aun en pruebas
def findPaths(graph, vertex, destination, path = [], visited = []):
    #Agrego el vertice actual a la ruta y lo marco como visitado(para evitar ciclos)
    visited.append(vertex)
    path.append(vertex)

    #Si el vertice actual es mi destino, imprimo la ruta seguida
    if (vertex == destination):
        print(path)

    #Si no es el destino, se iteran las aristas del vertice actual
    else:
        for edge in graph[vertex]:
            #Si la arista actual no se encuentra en los visitados, se llama recursivamente la función 
            #para seguir avanzando
            if(not edge in visited):
                findPaths(graph, edge, destination, path, visited)

    #Luego de encontrar el destino, se retrocede un paso para poder buscar mas posibles caminos
    path.pop()
    visited.pop()

print("Todos los posibles caminos entre E y D:\n")
findPaths(graph, "E", "D")