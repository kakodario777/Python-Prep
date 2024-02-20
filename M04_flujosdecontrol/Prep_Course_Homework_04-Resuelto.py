#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:


a = 5
if a>0:
    print("A es mayor que 0")
elif a<0:
    print("A es menor que cero")
else:
    print("A es igual a 0")


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:


a = 5
b = 25
if type(a) == type(b):
    print("A y B Son el mismo tipo de dato")
else:
    print("A y B No son el mismo tipo de dato")


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:


for e in range(1,21):
    if e % 2 == 0:
        print(str(e),"Es par")
        
    else:
        print(str(e),"No es par")


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:


for i in range(0,6):
    print(str(i), "elevado a la tercera es igual a:", str(i**3))


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

va = 5
for n in range(0,va):
     print(n)


# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:


n=35
if (type(n)==int):
  if (n>0):
    factorial= n
    while(n>1):
        n=n-1
        factorial=factorial*n
    print("El factorial es igual a:", factorial)
else:
   print("Este numero no es entero y no es mayor que 0")
    


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:


num=1
while num < 6:
    print("Num con while ", num)
    num =num+1
    for i in range(6,11):
        print("Num con for",i)
 

# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

for i in range (1,6):
    print("Impreso con for:",i)
    b=6
    while b<11:
        print("Impreso con while:",b)
        b=b+1


# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:


for num in range(0,31):
    if num>1:
        cont=0    
        i=2
        while i<num and cont==0:
                
            resto=num%i
            #print("{}%{}={}".format(num,i,resto))
            if resto==0:
               cont+=1             
            i+=1
        if cont==0:
            print("El:",num,"es primo")


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:





# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:


e=100

while e<300:
   e+=1
   if e%12!=0:
      continue
   print(e,"es divisible por 12")

# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:


num=int(input("Ingrese su número:"))
cont=0
if num>1:
    for i in range(2,num):
        resto=num%i
        #print("{}%{}={}".format(num,i,resto))
        if resto==0:
            cont+=1
            break
    if cont==0:
        print("El:",num,"es primo")
    else:
        print("El:",num,"no es primo")
else:
    print(num,"no es primo")


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

tope=300
e=100
while (e < tope):
    if e % 3 == 0 and e % 6==0:
        print("Es divisible x 3 y es multiplo de 6 el numero:",e)
        break
    e+=1


