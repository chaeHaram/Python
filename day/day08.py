# n의 약수를 구하는 프로그램
# n1 = int(input("수 입력 : "))
# n2 = int(input("수 입력 : "))
# li=[]
# if n1>n2:
#     b=n2
# else:
#     b=n1
# for i in range(1,b+1):
#     if n1%i==0 and  n2%i==0:
#         li.append(i)
# print(li)

# for에도 else가 있다.
# for i in range(1,11):
#     print(i)
#     break #비정상적인 종료
# else:
#     print("정상적으로 종료")

# n = int(input("수 입력 : "))
# su=0
# for i in range(1,n+1):
#     if n%i==0:
#         su+=1
# if su==2:
#     print(n,"은 소수")
# else:
#     print(n,"은 소수가 아닙니다")

# 수를 입력받고 완전수인지를 판별하라
# n = int(input("수 입력 : "))
# su = 0
# for i in range(1,n):
#     if n%i==0:
#         su+=i
#         #li.append(i)

# #if sum(li)==n
# if su==n:
#     print(n,"은 완전수")
# else:
#     print(n,"은 완전수가 아니다")

# 두 수를 입력받고, 두 수 사이의 수들의 합을 구하세요.
# n1 = int(input("수 입력 : "))
# n2 = int(input("수 입력 : "))
# su = 0
# if n1>n2:
#     for i in range(n2+1,n1):
#         su+=i
# elif n2>n1:
#     for i in range(n1+1,n2):
#         su+=i
# else:
#     print("두 수는 같은수라 사이의 합은 존재하지 않습니다.")
# print(su)

# 한 반 학생들의 혈액형입니다. A,B,AB,O형이 각각 몇명인지 구하시오.
# a=0
# b=0
# ab=0
# o=0

# for i in ['O', 'O', 'O', 'O', 'AB', 'B', 'A', 'A', 'O', 'AB', 'B', 'A', 'B', 'AB', 'AB', 'AB', 'O', 'A', 'A', 'AB', 'B', 'AB', 'O', 'B', 'A', 'O', 'A', 'O', 'AB', 'O', 'AB', 'AB', 'O', 'B', 'B', 'O', 'O', 'AB', 'B', 'A']:
#     if i=='A':
#         a+=1
#     elif i=='B':
#         b+=1
#     elif i=='AB':
#         ab+=1
#     elif i=='O':
#         o+=1
# print("A형의 수 : ",a,"B형의 수 : ",b,"AB형의 수 : ",ab,"O형의 수 : ",o)

# 현재 당신은 5000 원이 있습니다. 편의점에 있는 물품들의 가격들이 다음과 같습니다. 구매가능한 물품의 개수를 구하세요.
# money=5000
# cnt=0
# for i in [6600, 4800, 3400, 3200, 4500, 5500, 3200, 7800, 4200, 5300, 7500, 4200, 7200, 5600, 6700, 8000, 7000, 6700, 6200, 6100, 4700, 7200, 7100, 5700, 5900, 4300, 5200, 5600, 5900, 6600, 4900, 5800, 7100, 5800, 4500, 3200, 7800, 5300, 7200, 8000]:
#     if money>=i:
#         cnt+=1
#     else:
#         pass
# print("살 수 있는 물품의 개수는 : ",cnt)

# 한 반 학생들의 국어 점수이다. 80점 미만은 보충수업을 받아야한다고 했을 때, 보충수업 대상자는 몇명일까?
# cnt=0
# for i in [80, 70, 44, 66, 40, 80, 77, 57, 68, 90, 75, 84, 99, 52, 45, 53, 54, 96, 59, 47, 57, 68, 74, 68, 79, 60, 63, 67, 43, 100, 43, 54, 77, 59, 75, 60, 97, 47, 100, 54]:
#     if i<80:
#         cnt+=1
#     else:
#         pass
# print("보충 수업 대상자는 : ",cnt)

# 단을 입력받고 구구단을 출력하는 프로그램을 작성
# n = int(input("단 입력 : "))

# for i in range(1,10):
#     print(n,"x",i,"=",n*i)

# 입력횟수를 입력받고, 그 수 만큼 두 수의 사칙연산을 계산해주는 프로그램을 작성
# n = int(input("입력할 횟수  : "))

# for i in range(1,n+1):
#     print("=====",i,"회 입력=====")
#     j=int(input("수 입력 : "))
#     k=int(input("수 입력 : "))
#     l=int(input("연산자(+ : 0, - : 1) : "))
#     if l==0:
#         print("연산 결과는 ",j+k,"입니다.")
#     elif l==1:
#         print("연산 결과는 ",j-k,"입니다.")
#     print("="*30)

# for i in [1,2,3]:
#     for j in [4,5,6]:
#         print(i,j)
#     print("a")

for i in range(2,10):
    print(i,"단 출력")
    for j in range(1,10):
        print(i,"x",j,"=",i*j)
    print("\n")
