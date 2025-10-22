#4.	Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura si la primera nota tiene un valor del 20%, la segunda del 30% y la última del 50%.
Definitiva=(5*0.20)+(3*0.30)+(1*0.50 )
nota1=float(input("Ingresa nota 1: "))
nota2=float(input("Ingresa nota 2: "))
nota3=float(input("Ingresa nota 3: "))
print(f"Definitiva es:{(nota1*0.20)+(nota2*0.30)+(nota3*0.50)}")