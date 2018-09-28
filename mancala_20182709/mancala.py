def mancala(estado, posição):
    atual = estado[posição[0]][posição[1]]-estado[posição[0]][posição[1]]
    
    if posição == (1, 0):
        return [
            estado[0],
            [atual, estado[1][1]+1, estado[1][2]+1, estado[1][3]+1, estado[1][4]+1, estado[1][5]]
        ]
    if posição == (1,1):
        return [
            estado[0],
            [estado[1][0], estado[1][1]-estado[1][1], estado[1][2]+1, estado[1][3]+1, estado[1][4]+1, estado[1][5]+1]
        ]
    if posição == (1, 2):
        return [
            [estado[0][0], estado[0][1], estado[0][2], estado[0][3], estado[0][4], estado[0][5] + 1],
            [estado[1][0], estado[1][1], atual, estado[1][3]+1, estado[1][4]+1, estado[1][5]+1],
        ]

    if posição == (1, 3):
        return [
            [estado[0][0], estado[0][1], estado[0][2], estado[0][3], estado[0][4]+1, estado[0][5] + 1],
            [estado[1][0], estado[1][1], estado[1][2], atual, estado[1][4]+1, estado[1][5]+1]
        ]
