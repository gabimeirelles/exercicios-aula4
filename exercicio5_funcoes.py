import math as mt

def area (raio):
    area = (mt.pi*(raio)**2)
    return area

def comp (raio):
    comp = (2*((mt.pi)*raio))   
    return comp 

try:
    raio = float(input('Digite o valor do raio do círculo: '))
    area_circulo = area(raio)
    print('O círculo de raio ','%.2f' %raio,'tem área igual a ','%.2f' %area_circulo)
    comp_circulo = comp(raio) 
    print('E comprimento igual a ','%.2f' %comp_circulo)
except:
    raio = 0    
    print('Insira um valor numérico.')
 
    
