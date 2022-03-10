# li = []
# tu = ()

# print(type(li))
# print(type(tu))
# li = [True, "hello", 1.2, 1, 'world']

# 리스트는 수정 가능
# 튜플은 수정 불가능

# li = [1.2,"hello",False,3,'world',3,3,3]

# # 요소(자료)추가 맨 뒤에
# li.append(5)
# print(li)

# # 요소추가 자리 지정
# li.insert(0,1-2j) # (인덱스 자리, 값)
# print(li)

# # 요소삭제
# B = li.pop() # default 값은 맨 뒤
# print(B,"가 삭제됨")
# print(li)

# # 요소 개수 반환
# c = li.count(3) # 3의 개수 추출
# print(c)

# # 요소 정렬
# li = [4,1,2,3,7,56,8,2,4,2,5,4,6]
# li.sort()
# print(li)

# # 요소 뒤집기
# li = [4,1,2,3,7,56,8,2,4,2,5,4,6]
# li.reverse()
# print(li)

# # 깊은 복사
# li = [1,2,3,4]
# a= li.copy
# a[0]="one"
# print(li,a)

# # 얕은 복사
# li = [1,2,3,4]
# a= li
# a[0]="one"
# print(li,a)

# # 초기화
# li.clear()
# print(li)

# sum(li) 집합 자료형의 모든 요소들의 합
# len(li) 집합 자료형의 요소의 개수

# li = [80,75,60,90]
# avg = sum(li)/len(li)
# print(avg)

# for [반복분에서 사용될 변수] in [ iterable 자료형]:
#     [종속문장]

# for i in [1,2,3,4,5,6,7,8,9]:
#     print(i)

# li = [True, 1, 1.2, "hello", 1-2j, 'world']

# for i in li:
#     print(i)

# range([start:0,stop,step:1])
# range(20) stop
# range(3,10) start, stop
# range(3,10,1) start, stop, step

# range(40)
# range(10,100)
# range(100,999)

# n1 = int(input("수 입력 : "))
# n2 = int(input("수 입력 : "))

# if n1<n2:
#     for i in range(n1+1,n2):
#         print(i)
# elif n1>n2:
#     for i in range(n1-1,n2,-1):
#         print(i)
# else:
#     print("두 수는 같은 수 입니다.")

# li = 'ab'
# a=2
# a+=3
# a-=4
# a*=2
# a/=5
# a//=3
# a**=4
# li+='c'
# li*=4

# n = int(input("수 입력 : "))
# su = 0

# for i in range(1,n+1):
#     su += i
# print(su)

# n = int(input("수 입력 : "))
# su = 1
# for i in range(1,n+1):
#     su*=i
# print(su)

# 1에서 100까지 짝수 출력
# for i in range(1,101):
#     if i%2==0:
#         print(i)

# 1에서 1000까지 3의 배수 출력
# for i in range(1,1001):
#     if i%3==0:
#         print(i)

# 1에서 300까지 7의 배수의 합
# su = 0
# for i in range(1,301):
#     if i%7==0:
#         su+=i
# print(su)

# n을 입력받고, 1에서 n까지 이어적었을 때 전체 길이를 출력하세요.
# 12345 -> 5
# 12345678910 -> 11
# 12345678910111213 -> 17

n = int(input("수 입력 : "))
li=[]
for i in range(1,n+1):
    li.append(i)
    print(li)
print(len(li))
