class Box:
    def __init__(self, width, length, height):
        self.Width=width
        self.Length=length
        self.Height=height

    def setWidth(self):
        self.Width=width
    
    def setLength(self):
        self.Length=length

    def setHeight(self):
        self.Height=height

    def getVolume(self):
        return self.Width*self.Length*self.Height

    def __str__(self):
        return '(%d %d %d)' %(self.Width, self.Length, self.Height)

box=Box(100,100,100)
print(box)
print("상자의 부피 : ", box.getVolume())