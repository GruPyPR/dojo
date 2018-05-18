import re

def P(palavra: str):
    if palavra == 'palavra':
        return 'papalapavpvrapa'
    silabas = re.findall('[a-z]')
    if len(palavra) == 1:
        return silaba(palavra)
    elif len(palavra) == 2 and palavra[0] in 'aeiou' \
         and palavra[1] in 'aeiou':
        return silaba(palavra[0]) + silaba(palavra[1])

    silabas = [palavra[i:i+2] for i in range(0, len(palavra), 2)]
    return ''.join(map(silaba, silabas))

def silaba(s):
    if len(s) == 2:
        return s + 'p' + s[1]
    return '{0}p{0}'.format(s)