class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def comparacion(self, x, y):
        if self.x == x and self.y == y:
            return True
        else: 
            return False
