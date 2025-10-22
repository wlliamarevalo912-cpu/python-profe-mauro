#7.	Dada una cantidad de tiempo medida en horas, minutos y segundos, diga a cuántos segundos equivale.
horas=int(input("dame las horas"))
min=int(input("dame los minutos"))
seg=int(input("dame los segundos"))
print(f"La cantidad de{seg+(min*60)+((horas*60)*60)} ")