
import math

class Vector2:
    
    """ Vector 2D Class
        takes 2 arguments : x and y
    """
    
    def __init__(self, x = 0 , y = 0):
        self.x, self.y = x , y

    def __len__(self):
        """ Gives the length of vector
        """
        return math.hypot(self.x, self.y)
    
    def __add__(self, v):
        """ Addition of two vectors
            Operation: +
        """
        if isinstance(v,list) or isinstance(v,tuple):
            if len(v) == 2:
                return Vector2(self.x + v[0], self.y + v[1])
            else:
                raise Exception('Expected 2 values of list, gotted {}'.format(len(v)))
        elif isinstance(v,Vector2) or isinstance(v,Vector3):
            return Vector2(self.x + v.x, self.y + v.y)
        else:
            raise Exception('Expected list/tuple/Vector, gotted {}'.format(type(v)))
    
    def __sub__(self, v):
        """ Subtract of two vectors
            Operation: -
        """
        if isinstance(v,list) or isinstance(v,tuple):
            if len(v) == 2:
                return Vector2(self.x - v[0], self.y - v[1])
            else:
                raise Exception('Expected 2 sized list/tuple, gotted {}'.format(len(v)))
        elif isinstance(v,Vector2) or isinstance(v,Vector3):
            return Vector2(self.x - v.x, self.y - v.y)
        else:
            raise Exception('Expected list/tuple/Vector, gotted {}'.format(type(v)))
    
    def __mul__(self, num):
        """ Multiplication of vector by a number
            Operation: *
        """
        if isinstance(v,int) or isinstance(v,float):
            return Vector2(self.x * num, self.y * num)
        else:
            raise Exception('Expected number/float, gotted {}'.format(type(v)))
    
    def __and__(self, v):
        """ Multiplication of two vectors
            Operation: &
        """
        if isinstance(v,Vector2) or isinstance(v,Vector3):
            return Vector2(self.x * v.x, self.y * v.y)
        else:
            raise Exception('Expected Vector, gotted {}'.format(type(v)))
    
    def __iadd__(self, v):
        """ Addition of two vectors
            Operation: +=
        """

        if isinstance(v,list) or isinstance(v,tuple):
            if len(v) == 2:
                self.x += v[0]
                self.y += v[1]
            else:
                raise Exception('Expected 2 values of list, gotted {}'.format(len(v)))
        elif isinstance(v,Vector2) or isinstance(v,Vector3):
            self.x += v.x
            self.y += v.y
        else:
            raise Exception('Expected list/tuple/Vector, gotted {}'.format(type(v)))
        
        return self
    
    def __isub__(self, v):
        """ Subtract of two vectors
            Operation: -=
        """
        
        if isinstance(v,list) or isinstance(v,tuple):
            if len(v) == 2:
                self.x -= v[0]
                self.y -= v[1]
            else:
                raise Exception('Expected 2 values of list, gotted {}'.format(len(v)))
        elif isinstance(v,Vector2) or isinstance(v,Vector3):
            self.x -= v.x
            self.y -= v.y
        else:
            raise Exception('Expected list/tuple/Vector, gotted {}'.format(type(v)))
        
        return self
    
    def __imul__(self, num):
        """ Multiplication of vector by a number
            Operation: *=
        """
        
        if isinstance(v,int) or isinstance(v,float):
            self.x *= num
            self.y *= num
        else:
            raise Exception('Expected number/float, gotted {}'.format(type(v)))
        
        return self
    
    def __iand__(self, v):
        """ Multiplication of two vectors
            Operation: &=
        """
        if isinstance(v,Vector2) or isinstance(v,Vector3):
            self.x *= v.x
            self.y *= v.y
        else:
            raise Exception('Expected Vector, gotted {}'.format(type(v)))
        
        return self
    
    def __eq__(self, v):
        """ Comparing of two vectos for true
            Operation: ==
        """
        if isinstance(v,Vector2):
            return self.x == v.x and self.y == v.y
        else:
            raise Exception('Expected Vector2, gotted {}'.format(type(v)))
    
    def __ne__(self, v):
        """ Comparing of two vectos for false
            Operation: ==
        """
        if isinstance(v,Vector2):
            return self.x != v.x and self.y != v.y
        else:
            raise Exception('Expected Vector2, gotted {}'.format(type(v)))
    
    
    def __abs__(self, v):
        """ Gives the length of vector
        """ 
        return math.hypot(self.x, self.y)
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


