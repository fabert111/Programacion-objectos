#Creen su propia clase, por ejemplo,"Persona"
class  Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
        self.is_alive = True

    def greet(self):
        print("Hola que mas, mi nombre es " + self.name  )

    def best_regard(self):
        print("Que mas, me llamo " , self.name , ", tengo " + str(self.age) + " años y soy " + self.profession)

    def xxx_ppp(self):
        print(f"Me llaman el poderoso {self.name} y tengo {self.age} y {self.profession}.")


person1 = Person("Faber", 25, "doctor")
person2 = Person("Lina", 30, "Policia")
person3 = Person("Hulx", 25 , "Hablo mucho")

print("--------------------------------------------------------")
person1.greet()
print("--------------------------------------------------------")
person2.best_regard()
print("--------------------------------------------------------")
person3.xxx_ppp()
print("---------------------------------------------------------")
print("----------------INHERITANCE-------------------------------")
#------------------------------------------------------------------
class Student(Person):
    def __init__(self, name, age, profession, school_name, grade_and_section):
        super().__init__(name, age, profession)
        self.schol_name = school_name
        self.grade_and_section = grade_and_section

    def personal_information(self):
        print(f"Que mas me llamo {self.name} y estudio enel colegio {self.schol_name} y voy en {self.grade_and_section} año .")
    
student1 = Student("Camila", 15, "estudiante", "Braulio Gonzales", "5-")             
student2 = Student("Fernando", 19, "estudiante", "San Rafael", "10-")


print("-----------------------------------------------------------")
student1.greet()
print("")
student1.best_regard()
print("-----------------------------------------------------------")
student2.greet()
print("")
student2.best_regard()
print("-----------------------------------------------------------")
student1.personal_information()
print("")
student2.personal_information()
print("-----------------------------------------------------------")








    