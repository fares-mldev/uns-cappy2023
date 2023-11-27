class punto2d:
    
    # class defaults
    dims=2
    x=None
    y=None
    
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.validate(x,y)
        self.x = x
        self.y = y
        
    def validate(self,x,y):
        assert isinstance(x, float) or isinstance(x, int) 
        assert isinstance(y, float) or isinstance(y, int)
    
    def __str__(self):
        '''
        Convert to string
        '''
        return f'punto2d({self.x},{self.y})'
    
    def __repr__(self):
        '''
        Alternative representation
        '''
        return f'punto2d({self.x:0.2f},{self.y:0.2f},{self.magnitude():0.2f})'

    def __add__(self, o):
        '''
        Add points
        '''
        return punto2d(self.x + o.x,self.y + o.y)
    
    def __sub__(self, o):
        '''
        Substract points
        '''
        return punto2d(self.x - o.x,self.y - o.y)

    def __lt__(self, o):
        '''
        Substract points
        '''
        return self.magnitude() < o.magnitude()

    def __gt__(self, o):
        '''
        Substract points
        '''
        return self.magnitude() > o.magnitude()

    def __eq__(self, o):
        '''
        Substract points
        '''
        return self.magnitude() == o.magnitude()
    
    def magnitude(self):
        '''
        Get point magnitude
        '''
        return ( self.x**2 + self.y**2 ) ** 0.5

p1 = punto2d(1,2)
p2 = punto2d(3,-1)
print(p1,p2)
print(p1.magnitude(),p2.magnitude())

import random

l = [punto2d(random.randint(-10,10),random.randint(-10,10)) for i in range(20)]

print(sorted(l))

#funcion lambda
# toma como parametro p y le extrae el valor y
l.sort(key = lambda p:p.y)
print(l)

print(p1.dims)