class Vector3:
    
    """ Vector 3D Class
        takes 3 arguments : x,z and z
    """
    
    def __init__(self, x = 0,y = 0,z = 0):
        self.x, self.y, self.z = x,y,z

    def __len__(self):
        """ Gives the magnitude of vector
        """
        return math.sqr(self.x*selfx + self.y*self.y + self.z*self.z)

    def __add__(self, v):
        """ Addition of two vectors
            Operation: +
        """
        if isinstance(v,list) or isinstance(v,tuple):
            if len(v) == 3:
                return Vector3(self.x + v[0], self.y + v[1], self.z + v[2])
            else:
                raise Exception('Expected 3 values of list, gotted {}'.format(len(v)))
        elif isinstance(v,Vector2):
            return Vector3(self.x + v.x, self.y + v.y, self.z)
        elif isinstance(v,Vector3):
            return Vector3(self.x + v.x, self.y + v.y, self.z + v.z)
        else:
            raise Exception('Expected list/tuple/Vector, gotted {}'.format(type(v)))
    
    def __sub__(self, v):
        """ Subtract of two vectors
            Operation: -
        """
        if isinstance(v,list) or isinstance(v,tuple):
            if len(v) == 3:
                return Vector3(self.x - v[0], self.y - v[1], self.z - v[2])
            else:
                raise Exception('Expected 3 sized list/tuple, gotted {}'.format(len(v)))
        elif isinstance(v,Vector2):
            return Vector3(self.x - v.x, self.y - v.y, self.z)
        elif isinstance(v,Vector3):
            return Vector3(self.x - v.x, self.y - v.y, self.z - v.z)
        else:
            raise Exception('Expected list/tuple/Vector, gotted {}'.format(type(v)))
    
    def __mul__(self, num):
        """ Multiplication of vector by a number or dot product of vectors
            Operation: *
        """
        if isinstance(v,int) or isinstance(v,float):
            return Vector3(self.x * num, self.y * num, self.z * num)
        elif isinstance(v,Vector3):
            return self.x * v.x + self.y * v.y + self.z * v.z
        else:
            raise Exception('Expected number/float/vector3, gotted {}'.format(type(v)))
    
    def __and__(self, v):
        """ Multiplication of two vectors
            Operation: &
        """
        if isinstance(v,Vector2):
            return Vector3(self.x * v.x, self.y * v.y, 0)
        elif isinstance(v,Vector3):
            return Vector3(self.x * v.x, self.y * v.y, self.z * v.z)
        else:
            raise Exception('Expected Vector, gotted {}'.format(type(v)))
    
    def __iadd__(self, v):
        """ Addition of two vectors
            Operation: +=
        """

        if isinstance(v,list) or isinstance(v,tuple):
            if len(v) == 3:
                self.x += v[0]
                self.y += v[1]
                self.z += v[2]
            else:
                raise Exception('Expected 3 values of list, gotted {}'.format(len(v)))
        elif isinstance(v,Vector2):
            self.x += v.x
            self.y += v.y
        elif isinstance(v,Vector3):
            self.x += v.x
            self.y += v.y
            self.z += v.z
        else:
            raise Exception('Expected list/tuple/Vector, gotted {}'.format(type(v)))
        
        return self
    
    def __isub__(self, v):
        """ Subtract of two vectors
            Operation: -=
        """
        
        if isinstance(v,list) or isinstance(v,tuple):
            if len(v) == 3:
                self.x -= v[0]
                self.y -= v[1]
                self.z -= v[2]
            else:
                raise Exception('Expected 3 values of list, gotted {}'.format(len(v)))
        elif isinstance(v,Vector2):
            self.x -= v.x
            self.y -= v.y
        elif isinstance(v,Vector3):
            self.x -= v.x
            self.y -= v.y
            self.z -= v.z
        else:
            raise Exception('Expected list/tuple/Vector, gotted {}'.format(type(v)))
        
        return self
    
    def __imul__(self, num):
        """ Multiplication of vector by a number
            Operation: *=
        """
        
        if isinstance(v,int) or isinstance(v,float):
            self.x *= num
            self.y *= num
            self.z *= num
        else:
            raise Exception('Expected number/float, gotted {}'.format(type(v)))
        
        return self
    
    def __iand__(self, v):
        """ Multiplication of two vectors
            Operation: &=
        """
        if isinstance(v,Vector2):
            self.x *= v.x
            self.y *= v.y
            self.z = 0
        elif isinstance(v,Vector3):
            self.x *= v.x
            self.y *= v.y
            self.z *= v.z
        else:
            raise Exception('Expected Vector, gotted {}'.format(type(v)))
        
        return self
    
    def __eq__(self, v):
        """ Comparing of two vectos for true
            Operation: ==
        """
        if isinstance(v,Vector3):
            return self.x == v.x and self.y == v.y and self.z == v.z
        else:
            raise Exception('Expected Vector3, gotted {}'.format(type(v)))
    
    def __ne__(self, v):
        """ Comparing of two vectos for false
            Operation: ==
        """
        if isinstance(v,Vector3):
            return self.x != v.x and self.y != v.y and self.z != v.z
        else:
            raise Exception('Expected Vector3, gotted {}'.format(type(v)))
    
    
    def __abs__(self, v):
        """ Gives the magnitude of vector
        """ 
        return math.sqr(self.x*selfx + self.y*self.y + self.z*self.z)
    
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    
    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y,self.z)

    def normalize(self):
        """
             Normalize vector
        """
        inv_length = 1 / len(self)
        self.x *= inv_length;
	self.y *= inv_length;
	self.z *= inv_length;
	return self

    def cross(self, v):
        """
            Cross product of vector
        """
        if isinstance(v,Vector3):
            return Vector3(self.y * v.z - self.z * v.y, self.z * v.x - self.x * v.z, self.x * v.y - self.y * v.z)
        else:
            raise Exception('Expected Vector3, gotted {}'.format(type(v)))

    def distance(self, v):
        """
            Distance between two points
        """
        if isinstance(v,Vector3):
            dx = self.x - v.x
            dy = self.y - v.y
            dz = self.z - v.z
            return math.sqr(dx*dx+dy*dy+dz*dz)
        else:
            raise Exception('Expected Vector3, gotted {}'.format(type(v)))
    
