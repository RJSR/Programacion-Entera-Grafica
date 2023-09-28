# Librería Pulp para los cálculos
import pulp
import sys

# Librería PyQt6 para la interfaz
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel,
        QMainWindow, QGridLayout)

# Numpy
import numpy as np

# Librerías de matplot
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from shapely.geometry import LineString

"""
Un Avión que hace el recorrido Caracas-Bogotá, ofrece asientos para fumadores al precio de 100 dolares y a no fumadores al precio de 60 dolares. Al no fumador se le deja llevar 40 Kg. de peso y al fumador 10 Kg. Si el avión tiene 100 asientos y admite un equipaje de hasta 2.000 Kg. ¿Cuál ha de ser la oferta de asientos de la compañía para cada tipo de pasajeros, con la finalidad de optimizar el beneficio? Además, se debe considerar que por políticas de la empresa, deben ofrecerse cómo mínimo 5 asientos para pasajeros no fumadores.
"""

prob = """Un Avión que hace el recorrido Caracas-Bogotá, ofrece asientos para fumadores al precio de 100 dolares y a no fumadores al precio de 60 dolares. Al no fumador se le deja llevar 40 Kg. de peso y al fumador 10 Kg. Si el avión tiene 100 asientos y admite un equipaje de hasta 2.000 Kg. ¿Cuál ha de ser la oferta de asientos de la compañía para cada tipo de pasajeros, con la finalidad de optimizar el beneficio? Además, se debe considerar que por políticas de la empresa, deben ofrecerse cómo mínimo 5 asientos para pasajeros no fumadores."""

# 1. Definir las variables de decisión
x = pulp.LpVariable("x", lowBound=1) # Fumador
y = pulp.LpVariable("y", lowBound=1) # No Fumador

# 2. Establecer la función objetivo
funcion_objetivo = 100 * x + 60 * y

# 3. Agregar restricciones
restricciones = [
    10 * x + 40 * y <= 2000,
    x + y <= 100,
    y >= 5,
    y >= 0
    
]

# 4. Resolver el problema de programación entera lineal utilizando PuLP
problema = pulp.LpProblem("Problema de Programación Lineal", pulp.LpMaximize)
problema += funcion_objetivo
for restriccion in restricciones:
    problema += restriccion

problema.solve()

# 5. Asignación de los resultados a variables, para ser usados en la interfaz
punto_1 = x.varValue
punto_2 = y.varValue
resultado = pulp.value(problema.objective)


# 6. Creación de la ventana principal
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # 6.1. Creación de las etiquetas
        titulo = QLabel("Problema de Programación Lineal")
        myFont=QtGui.QFont('Arial', 12)
        myFont.setBold(True)

        titulo.setFont(myFont)
        enun = QLabel(prob, alignment=Qt.AlignmentFlag.AlignJustify)
        enun.setWordWrap(True)

        funcion = QLabel("Función Objetivo: 100 * x + 60 * y", alignment=Qt.AlignmentFlag.AlignJustify)
        res1 = QLabel("Restricción 1: 10 * x + 40 * y <= 2000", alignment=Qt.AlignmentFlag.AlignJustify)

        res2 = QLabel("Restricción 2: x + y <= 100", alignment=Qt.AlignmentFlag.AlignJustify)
        res3 = QLabel("Restricción 3: y >= 5", alignment=Qt.AlignmentFlag.AlignJustify)
        res4 = QLabel("Restricción 4: y >= 0", alignment=Qt.AlignmentFlag.AlignJustify)
        titulo2 = QLabel("Asignación óptima de recursos", alignment=Qt.AlignmentFlag.AlignHCenter)


        x1 = QLabel(f"Fumadores = {punto_1}", alignment=Qt.AlignmentFlag.AlignJustify)
        y1 = QLabel(f"No Fumadores = {punto_2}", alignment=Qt.AlignmentFlag.AlignJustify)
        final = QLabel(f"Beneficio máximo obtenido: {resultado}", alignment=Qt.AlignmentFlag.AlignJustify)

        Font=QtGui.QFont('Arial', 10)
        Font.setBold(True)
        final.setFont(Font)
        titulo2.setFont(Font)


        # 6.2. Asignación de los espacios a los componentes
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.setContentsMargins(20,20,20,30)
        grid.addWidget(titulo, 0, 0)
        grid.addWidget(enun, 1, 0)
        grid.addWidget(funcion, 2, 0)
        grid.addWidget(res1, 3, 0)
        grid.addWidget(res2, 4, 0)
        grid.addWidget(res3, 5, 0)
        grid.addWidget(res4, 6, 0)
        grid.addWidget(titulo2, 7, 0)
        grid.addWidget(x1, 8, 0)
        grid.addWidget(y1, 9, 0)
        grid.addWidget(final, 10, 0)

        # 6.3. Datos finales del widget
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)
        self.setGeometry(500, 100, 400, 600)
        self.setWindowTitle('Problema de Programación Lineal')
        self.show()




# 7. Ejecución de la ventana
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

#8. Gráfica de las ecuaciones y el área de resultados.

#8.1 Ecuaciones e intervalos (Restricciones despejadas)
x = np.arange(-100, 150, 50)
y = np.arange(-100, 150, 50)
y1 = (2000 - (10 * x))/ 40
y2 = 100 - x
y3 = 5 + (0 * x)
x1 = 0 * y
y4 = 0 * x
z = (-100 * x) / 600

