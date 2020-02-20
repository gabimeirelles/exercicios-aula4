import math as mt

def area (raio):
    area = (mt.pi*(raio)**2)
    return area

def comp (raio):
    comp = (2*((mt.pi)*raio))   
    return comp 

raio = float(input('Digite o raio do círculo: '))

if (raio == str):
    print('Insira um valor numérico.')
 
area_circulo = area(raio)
comp_circulo = comp(raio)     

print('O círculo de raio ','%.2f' %raio,'tem área igual a ','%.2f' %area_circulo,'e comprimento igual a ','%.2f' %comp_circulo)