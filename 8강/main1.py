import random
com = random.randint(0, 100)
# while com < 100000000000000:
    # com = random.randint(0, 1000000000000000000000000000000000000000)
    # print(com)
n = 0
while True:
    print("0 부터 100 까지 숫자중 하나 골라보세요")
    n = n + 1
    print("{}번째 도전!".format(n))
    user = input("당신의 선택은!?!?!: ")
    user = int(user)
    if int(user) == com:
        print("ㅊㅊ! 드디어 맞추셨군요!")
        break
    elif user > 100:
        break
    elif user < 0:
        print(com)
        break
    elif int(user) > com:
        print("입력값이 더 큽니다")
    elif user < com:
        print("컴퓨터의 입력값이 더 큽니다")
    if n == 11:
        print("당신은 떨어졌습니다 ㅂㅂ")
        break
