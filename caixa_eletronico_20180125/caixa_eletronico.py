NOTAS = [100, 50, 20, 10, 5, 2]

def caixa_eletronico(valor):

    notas_possiveis = [nota for nota in NOTAS if nota <= valor]
    if notas_possiveis == []:
        return  {}    
    maior_nota = max(notas_possiveis)

    resto = valor % maior_nota
    
    essa_nota = {maior_nota: valor // maior_nota}
    if resto > 0:
        return {
            **essa_nota,
            **caixa_eletronico(resto)
        }
    return {essa_nota: valor // maior_nota}


    if valor in NOTAS:
        return {valor: 1}

    if valor % 2 == 0 and valor < 10:
        return {2: valor // 2}

    if valor % 100 == 0:
        return {100: valor // 100}
    
    if valor > 100:
        return {100: valor // 100,
                valor % 100: 1}

    if valor % 20 == 0:
        return {20: valor // 20}

    if valor == 15:
        return {10: 1, 5: 1}

    if valor == 90:
        return {50: 1, 20: 2}
