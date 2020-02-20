def retornar_meu_nome (nome,sobrenome):
    resultado = 'Olá, seu nome é: ' + nome + ' ' + sobrenome
    return resultado

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

meu_nome = retornar_meu_nome(nome,sobrenome)
print(meu_nome)
