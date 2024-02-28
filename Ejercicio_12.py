#Declaracion de variables
Salario_bruto = 0
Retencion_fuente = 0
Salario_neto = 0
#Proceso
Salario_bruto = 48 * 5000
Retencion_fuente = Salario_bruto * 0.125
Salario_neto = Salario_bruto - Retencion_fuente
#Salida
print(f'El salario bruto es ${Salario_bruto}')
print(f'La retencion en la fuente es ${Retencion_fuente}')
print(f'El salario neto es ${Salario_neto}')
