# 입력받은 수의 자릿수 구하기
# n = int(input("입력 : "))
# st=''

# for i in range(1,n+1):
#     st+=str(i)
# print(len(st))

# n이 짝수인지 홀수인지 판별하는 코드
# n = int(input("입력 : "))

# su1 = 0
# su2 = 0

# for i in range(1,n+1):
#     if i%2==0:
#         su1+=i
#     else:
#         su2+=i
# print("홀수의 합 : ",su2,"짝수의 합 : ",su1)

# 1부터 n까지 리스트에 추가하는 프로그램

# n = int(input("입력 : "))

# li = []

# for i in range(1,n+1):
#     li.append(i)
# print(li)

# 1부터 n까지 홀수만 리스트에 추가하는 프로그램
# n = int(input("입력 : "))

# li = []

# for i in range(1,n+1):
#     if i%2==1:
#         li.append(i)
# print(li)

# 수를 입력받고 1~n에서 3의 배수 출력하는 프로그램
# n = int(input("입력 : "))
# su = 0
# li=[]
# for i in range(1,n+1):
#     if i%3==0:
#         su+=i
#         li.append(i)
# print("3의 배수 : ",li,"3의 배수의 개수 : ",len(li),"3의 배수의 합 : ",su)

# 개수의 다른 방법
# su1 = 0 개수
# su2 = 0 합
# for i in range(1,n+1):
#     if i%3==0:
#         su1+=1
#         su2+=i
#         li.append(i)
# print("3의 배수 : ",li,"3의 배수의 개수 : ",su1,"3의 배수의 합 : ",su2)

# a-b-c-d가 번갈아가면서 청소를 하기로했다.
# 만약 첫날 a가 당번이라면 오늘부터 n일까지 당번을 출력해라.
# n = int(input("입력 : "))
# li=[]

# for i in range(1,n+1):
#     if i%4==1:
#         li.insert(i,'a')
#     elif i%4==2:
#         li.insert(i,'b')
#     elif i%4==3:
#         li.insert(i,'c')
#     else:
#         li.insert(i,'d')
# print(li)

# 2021년에서 2100년 사이에 윤년 출력하기
# for i in range(2021,2101):
#     if i %400==0:
#         print(i)
#     elif i%100==0:
#         pass # 종속문장이라 비울 수는 없지만 아무것도 필요없을 때 사용
#     elif i%4==0:
#         print(i)

# 4개의 수를 입력받고, 짝수 홀수 판별하는 프로그램

# for i in range(4):
#     n = int(input("수 입력 : "))
#     if n%2==0:
#         print(n,"는 짝수")
#     else:
#         print(n,"는 홀수")

# 리스트 이용하여 수 저장 후 판별하는 프로그램
# li=[]
# for i in range(4):
#     n = int(input("수 입력 : "))
#     li.append(n)
# for i in li:
#     if i%2==0:
#         print(i,"짝수")
#     else:
#         print(i,"홀수")

# 수 입력 받고 받아올림 유무 판별 프로그램
# for i in range(5):
#     n1 = int(input("수 입력 : "))
#     n2 = int(input("수 입력 : "))
#     if n1%10 + n2%10 >=10:
#         print("받아올림 발생")
#     else:
#         print("받아올림 발생하지 않음")

# 5개의 점수를 입력 받고 평귬보다 낮은 수들을 구하는 프로그램
# li = []
# su = 0
# for i in range(5):
#     n = int(input("수 입력 : "))
#     li.append(n)

# avg= sum(li)/len(li)
# print("평균은",avg)

# print("5과목의 평균은",avg)
# for i in li:
#     if i<=avg:
#         print(i,"는 평균이하")

# 1에서 n까지의 3의 배수의 합
# n = int(input("수 입력 : "))
# su=0
# for i in range(1,n+1):
#     if i%3==0:
#         su+=i
# print(su)

# 1에서 100까지 3의배수 - 5의 배수의 개수는?
# su1=0
# su2=0
# for i in range(1,101):
#     if i%3==0:
#         su1+=1
#     elif i%5==0:
#         su2+=1
# print("3의배수 - 5의배수 = ",su1-su2)

