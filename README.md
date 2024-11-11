Punto de Pago Air (PPA), una aerolínea en fase de lanzamiento 
planea iniciar operaciones en 8 aeropuertos nacionales colombianos: BOG, MDE, BAQ, BGA, SMR, CTG, CLO y EOH. 
La aerolínea ha establecido un itinerario semanal fijo, es decir, los mismos vuelos operarán los mismos días cada semana. 
Sin embargo, debido al tamaño inicial de la flota, no todos los aeropuertos estarán conectados por vuelos directos.
Como ingeniero de desarrollo, se te solicita diseñar e implementar una funcionalidad de búsqueda de vuelos 
que permita a los usuarios consultar los posibles itinerarios entre cualquier par de aeropuertos dentro de la red de PPA, 
considerando una fecha de viaje específica. El sistema debe ser capaz de encontrar rutas directas 
y aquellas que involucren escalas en otros aeropuertos de la red, así como organizar los resultados por duración 
o tiempo total del viaje.


El sistema hace uso de un grafo para la visualizacion de los vuelos. Se consideran tres casos:
1- vuelos directos
2- vuelos con 1 escalas
3- vuelos con dos escalas
4- vuelos con mas de dos escalas

El objetivo es encontrar un vuelo entre las ciudades de Bogota y Barranquilla (BOG y BAQ) Se crean vuelos según el caso con su duración en minutos









