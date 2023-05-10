#Cree su propia clase con animal
class Animals:
    def __init__(self, name, specie , age):
        self._name  = name 
        self.specie = specie
        self._age = age
        self.is_they_are_alive = True

    def species_and_name(self):
        print("Es una " + self.specie + " y tiene" , self._age  , "años")      
    
    def name_species_and_age(self):
        print("Su nombre es " + self._name + " y es un " + self.specie, "que ha vivido" , self._age ,"años")
    
    def get_name(self):
        return self._name 
    def set_name(self,name):
        self._name = name



animals1 = Animals("Zimba", "Leon", 12)
animals2 = Animals("kiara", "Perra", 7)

animals1.set_name("Cachimbo")
print(animals1.get_name())


print("-----------------------------------------------------------------------")
animals1.name_species_and_age()
print("-----------------------------------------------------------------------")  
animals2.species_and_name()
print("-----------------------------------------------------------------------")  

class Amo(Animals):
    def __init__(self, name, specie, age, classification):
        super().__init__(name, specie, age)
        self._classification = classification

    def species_and_name(self):
        print(" Es un " , self.specie , " y es " + self._classification  ) 
    
    def congratulations(self):
        print("Los animales son muy bonitos")

    def get_classification(self):
        return self._classification

    def set_classification(self,classification):
        self._classification = classification


bestia = Amo("Poo", "Panda", 9, "Terrestre") 

bestia.name_species_and_age()
bestia.congratulations()

bestia.set_classification("acuatico")
print(bestia.get_classification())

bestia.set_classification("acuatico")
print(bestia.get_classification())