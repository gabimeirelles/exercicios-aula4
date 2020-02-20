def somar (a,b):
    resultado = a + b
    if resultado <40:
        return('Ops, só retorno valores acima de 40')
    else:    
        return resultado
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
soma = somar(a,b)
print(soma)         