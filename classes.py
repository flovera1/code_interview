class Pet(object):
    num_pets =  0
    def __init__(self, name):
        self.name = name
        '''
        There's the difference between class and instance- attributes. if I put self.num_pets the value that I'll change is just the one from the object
        not the one from the class. This is fixed by chanching the variable self by the 
        name of the class.
        '''
        Pet.num_pets += 1
        
    def speak(self):
        print("My name is %s and the number of pets is %d" % (self.name, self.num_pets))
        

rover = Pet("rover")
spot = Pet("spot")
rover.speak()
spot.speak()
