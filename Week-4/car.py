class car:
    def __init__(self,model,make,year_of_man,engine_capacity):
    self.model = model
    self.make = make
    self.year = year_of_man
    self.engine_capacity

    #getters

    def get_model (self):
        return self.model 
    
    def  get_make (self):
        return self.make 
    
    def get_year (self):
        return self.year_of_man

    
    def set_model(self,model):
        self.model = modelt_engine_capacity(self):
        return self.engine_capacity

   #setters
    def set_model(self,model):
        self.model = model
    
    
    def set_model(self,make):
        self.model = make

    
    

car 1 = car("demio","nissan",2018,1300)
car2 =car("hilux","toyota",2020,3500)
car3 = car("passat","vw",2009,2600)


print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car3.get_year())

print()
