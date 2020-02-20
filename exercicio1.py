import datetime as dt 

def dias_vida (data_hoje,data_nasc):
    dias_vida = data_hoje - data_nasc
    return dias_vida

dia_hoje = int(input('Digite o dia atual: '))
mes_hoje = int(input('Digite o mês atual: '))  
ano_hoje = int(input('Digite o ano atual: '))
dia_nasc = int(input('Digite o dia do seu nascimento: ')) 
mes_nasc = int(input('Digite o mês do seu nascimento: ')) 
ano_nasc = int(input('Digite o ano do seu nascimento: ')) 

dias_de_vida = dias_vida(dt.date(year=ano_hoje,month=mes_hoje,day=dia_hoje),
dt.date(year=ano_nasc,month=mes_nasc,day=dia_nasc))
print ('Você tem ',dias_de_vida, 'dias de vida.')
