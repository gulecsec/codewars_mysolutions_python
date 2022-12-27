import numpy

class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
        
    def mix(self, other):
        self.other = other
        self.other_volume = self.other.volume
        
        self.new_volume = self.other_volume + self.volume
        
        x = self.volume/self.new_volume
        y = self.other_volume/self.new_volume
        
        self.new_color1 =  numpy.ceil(x*self.color[0] + y*self.other.color[0])
        self.new_color2 =  numpy.ceil(x*self.color[1] + y*self.other.color[1])
        self.new_color3 =  numpy.ceil(x*self.color[2] + y*self.other.color[2])
        
        
        return Potion((self.new_color1, self.new_color2, self.new_color3), self.new_volume)