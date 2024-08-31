# -*-coding:UTF-8 -*-

print "Veamos cuántos dias, minutos y segundos has vivido."
name = str(raw_input("nombre: "))

print("ahora escribe tu edad")
age = int(input("edad: "))

days = age * 365
minutes = age * 525948
seconds = age * 31556926

print name, "ha estado vivo por", days,"días", minutes, "minutos y", seconds, "segundos "