from collections import Counter

def separador(string):
    resultado = []
    co

    for letra in string:

        resultado.append(letra)

    return resultado

def lookandsay(numero):
    counter = Counter(str(numero))

    result = ''
    conta = 0
    ultimo_numero = None

    for n in str(numero):
        if ultimo_numero == n or ultimo_numero is not None:
            conta += 1
        
        elif ultimo_numero is not None: 
            result += str(conta) + ultimo_numero
            ultimo_numero = n

    return result

    counted_numbers = [str(len(item)) + item[0] for item in result]

    result_str = ''.join(counted_numbers)

    return int(result_str)

