class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('멍멍')

    def move(self):
         print('움직인다ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ')
    def __str__(self):
        sentence = "이름:{}, 나이:{}".format(self.name, self.age)
        return sentence

dog1 = Dog('코코', 2)
dog2 = Dog('겨울', 4)
print(dog1)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ')

class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner

    def bark(self):
        print('멍멍')

    def move(shake):
         print('꼬리를 흔든다')

    def __str__(self):
        sentence = "이름:{}, 나이:{}, 주인:{}".format(self.name, self.age, self.owner)
        return sentence

dog1 = Dog('코코', 2, '신주영')
dog2 = Dog('겨울', 4, '루피')
print(dog1)
print(dog2)

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def lick(self):
        print('핥는다')
    def scratch(self):
        print('긁는다')
cat = Cat('고먐', 1)
cat.lick()
cat.scratch()

class Calculator:
    def __init__(self):
        self.result = 0

    def 더하기(self, num):
        self.result += num
        return self.result
    
    def 빼기(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.더하기(3))
print(cal2.더하기(3))
print(cal1.더하기(4))
print(cal2.더하기(4))
print(cal1.빼기(100))
print(cal2.빼기(100))
print(cal1.빼기(10))
print(cal2.빼기(10))




class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('냠냠')
    def drink(self):
        print('키야ㅑ')
    def walk(self):
        print('터벅터벅')
    def talk(self):
        print('%!*^!*^)$^!$^!$#^8!')
    
class Student(Human):
    def __init__(self, name, age, num):
        super().__init__(name, age)
        self.num = num
    def study(self):
        print('안해')
    def gotoschool(self):
        print('지각이다!!!')
    def __str__(self):
        sentence = "이름:{}, 나이:{}, 번호:{}".format(self.name, self.age, self.num)
        return sentence
student = Student('이백염룡', 15, 200)
student2 = Student('박홍염룡', 15, 666)
print(student)
print(student2)
