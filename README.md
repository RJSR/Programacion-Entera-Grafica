# Programacion Entera Grafica
Aplicación Python que resuelve un problema de optimización con librería Pulp

## Librerías Usadas
### Pulp
Librería usada para la resolución de problemas lineales, se instala con:
```
python -m pip install pulp
```

### PyQT6
Librería usada para la creación de GUIs (Graphic User Interfaces), en este caso, se usa la 6ta versión, implementada para la ventana con la resolución del problema, se instala con:
```
python -m pip install pyqt6
```

### Matplotlib
Librería usada para la creación de gráficos matemáticos y estadísticos, en este caso, usado para mostrar los puntos de intersección para obtener la respuestaa al problema
```
python -m pip install matplotlib
```

### Numpy
Librería usada por su amplias herramientas a la hora de resolver problemas matemáticos, en este caso, usado para crear los valores de los ejes X y Y de la gráfica
```
python -m pip install numpy
```

### Shapely
Librería que permite la manipulación y analisis de objetos geometricos planos, usado en este caso para obtener el area de posibles respuestas al problema planteado.
```
python -m pip install shapely
```

## Problema a solucionar
```
Un Avión que hace el recorrido Caracas-Bogotá, ofrece asientos para fumadores al precio de 100 dolares y a no fumadores al precio de 60 dolares. Al no fumador se le deja llevar 40 Kg. de peso y al fumador 10 Kg. Si el avión tiene 100 asientos y admite un equipaje de hasta 2.000 Kg. ¿Cuál ha de ser la oferta de asientos de la compañía para cada tipo de pasajeros, con la finalidad de optimizar el beneficio? Además, se debe considerar que por políticas de la empresa, deben ofrecerse cómo mínimo 5 asientos para pasajeros no fumadores.
```
Es decir, se debe maximizar la respuesta para obtener el mayor beneficio.

## Puntos a mejorar

- Implementación de la librería `matplotlib` dentro de la GUI en `PyQT6`, ya sea con la creación de un segundo layout en la ventana principal, o añadiendo un botón conectado a una segunda ventana.
- Modificación de la funcionalidad, al preguntarle al usuario la función objetivo, y las restricciones, para obtener la optimización de otros problemas, esto requiere previa familiarización del usuario con el tema.
- Re-implementar la GUI usando otras librerías, como `Django` o `Flet` para mejor flexbilidad y mayor documentación.
