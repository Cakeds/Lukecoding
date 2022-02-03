import random
com = random.randint(0, 100)
com1 = random.randint(0, 100)
a = random.random()
# while a < 0.9999999999:
#     a = random.random()
#     print(a)
n = 1
while True:
    print("이믜의 두 수짜가 주워집니다. 더학이, 빽이 갑슬 궇앗에요.")
    print("숫자 1:  {}, 숫자 2:   {}".format(com, com1))
    a = input("두 수의 더하기 값은? ({} 번째 도전)".format(n))
    print (a)
    a = int(a)
    n = n + 1
    if a == com + com1:
        print("딩동댕~\n(???:전국~~~노래자랑~~!!!)")
        break
    elif a < 0:
        print(com + com1)
        break
    elif a > 200:
        print(com + com1)
        break
    elif a > com + com1:
        print("값이 더 크군 ㅋ")
    elif a < com + com1:
        print("값이 더 작군 ㅋ")
while True:
    print("이믜의 두 수짜가 주워집니다. 더학이, 빽이 갑슬 궇앗에요.")
    print("숫자 1:  {}, 숫자 2:   {}".format(com, com1))
    a = input("두 수의 빼기 값은? ({} 번째 도전)".format(n))
    print (a)
    a = int(a)
    n = n + 1
    if a == com - com1:
        print("딩동댕~\n(???:전국~~~노래자랑~~!!!)")
        break
    elif a < -100:
        print(com - com1)
        break
    elif a > 100:
        print(com - com1)
        break
    elif a > com - com1:
        print("값이 더 크군 ㅋ")
    elif a < com - com1:
        print("값이 더 작군 ㅋ")
