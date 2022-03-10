# set
# {} 중괄호 사용
# 단, 빈 중괄호는 딕셔너리
# 따라서 빈 세트를 만들 때는 s = set() 이 방식만 가능

# set의 특징
# 1. 순서가 없다.(인덱스가 없음)
# 2. 중복을 허용하지 않음.
# 3. 집합 연산에 주로 사용된다. (차집합, 교집합, 합집합 등등..)
# li1[1,2,3]
# li2[3,4,5]
# 차집합 set(li1) - set(li2)
# 교집합 set(li1) & set(li2)
# 합집합 set(li1) | set(li2)
# 순서가 없고, 중복을 허용하지 않으며, 집합 연산에 주로 사용되는 자료형!

# set 자료 추가 제거
# s = set()
# s.add(1)
# s.add(2)
# s.remove(1)
# s.remove(2)

# set와 for 문
# li=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,12,11,2,2,2,2,2,2,2,2,2]
# for i in set(li):
#     print(f"{i}의 등장횟수 {li.count(i)}")

dy = """'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight
Shoes on, get up in the morn'
Cup of milk, let's rock and roll
King Kong, kick the drum, rolling on like a Rolling Stone
Sing song when I'm walking home
Jump up to the top, LeBron
Ding dong, call me on my phone
Ice tea and a game of ping pong, huh
This is getting heavy
Can you hear the bass boom? I'm ready (woo hoo)
Life is sweet as honey
Yeah, this beat cha-ching like money, huh
Disco overload, I'm into that, I'm good to go
I'm diamond, you know I glow up
Hey, so let's go
'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight (hey)
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa oh oh
Bring a friend, join the crowd
Whoever wanna come along
Word up, talk the talk
Just move like we off the wall
Day or night, the sky's alight
So we dance to the break of dawn
Ladies and gentlemen, I got the medicine
So you should keep ya eyes on the ball, huh
This is getting heavy
Can you hear the bass boom? I'm ready (woo hoo)
Life is sweet as honey
Yeah, this beat cha-ching like money
Disco overload, I'm into that, I'm good to go
I'm diamond, you know I glow up
Let's go
'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight (hey)
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa oh oh
Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa oh oh
Dy-na-na-na, na-na, na-na, ayy
Dy-na-na-na, na-na, na-na, ayy
Dy-na-na-na, na-na, na-na, ayy
Light it up like dynamite
Dy-na-na-na, na-na, na-na, ayy
Dy-na-na-na, na-na, na-na, ayy
Dy-na-na-na, na-na, na-na, ayy
Light it up like dynamite
'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight
Shining through the city with a little funk and soul
So I'ma light it up like dynamite (this is ah)
'Cause I-I-I'm in the stars tonight
So watch me bring the fire and set the night alight (alight, oh)
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa (light it up like dynamite)
Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
Shining through the city with a little funk and soul
So I'ma light it up like dynamite, whoa oh oh"""

제거기호 = "()!,-\"?"
for i in 제거기호:
    dy = dy.replace(i, " ")
dy = dy.replace("'m", " am ")
dy = dy.replace("t's", "t us ")
dy = dy.lower()

단어=dy.split()

# key : 단어 , value : 등장횟수(빈도수)
사전={}

for i in set(단어):
    사전[i] = 단어.count(i)
print(사전)


# dictionary
# key 값 : value 값
#  단어   :   뜻
# ex)
# d = {1:"one", 2:"two","3":"three"}
# d={}
# 순서없는 자료형(인덱싱 x)
# 단 키 인덱싱 가능 > 키 값을 가지고 밸류에 접근
# d[1] > 'one'
# d['3'] > 'three'
# d[1] = 1
# d = {1:1, 2:"two","3":"three"}
# 키 인덱싱을 통해 value값 변경 가능
# d[4]="four"
# d = {1:"one", 2:"two","3":"three",4:"four"}
# 기존에 있는 키를 가지고 밸류와 매칭 : 갱신
# 기존에 없는 키를 가지고 밸류와 매칭 : 추가

# 1 in d > True

# del d[1]
# d > d = {2:"two","3":"three",4:"four"}

# d1={}
# for i in range(10):
#   di[i]=i

# key 값은 "단어", value 값은 "문자열의 길이"로 저장

# for문에 사용!
# d = {1:"one", 2:"two",3:"three"}
# for i in d:
#     print(f"key값 : {i}, value값 : {d[i]}")

# turtle.shape("설정할 모양")
# > 거북이 모양 설정
# turtle.getshapes()
# > 설정할 수 있는 모양들 반환
# turtle.color("red")
# > 커서 색깔 설정
# turtle.penup()
# > 펜을 들겠다! (이동간, 선을 그리지 않음)
# turtle.pendown()
# > 펜을 내리겠다! (이동간, 선을 그림)
# turtle.hideturtle()
# > 커서를 숨긴다.
# turtle.showturtle()
# > 커서를 드러냄.
# turtle.pensize(X)
# > 펜사이즈 설정 7이 적당
# turtle.forward(X)
# > X만큼 전진!
# turtle.left(X)
# > X만큼 왼쪽으로 돌아라!
# turtle.right(X)
# > X만큼 오른쪽으로 돌아라!
# turtle.speed(X)
# > 이동 스피드 조정(0~1) 0일수록 빠르다.

# import turtle as t
# from random import randint as ri

# # t.shape("blank")

# t.pensize(7)
# t.speed(0)
# # t.color("red")           #도형의 펜의 색상은 red 색상으로 준비한다.
# # t.left(45)                #펜의 각도를 왼쪽으로 45도 회전한다 
# # t.forward(200)         #200 만큼 전진한다
# # t.circle(73,221.37)     #반지름이 73 인 호를 221.37 만큼 그린다.   
# # t.left(180)               #펜의 각도를 왼쪽으로 180도 회전한다.
# # t.circle(73,221.37)     #반지름이 73 인 호를 221.37 만큼 그린다.
# # t.forward(200)         #200 만큼 전진한다


# # print(t.getshapes())

# # for i in t.getshapes():
# #     t.shape(i)
# #     input(i)

# t.listen() # 이벤트 발생시 처리하겠다.
# # t.onkey(F,key) (함수,키)
# def 오른쪽() :
#     t.seth(0)
#     t.fd(50)

# def 왼쪽() :
#     t.seth(180)
#     t.fd(50)

# def 위쪽() :
#     t.seth(90)
#     t.fd(50)

# def 아래쪽() :
#     t.seth(270)
#     t.fd(50)

# t.onkey(오른쪽,"Right") 
# t.onkey(왼쪽,"Left")
# t.onkey(위쪽,"Up")
# t.onkey(아래쪽,"Down")

# # t.goto(x,y) x,y로 이동
# def 원점이동():
#     t.pu()
#     t.goto(0,0)
#     t.pd()

# t.colormode(255)
# def 색():
#     t.color(ri(0,255),ri(0,255),ri(0,255))
# t.onkey(색,"c")

# t.onkey(원점이동,"space")

import turtle as t
from random import randint as ri
import dy

사전 = dy.사전

t.ht()
t.pu()
t.speed(0)
t.colormode(255)

t.setup(800,600)
for i in 사전:
    t.goto(ri(-350,300),ri(-250,200))
    t.color(ri(0,255),ri(0,255),ri(0,255))
    t.write(i,font=("맑은고딕",(사전[i]+5)*2,"bold"))


t.mainloop() # 창을 유지 항상 맨 밑
