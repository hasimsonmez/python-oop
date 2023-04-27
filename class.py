class Person:
    #class attributes (sınıf nitelikleri)
    adress  = "no information"

    #constructer (yapıcı metod)
    def __init__(self,name,year):
        
        #object attributes(obje nitelikleri)
        self.name = name
        self.year = year
        print("init metodu çalıştı.")

    #instance methods
    def intro(self):
        print("Hello There. I am "+ self.name)
    def calculateAge(self):
        return 2019 - self.year
#object (instance)
p1 = Person(name="hasim",year=1998)
p2 = Person(name= "ali",year = 1995)
p1.adress = "kutahya merkez"
print(f"name: {p1.name} year: {p1.year} adress: {p1.adress}")
print(f"name: {p2.name} year: {p2.year} adress: {p2.adress}")

p1.intro()
p2.intro()
print(f'adım:{p1.name} ve yaşım :{p1.calculateAge()}')
print(f'adım:{p2.name} ve yaşım :{p2.calculateAge()}')