from math import pi
#Declaracion de variables
areaCirculo = 0
circunferencia = 0
#Proceso
radio = 4
areaCirculo = pi * pow(radio,2)
areaCirculo = round(areaCirculo,2)
circunferencia = 2 * pi * radio
circunferencia = round(circunferencia,2)
#Salida
print(f'El área del circulo es {areaCirculo} unidades cuadradas')
print(f'La longitud de la circunferencia es {circunferencia} unidades')