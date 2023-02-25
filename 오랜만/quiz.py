print("'Python'은 프로그래밍 언어입니다")


temp1 = 32
temp2 = 32
conv1= (temp1-32)/1.8
conv2= temp2*1.8+32
print('{}, {}'.format(temp1, conv1))
print('{}, {}'.format(temp2, conv2))

y=2023

sen = 'python에서 숫자 10과 문자 "10"은 다르다.'
print(sen [5])
print(sen [-5])
print(sen [10:12])
print(sen [13:])

s = '갸라도스의 아쿠아테일!{} 효과가 별로인 듯 하다'
print(s.format('-10'))
print(s.format('-50'))
print(s.format('-297'))

age = 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1
year=2023+1-age
month=12
day=25
print('당신의 나이는 올해 {}살입니다. 당신은 {}년 {}월 {}일 00:00에 태어났습니다.'.format(age, year, month, day))

def smile(s):
    end = ':D'
    print(s+end)
smile('안녕하세요')

def dol(won):
    dollar = won * 1.3
    return dollar

print(dol(won=1011.3846153846153729836415739203))


# def eo(number):
#     if number%2==0:
#         print('짝수')
#     else:
#         print('홀수')
# number = input("숫자 입력: ")
# eo(int(number))

num1=1
num2=2
num3=3
print(num1,num2,num3)

def e(t):
    ae = 0
    ce = 0
    if t == 'Bus':
        ae += 40000
        ce += 40000/2
    elif t == 'Ship':
        ae += 30000
        ce += 30000/2
    elif t == 'Airplane':
        ae += 70000
        ce += 70000/2
    else:
        print("망나뇽의 성인 요금은 체육관 뱃지 8개, 어린이의 요금은 체육관 벳지 4개입니다.")
        return
    print('{}의 성인요금은 {}원, 어린이 요금은 {}원입니다.'.format(t,ae,ce))
t=input('사용할 교통편: ')
e(t)
