#22. Se tienen tres baldes de agua, uno de cinco litros, otros de tres litros y otro de un litro; si el de un litro tarda una hora y media en
#  llenarse, resuelva cuanto tiempo pueden tardar en llenarse los otros baldes. Si tiene tres baldes, pero se desconoce su tamaño debe de 
# resolver igualmente el ejercicio. 
''' Cada litro de agua demora un total de 1:30 horas o 90 minutos. Entonces para saber cuales baldes son debemos de saber cuanto tiempo 
se demoraron en llenarse'''
tiempoxlitro=1.5
baldes=[5,3,1]
tiempoDllenado=[]
for i in baldes:
    tiempoDllenado.append(i*tiempoxlitro)
print(tiempoDllenado)
