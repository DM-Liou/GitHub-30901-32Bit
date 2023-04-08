import os
class Human:
    def __init__(self, h=0, w=0):
        self.height = h
        self.weight = w
       
    def BMI(self):
        return self.weight / ((self.height/100)**2)
   
     
class Woman(Human):
    def __init__(self, h, w, bust=0, waist=0, hip=0):
        super().__init__(h, w)
        self.bust = bust
        self.waist = waist
        self.hip = hip

    def printBWH(self):
        print("bust={},waist={},hip={}".format(self.bust, self.waist, self.hip))



#=======================================
import AI
AI.cls_ai()
#-----------
if __name__ == '__main__':

#a = myclass.Woman(165, 54, 83, 64, 84)    
    a = Woman(165, 54, 83, 64, 84)
    print(a.BMI())
    a.printBWH()
#==========================================
