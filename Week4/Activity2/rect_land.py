class RectLand():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_dimensions(self, length, width):
        self.__init__(length, width)

    def calc_area(self):
        return self.length * self.width
    
    def calc_perimeter(self):
        return 2 * (self.length + self.width)
