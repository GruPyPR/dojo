def magnetico(ponto_magnetico, cursor):
    if cursor.x == cursor.y:
        return cursor
    if cursor.distancia(ponto_magnetico) <= 5:
        return ponto_magnetico
    return cursor

class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, ponto):
        dist_x = self.x - ponto.x
        dist_y = self.y - ponto.y
        return dist_x or dist_y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, ponto):
        return self.x == ponto.x and self.y == ponto.y