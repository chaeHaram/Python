# print(type(True))

# 숫자 자료형의 경우 0은 False, 0이 아니면 True
# 문자열 자료형의 경우 ""은 False, ""이 아니면 True

# a = 10

# print(a>0)
# print(a<3)
# print(a==1)
# print(a!=2)
# print(a>=4)
# print(a<=5)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# 산술      >       비교      > 논리
#(*,/,+,-) >       비교      >(and,or)

# if 비교연산자 and 비교연산자
# if 비교연산자 or 비교연산자

# if[Bool]:
#   [종속문자]
# 파이썬에서 : 의미는 "종속문장의 시작"

# if(a==1){
#   printf();
# }

# if a==1:
#   print()

# 파이썬에서 : 는 c언어의 { }느낌
# 같은 종속문장이면 같은 라인으로 설정 탭키로 띄워주기

# if 1:
#     print(1)
#     print(2)

# if True:
#     print(1)
# if 0:
#     print(2)
# if 100:
#     print(3)
# if "hello":
#     print(4)
# a=10
# if a>0:
#     print(5)
# if a!=10:
#     print(6)
# if a>=0 and a<=5:
#     print(7)

# a = input("문자 입력 : ")

# if a:
#     print("입력이 들어왔음!")

# A = int(input("숫자 입력 : "))

# if 0 <= A < 10:
#     print(A,"한자리 수!!")

# a = int(input("입력 : "))
# if a>0:
#     print("양수입력")
# if a<0:
#     print("음수입력")
# if a==0:
#     print("0입력")

# a = int(input(첫번째 수 입력 : ))
# b = int(input(두번째 수 입력 : ))

# if a>b:
#     print(a,"가 더 크다")
# if a<b:
#     print(b,"가 더 크다")
# if a==b:
#     print("같은 수")

# a = int(input("수 입력 : "))

# if a%2==0:
#     print("짝수")
# if a%2==1:
#     print("홀수")

# a = int(input("수 입력 : "))

# if a%3==0:
#     print("3의 배수입니다.")
# if a%3==1 or a%3==2:
#     print("3의 배수가 아닙니다.")

# kor = int(input("국어 점수 입력 : "))
# math = int(input("수학 점수 입력 : "))
# avg = (kor+math)/2

# if avg>=80:
#     print("합격")
# if avg<80:
#     print("불합격")

# a = int(input("첫 번째 수 : "))
# b = int(input("두 번째 수 : "))

# if a%10+b%10>=10:
#     print("일의 자리 올림 발생!")
# if a%10+b%10<10:
#     print("일의 자리 올림 발생x")

# a = int(input("첫 번째 수 : "))
# b = int(input("두 번째 수 : "))

# if a//10 + b//10 != (a+b) //10:
#     print("일의 자리 올림 발생!")
# if a//10 + b//10 = (a+b) //10:
#     print("일의 자리 올림 발생x")

# a = int(input("첫 번째 수 : "))
# b = int(input("두 번째 수 : "))
# c = input("연산을 입력하세요 : ")

# if c == '+':
#     print(a,"와",b,"의 합은",a+b)
# if c == '-':
#     print(a,"와",b,"의 차은",a-b)
# if c == '*':
#     print(a,"와",b,"의 곱은",a*b)
# if c == '/':
#     print(a,"와",b,"의 나눗셈은",a/b)

# 1. if의 확장~
#  - elif, else가 먼저 나오면x
#  - else가 확장의 마지막~
#  - if는 무조건 elif, else선택
#     if elif(else 없이 가능)
#     if else(elif 없이 가능)

# 2. 조건의 유무!
# - else에 조건 붙이지 마세요

a = int(input("수 입력 : "))

if a>0:
    print("양수입력")
elif a<0:
    print("음수입력")
else:
    print("0입력")