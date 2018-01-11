class JogadaInvalidaError(Exception):
    pass


def jokenpo(jogada1, jogada2):
    jogada1 = str(jogada1).lower()
    jogada2 = str(jogada2).lower()
    
    validos = ['tesoura','pedra', 'papel']

    if not all([
        jogada1, jogada2,
        jogada1 in validos,
        jogada2 in validos
    ]):
        raise JogadaInvalidaError

    if jogada1 == jogada2:
        return 'EMPATE'

    if jogada1 == 'tesoura' and jogada2 == 'pedra':
        return 'PEDRA'

    if jogada1 == 'tesoura':
        return 'TESOURA'

    if jogada1 == 'papel' and jogada2 == 'tesoura':
        return 'TESOURA'

    if jogada2 == 'tesoura':
        return 'PEDRA'

    if jogada2 == 'papel':
        return 'PAPEL'

    if jogada1 == 'papel':
        return 'PAPEL'