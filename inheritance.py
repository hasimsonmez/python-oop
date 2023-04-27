#Inheritance (Kalıtım):Miras alma

#Person=> name, lastname, age, eat(), run(), drink()
#Student(Person), Teacher(Person)

#Animal => Dog(Animal), Cat(Animal)

class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        print('Person Created')
    
    def who_am_i(self):
        print("I am a Person")
    
    def eat(self):
        print('I am eating')
    
class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber=number
        print('Student Created')
    
    #override (aynı isimdeki metodlarda,bulunduğu classın,üst classtaki metoda göre öncelik taşıması durumu)
    def who_am_i(self):
        print('I am a student')
    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f'I am a {self.branch} teacher ')

p1 = Person("Ali","Yılmaz")
s1 = Student("Fatih","Terim",1234)
t1 = Teacher("Okan","Buruk","Fizik")

print(p1.fname + ' '+ p1.lname)
print(f'{s1.fname} {s1.lname}  {s1.studentNumber}')
s1.who_am_i()
p1.who_am_i()
s1.eat()
p1.eat()
s1.sayHello()
print(f'name : {t1.fname} lastname : {t1.lname} branch : {t1.branch}')
t1.who_am_i()

