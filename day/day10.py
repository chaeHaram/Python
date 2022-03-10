# break 반복문을 빠져나간다.

# for i in range(10):
#     print(i)
#     if i ==2:
#         break

# for i in ['a','b','c','d','e']:
#     print(i)
#     if i =='d':
#         break

# 반복문 밖에서 사용하면 어떻게 되는가 ? 

# 반복문 안에서 써야하고, 제일 가까운 반복문(loop) 하나를 빠져나간다.
# for i in [1,2,3]:
#     for j in [4,5,6]:
#         print(i,j)
#         if j == 5:
#             break
#     print("A")

# for i in range(1,11):
#     print(i)
#     if i>3:
#         continue

# 함수 구문(if, for, while)
# --- ---
# 반복문 (for, while)
# for : 반복 횟수가 명확
# while : 반복횟수가 명확x
# > 게임,  GUI 프로그래밍

# while Bool:
#   [종속문장]
# bool 값이 참일 때 동안 종속문장 반복
# 반복의 의미가 강함! (반복간 변하는 값은 일일히 지정)

# for i in range(1,10):
#     print(i)

# print("="*30)

# n = int(input())
# i = 1
# while i<10:
#     print(f"{n}x{i}={n*i}")
#     i+=1

# j=2
# while j<10:
#     i=1
#     while i<10:
#         print(f"{j}x{i}={j*i}")
#         i+=1
#     j+=1

# su=0
# cnt=0
# while True:
#     n = int(input("수 입력 : "))
#     su+=n
#     cnt+=1
#     if n==0:
#         avg=su/cnt
#         print(avg)
#         break

# li=[]
# while True:
#     n = int(input("입력 : (종료q)"))
    
#     if n.isnumeric():
#         n=int(n)
#         li.append(n)
#     else:
#         if n =="q":
#             if li:
#                 print("합",sum(li)/len(li))
#             else:
#                 print("리스트가 비어있어요!")
#                 print("Program EXIT!")
#             break
#         else:
#             print("숫자만 입력하세요")
    
# 0 입력시 편균 이상인 수들을 출력하세요.

# li=[]
# while True:
#     n = input("입력 : (종료 : 0)")
#     if n.isnumeric():
#         n=int(n)
#         li.append(n)
#     else:
#         if n =="0":
#             if li:
#                 avg=sum(li)/len(li)
#                 print("평균",avg)
#                 for i in li:
#                     if i>=avg:
#                         print("평균 이상인 수",i)
#             else:
#                 print("리스트가 비어있어요!")
#                 print("Program EXIT!")
#             break
#         else:
#             print("숫자만 입력하세요")


# 문자열.isnumeric()
# >앞의 문자열이 숫자로 이루어져있다면 True
# >숫자가 아닌게 섞여있다면 False

# """0 입력 시 까지 숫자들의 평균이상인 수들을 출력하세요."""
# li = [] 
# while True:    
#     N = input("입력 (종료q) : ")

#     if N.isnumeric(): # N 이 숫자로된 문자열이라면
#         N = int(N)
#         li.append(N)
#     else: # N 에 문자섞여있다면
#         if N == "q":
#             if li:
#                 A = sum(li)/len(li)
#                 print(f"입력한 수들의 합 {A}")
#                 for i in li:
#                     if i >= A:
#                         print(f"{i} 는 평균이상!")
#             else:
#                 print("리스트가 비어있어요!!")
#                 print("Program EXIT!")
#             break
#         else:
#             print("숫자만 입력해주세요!!")

# 자판기 프로그램
import time
import os

money=0
while True:
    print("---- Menu ----")
    print("1. 콜라 / 300")
    print("2. 사이다 / 300")
    print("3. 커피 / 200")
    print("4. 돈 넣기")
    print("5. 잔돈 반환")
    print("6. 종료")
    print("---------------")
    print("현재금액 ",money)
    menu=int(input("메뉴선택 : "))
    if menu==1:
        if money<300:
            print("금액이 부족합니다.")
        else:
            print("콜라 맛있게 드세요!")
            money-=300
        for i in range(10):
            print("★"*(10-i) + "☆"*i)
            time.sleep(0.2)
            os.system("clear") 
    elif menu==2:
        if money<300:
            print("금액이 부족합니다.")
        else:
            print("사이다 맛있게 드세요!")
            money-=300
        for i in range(10):
            print("★"*(10-i) + "☆"*i)
            time.sleep(0.2)
            os.system("clear")
    elif menu==3:
        if money<200:
            print("금액이 부족합니다.")
        else:
            print("커피 맛있게 드세요!")
            money-=200
        for i in range(10):
            print("★"*(10-i) + "☆"*i)
            time.sleep(0.2)
            os.system("clear")
    elif menu==4:
        if money!=0:
            money2=int(input("돈을 넣어주세요 : "))
            su = money+money2
            money=su
        else:
            money=int(input("돈을 넣어주세요 : "))
        for i in range(10):
            print("★"*(10-i) + "☆"*i)
            time.sleep(0.2)
            os.system("clear")
    elif menu==5:
        if money==0:
            print("반환할 잔돈이 없습니다.")
        else:
            print("잔돈",money,"원이 반환됩니다.")
            money=0
        for i in range(10):
            print("★"*(10-i) + "☆"*i)
            time.sleep(0.2)
            os.system("clear")
    elif menu==6:
        print("자판기 사용이 종료됩니다.")
        break
    else:
        print("올바른 메뉴를 선택해주세요.")
        for i in range(10):
            print("★"*(10-i) + "☆"*i)
            time.sleep(0.2)
            os.system("clear")
