class Robot:
    """ Robot qui sait avancer d'une case et pivoter à droite de 90°.
        Il est repéré par son abscisse x, son ordonnée y et sa direction.
    """
    def _nomDirection(idDirection):
        return 'nord est sud ouest'.split()[idDirection]

    def _idDirection(nomDirection):
        return ' nord est sud ouest'.split().index(nomDirection)

    def __init__(self, x, y, direction):
        """ Initialiser le robot self à partir de sa position (x, y) et sa direction. """
        self.x = x
        self.y = y
        self.direction = Robot._idDirection(direction)

    def avancer(self):
        """ Avancer d'une case dans la direction. """
        # mettre à jour self.x
        if self.direction == 1: # est
            self.x += 1
        elif self.direction == 3: # ouest
            self.x -= 1
        # mettre à jour self.y
        if self.direction == 0: # nord
            self.y += 1
        elif self.direction == 2: # sud
            self.y -= 1

    def pivoter(self):
        """ Pivoter ce robot de 90° vers la droite. """
        self.direction = (self.direction + 1) % 4


    def __repr__(self):
        return f'Robot(x={self.x} y={self.y} direction={Robot._nomDirection(self.direction)})'

# Exemple et test
if __name__ == '__main__':
    r1=Robot(4,10,'est')
    print("r1=",r1)
    r2 = Robot(15, 7, 'sud')
    print("r2=",r2)
    r1.pivoter()
    print("pivoter r1 =",r1)
    r2.avancer()
    print("avancer r2 =",r2)
    #Utilisation comme fonction dans un namespace ... 
    Robot.pivoter(r2)
    print(r2)
    

