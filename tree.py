import math

def deg2rad(deg):
    return math.pi/180*deg

def random_choice(iterable):
    return iterable[int(random(len(iterable)))]

class Node():
    def __init__(self, a, b):
        self.children = []
        self.thickness = 1
        self.a = a
        self.b = b
        
    def angle(self):
        return PVector.angleBetween(PVector(0,-1), self.b - self.a)

    def is_leaf(self):
        return len(self.children) == 0

    def update_thickness(self):
        sum_squared_thicknesses = 1
        for child in self.children:
            sum_squared_thicknesses += child.thickness**2
        self.thickness = math.sqrt(sum_squared_thicknesses)

    def branch(self):
        # New Branch
        my_shape = self.b - self.a
        if my_shape.x == 0:
            current_angle = 0
        else:
            current_angle = math.tan(my_shape.x/my_shape.y) 
        mean_regression = 0.02
        angle =  mean_regression * current_angle + (1 - mean_regression) * deg2rad(random(-10, 10))
        new_shape = my_shape.rotate(angle)
        branch = Node(self.b, self.b + new_shape)

        self.children.append(branch)

    def update(self):
        for child in self.children:
            child.update()
        # Leaves always grow
        if self.is_leaf():
            self.branch()
        # Random branching, dependent on thickness
        elif random(50) < 1/self.thickness**2:
            self.branch()
        self.update_thickness()

        
    def draw(self):
        strokeWeight(self.thickness)
        line(self.a.x, self.a.y, self.b.x, self.b.y)
        for child in self.children:
            child.draw()
        

    
