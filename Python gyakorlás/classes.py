class kcoka:
    def __init__(self, a):
      self.a=a
    def setA(self, a):
      self.a=a
    def getA(self):
      return self.a
    def getKerület(self):
      return 4*self.a 
    def getTerület(self):
      return self.a*self.a
    
class Téglalap:
  def __init__(self, a,b):
      self.a=a
      self.b=b
    def setA(self, a):
      self.a=a
    def setB(self,b)
      self.b=b
    def getAB(self,a,b)
      self.a=a
      self.b=b
    def getA(self):
      return self.a
    def getKerület(self):
      return 2*(self.a+self.b) 
    def getTerület(self):
      return self.a*self.b

class kör:
  def __init__(self, r):
      self.r=r
    def setA(self, r):
      self.r=r
    def getR(self):
      return self.r
    def getKerület(self):
      return 2*self.r*3.14
    def getTerület(self):
      return self.r**2*3.14