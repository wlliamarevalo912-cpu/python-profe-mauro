#11.	Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.  Dicha calificación se compone de los siguientes porcentajes:
#	55% del promedio de sus tres calificaciones parciales.
# 	30% de la calificación del examen final. 
#	15% de la calificación de un trabajo final
nota_parcial=[]
promedio1=0
for i in range(3):
    nota=float(input(f"Cual es tu nota #{i+1}: "))
    nota_parcial.append(nota)
for j in nota_parcial:
   promedio1=promedio1+j
promedio1=promedio1/3
print(promedio1)
examen_f=float(input("Cuanto sacaste en el examen final"))
trabajo_final=float(input("Cuanto sacaste en el trabajo final"))
print(f"El promedio de la materia fue {(promedio1*0.55)+(examen_f*0.30)+(trabajo_final*0.15)}")