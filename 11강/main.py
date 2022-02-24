# from 수학 import 더하기
# print(더하기(3,4))
# from 수학 import 더하기, 빼기
# print(더하기(3,4))
# print(빼기(4,2))
# from 수학 import *
# print(더하기(3,4))
# print(빼기(4,2))
# print(곱하기(3,4))
# print(나누기(3,4))
# print(파이)
# import keyword
# print(keyword. kwlist)
# print(keyword. iskeyword('hi'))
# print(keyword. iskeyword('if'))

# import random
# for i in range(6):
#     number = random.randint(1, 45)
#     print(number, end=' \n')

# import time
# print('현재시각: ', time.time())

# def manyloop(max):
#     t1 = time.time()
#     for a in range(max):
#         pass
#     t2 = time.time()
#     print(t2-t1, '초 경과')

# number = int(input('숫자를 입력하세요: '))
# manyloop(number)
class Dog:
    name = "토리"
    age = 2

    def bark(self):
        print('퉤퉤!')
    
    def move(self):
        print('(움직임)')

dog1 = Dog()
dog2 = Dog()
dog1.bark()
dog2.bark()
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)


class Dog:
    def __init__(self, name, age):
        self.name = "토리"
        self.age = 2

    def bark(self):
        print('퉤퉤!')
    
    def move(self):
        print('(움직임)')

dog1 = Dog('토리', 2)
dog2 = Dog('겨울', 0.5)
dog1.bark()
dog2.bark()
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('퉤퉤!')
    
    def move(self):
        print('(움직임)')

dog1 = Dog('토리', 5)
dog2 = Dog('겨울', 0.5)
dog1.bark()
dog2.bark()
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
