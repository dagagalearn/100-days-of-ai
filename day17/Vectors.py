class Vectors:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __add__(self,other):
    return Vectors(self.x+other.x,self.y+other.y)
  def __abs__(self):
    return (self.x**2+self.y**2)**(0.5)
  def __repr__(self):
    return f"Vectors: Vectors({self.x,self.y})"
v1 = Vectors(3,4)
v2 = Vectors(4,5)

print(v1+v2)
print(abs(v1))