#8.2 Identificadores para las líneas
primera_linea = LineString(np.column_stack((x, y1)))
segunda_linea = LineString(np.column_stack((x, y2)))
tercera_linea = LineString(np.column_stack((x, y3)))
cuarta_linea = LineString(np.column_stack((x1, y)))
quinta_linea = LineString(np.column_stack((x, y4)))
sexta_linea = LineString(np.column_stack((x, z)))

#8.3 Graficando las líneas
plt.plot(x, y1, '-', linewidth=2, color='b')
plt.plot(x, y2, '-', linewidth=2, color='g')
plt.plot(x, y3, '-', linewidth=2, color='r')
plt.plot(x1, y, '-', linewidth=2, color='y')
plt.plot(x, y4, '-', linewidth=2, color='k')
plt.plot(x, z, ':', linewidth=1, color='k')

#8.4 Generando las intersecciones (vértices)
primera_interseccion = cuarta_linea.intersection(primera_linea)
segunda_interseccion = primera_linea.intersection(segunda_linea)
tercera_interseccion = segunda_linea.intersection(tercera_linea)
cuarta_interseccion = tercera_linea.intersection(cuarta_linea)

#8.5 Graficando los vértices
plt.plot(*primera_interseccion.xy, 'o')
plt.plot(*segunda_interseccion.xy, 'o')
plt.plot(*tercera_interseccion.xy, 'o')
plt.plot(*cuarta_interseccion.xy, 'o')

#8.5 Imprimiendo las coordenadas de los vértices en la consola
print('\n COORDENADAS DE LAS INTERSECCIONES')
print('Coordenadas de la primera intersección: {} '.format(primera_interseccion))
print('Coordenadas de la segunda intersección: {} '.format(segunda_interseccion))
print('Coordenadas de la tercera intersección: {} '.format(tercera_interseccion))
print('Coordenadas de la cuarta intersección: {} '.format(cuarta_interseccion))

#8.6 Identificando los valores de las coordenadas x y y de cada vértice
xi1m, yi1m = primera_interseccion.xy
xi2m, yi2m = segunda_interseccion.xy
xi3m, yi3m = tercera_interseccion.xy
xi4m, yi4m = cuarta_interseccion.xy

#8.8 Cambiamos el formato de matriz a float
xi1 = np.float64(np.array(xi1m))
xi2 = np.float64(np.array(xi2m))
xi3 = np.float64(np.array(xi3m))
xi4 = np.float64(np.array(xi4m))
yi1 = np.float64(np.array(yi1m))
yi2 = np.float64(np.array(yi2m))
yi3 = np.float64(np.array(yi3m))
yi4 = np.float64(np.array(yi4m))

#8.9 Evaluando la función objetivo en cada vértice
FOi1 = (xi1 * 100) + (yi1 * 60)
FOi2 = (xi2 * 100) + (yi2 * 60)
FOi3 = (xi3 * 100) + (yi3 * 60)
FOi4 = (xi4 * 100) + (yi4 * 60)

#8.10 Imprimiendo las evaluaciones de la FO en cada vértice (Consola)
print('\n EVALUACIÓN DE LA FO EN LOS VÉRTICES')
print('Función objetivo en la intersección 1: {} pesos'.format(FOi1))
print('Función objetivo en la intersección 2: {} pesos'.format(FOi2))
print('Función objetivo en la intersección 3: {} pesos'.format(FOi3))
print('Función objetivo en la intersección 4: {} pesos'.format(FOi4))

#9. Calculando el mejor resultado (Maximizar)
ZMAX = max(FOi1, FOi2, FOi3, FOi4)

#10. Imprimiendo la solución óptima en la consola
print('\n SOLUCIÓN ÓPTIMA')
print('Solución óptima: {} pesos'.format(ZMAX))

#11. Ordenando las coordenadas de los vértices (Las coordenadas x en m y las coordenadas y en n)
m = [xi1, xi2, xi3, xi4]
n = [yi1, yi2, yi3, yi4]

#12. Graficando el polígono solución a partir de las coordenadas de los vértices 
plt.fill(m, n, color='silver')

#13. Identificando el índice del vértice de la mejor solución
dict1 = {0:FOi1, 1:FOi2, 2:FOi3, 3:FOi4}
posicion = max(dict1, key=dict1.get)

#14. Obteniendo las coordenadas del vértice de la mejor solución de acuerdo al índice
XMAX = m[posicion]
YMAX = n[posicion]

#15. Imprimiendo las coordenadas del vértice de la mejor solución (variables de decisión)
print('\n VARIABLES DE DECISIÓN')
print('Cantidad de asientos a reservar para fumadores: {} '.format(XMAX))
print('Cantidad de asientos a reservar para no fumadores: {} '.format(YMAX))

#16. Generando las anotaciones de las coordenadas y solución óptima en el gráfico
plt.annotate('  X: {0} / Y: {1} (Coordenadas)'.format(XMAX, YMAX), (XMAX, YMAX))
plt.annotate('  Solución óptima: {}'.format(ZMAX), (XMAX, YMAX+3))


#17. Configuraciones adicionales del gráfico
plt.grid()
plt.xlabel('Asientos para fumadores')
plt.ylabel('Asientos para no fumadores')
plt.title('Método Gráfico')

#18. Iniciación de la gráfica
plt.show()