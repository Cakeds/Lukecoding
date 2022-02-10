# list = [1 ,2 ,3]
# print(list)
# list1 = ['안녕', '친구들']
# print(list1[1])
# list = [1, 1, 1]
# a = len(list)
# print(a)
# rb = ['r', 'o', 'y', 'g', 'b', 'n', 'p']
# lastC = rb[6]
# print('무지개의 마지막 색은 {}이다.'.format(lastC))
# an = ['d', 'c', 'bi',  'e', 'b']
# pl = ['st', 'swt', 'ro', 'cb']
# cr = an + pl
# print(cr)
# print(cr*3)
# a = [1, 1, 1]
# a.append(3)
# print(a)
# a = [1, 2, 3]
# a[1] = 10
# print(a)
# an = ['d', 'c', 'bi',  'e', 'b']
# an.append('h')
# print(an)
# an = ['d', 'c', 'bi',  'e', 'b']
# an.insert(3, 'p')
# print(an)
# an = ['d', 'c', 'bi',  'e', 'b']
# del an[1]
# print(an)

# an = ['d', 'c', 'bi',  'e', 'b']
# an.remove('c')
# print(an)
# a = []
# print(a)
# m = ['ava', 'ave', 'ave', 't', 'Lee', 'f']
# print(m)
# m.append('f2')
# print(m)
# m.insert (4, 'ta')
# print(m)
# del m[1]
# print(m)
# m.remove ('ave')
# print(m)
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ['Python', 'Go', 'C#']
# langs = lang1 + lang2
# print(langs)
# a = ()
# print(a)
# f = ('t', 'h', 'p', 'k')
# print(f)
# rb = ('r', 'o', 'y', 'g', 'b', 'n', 'p')
# firstC = rb[0]
# print('무지개의 첫번째 색은 {}이다.'.format(firstC))
# lastC = rb[6]
# print('무지개의 마지막 색은 {}이다.'.format(lastC))
# t = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(t * 10)
# tt = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# ttt = t * 10
# print(ttt)
# print(len(ttt))
# t = [1, 2, 3]
# t[0] = 'a'
# print(t)
# while True:
#     data = input("1, 2, 3을 입력해주세요. ")
#     data = int(data)
#     a = ('주먹', '가위', '보')
#     if data < 1:
#         break
#     print( a[data-1] )
#  
# r = a[0]
# s = a[1]
# p = a[2]
# if data == 1:
#     print(r)
# elif data == 2:
#     print(s)
# elif data == 3:
#     print(p)
# f = []
# while True:
#     food = input("좋아하는 음식은 무엇입니까? ")
#     f.append(food)
#     if food == "끝":
#         break
#     print(f)
testS = ('A', 'B', 'C', 'D', 'E')
score = int(input("점수: "))
if score >= 81:
    print(testS[0])
elif score >= 61 and score <= 80:
    print(testS[1])
elif score >= 41 and score <= 60:
    print(testS[2])
elif score >= 21 and score <= 40:
    print(testS[3])
elif score >= 0 and score <= 20:
    print(testS[4])
