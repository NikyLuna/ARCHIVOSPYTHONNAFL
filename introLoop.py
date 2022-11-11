import time
nombre = input("escribe tu nombre: ")
#limiteSuperior=int(input("hasta que numero quieres llegar?"))
#for i in range (1,limiteSuperior+1):
   # print(i)
#time.sleep(i)


#for i in nombre:
    #print(i)
    #time.sleep(1)

position = int(input())
letra = nombre[position]
for i in nombre:
    print(i)
    time.sleep(1)
    if i == letra:
        break