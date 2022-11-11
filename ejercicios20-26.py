#ejercicio20
nombre=input("escribe tu primer nombre:")
length= len(nombre)
print(length)

#ejercicio21
primernombre=input("escribe tu primer nombre:")
apellido=input("escribe tu apellido en minusculas:")
nombre= primernombre + "  " + apellido
length=len(name)
print(name)

#ejercicio22
primernombre=input("escribe tu primer nombre en minusculas")
apellido=input("escribe tu apellido en minusculas")
primernombre=primernombre.title()
nombre=primernombre + " " + surname
print(name)

#ejercicio23
frase=input("escribe la primer linea de una rima infantil")
length= len(frase)
print("esto tiene", length, "letras en total" )
inicial=int(input("escribe un numero inicial:"))
final=int(input("escribe un numero final:"))
part=(frase(inicial:final))
print(part)

#ejercicio24
palabra=input("escribe una palabra")
palabra=palabra.upper
print(palabra)


#ejercicio25
nombre=input("escribe tu primer nombre:")
if len(nombre)<5:
    apellido=input("escribe tu apellido:")
    nombre=nombre+apellido
    print(name.upper())
else:
    print(name.lower())  


#ejercicio26
palabra=input("por favor escribe una palabra")     
first=palabra[0]
length=len(palabra)
rest=palabra[1:length]
if first != "a" and  first != "e" and first != "i" and first != "o" and first != "u"
      newword=rest + first + "ay"
else:
    newword= palabra + "way"  
print(newword.lower())   
