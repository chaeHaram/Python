# # 자판기 프로그램
# import time
# import os

# money=0
# while True:
#     print("---- Menu ----")
#     print("1. 콜라 / 300")
#     print("2. 사이다 / 300")
#     print("3. 커피 / 200")
#     print("4. 돈 넣기")
#     print("5. 잔돈 반환")
#     print("6. 종료")
#     print("---------------")
#     print("현재금액 ",money)
#     menu=int(input("메뉴선택 : "))
#     if menu==1:
#         if money<300:
#             print("금액이 부족합니다.")
#         else:
#             print("콜라 맛있게 드세요!")
#             money-=300
#     elif menu==2:
#         if money<300:
#             print("금액이 부족합니다.")
#         else:
#             print("사이다 맛있게 드세요!")
#             money-=300
#     elif menu==3:
#         if money<200:
#             print("금액이 부족합니다.")
#         else:
#             print("커피 맛있게 드세요!")
#             money-=200
#     elif menu==4:
#         if money!=0:
#             money2=int(input("돈을 넣어주세요 : "))
#             su = money+money2
#             money=su
#         else:
#             money=int(input("돈을 넣어주세요 : "))
#     elif menu==5:
#         if money==0:
#             print("반환할 잔돈이 없습니다.")
#         else:
#             print("잔돈",money,"원이 반환됩니다.")
#             money=0
#     elif menu==6:
#         print("자판기 사용이 종료됩니다.")
#         break
#     else:
#         print("올바른 메뉴를 선택해주세요.")
#     for i in range(10):
#         print("★"*(10-i) + "☆"*i)
#         time.sleep(0.5)
#         os.system("clear")


# st = f"""===========================
# 1. 콜라 / 300
# 4. 돈입력
# 5. 잔돈반환
# 6. 종료
# ===========================
# 현재금액 {money}
# """

# while True:    
#     # 메뉴출력
#     for i in st:
#         print(i, end="")
#         time.sleep(0.001)

# import random

# print(random.randint(1,10))

# random,randint(a,b)
# a에서 b까지 랜덤한 수를 반환

"""
1. 랜덤으로 숫자하나 받아주세요 (1,100)
2. 사용자에게 홀짝을 입력받습니다.
3. 만약 맞추면, "맞았습니다", 틀리면 "틀렸습니다."
"""

# import random
# import os
# import time

# life = 5
# combo = 0
# score = 0

# st = """홀짝게임에 오신 여러분 안녕하세요. """

# for i in st:
#     print(i, end="")
#     time.sleep(0.01)
# input("\n\nGAME START (ENTER) ")
# os.system("clear")

# while True:

#     print("="*20)
#     print("♥"*life+"♡"*(5-life))
#     print("Score : ",score)
#     print(combo,"Combo!")
#     print("="*20)

#     if life==0:
#         print("Game Over")
#         break

#     com = random.randint(1,100)
#     user = int(input("홀(1)? 짝(0)? "))

#     if com % 2 == user:
#         score +=100 * (1+0.2*combo)
#         combo +=1
#         print("맞았습니다.")
#     else:
#         life -=1
#         print("틀렸습니다.")
#         combo=0
#     print(f"원래 수는 : {com}")

"""
1. 랜덤으로 숫자를 받습니다 (1~9)(com)
2. 사용자에게 숫자를 입력받습니다(user)
3. com이 user보다 작으면 down!
   user가 com보다 작으면 up!
   맞추면 correct!
"""

# import random
# import os
# import time
# cnt = 0

# while True: 

#     while True:
#         st = """
#         ====================
#         난이도 선택 : 
#         1. Easy (1-9)
#         2. Normal (1-99)
#         3. Hard (1-999)
#         ====================
#     """
#         for i in st:
#             print(i, end="")
#             time.sleep(0.01)
#         level = int(input("Level Choice > "))

#         if level == 1:
#             com = random.randint(1,9)
#         elif level == 2:
#             com = random.randint(10,99)
#         elif level == 3:
#             com = random.randint(100,999)
#         else:
#             print("INPUT ERROR!!!")
#             time.sleep(0.5)
#             os.system("clear")
#             continue
        
#         break
#     os.system("clear")

#     while True:

#         user = int(input("수 입력 : "))
#         cnt+=1
#         if com < user:
#             print("down!")
#         elif user < com:
#             print("up!")
#         else:
#             print("correct")
#             print("원래 수는 : ",com)
#             print(cnt,"회 만에 정답")
#             break
#     again = int(input("다시 하시겠습니까? : 1.네, 0.아니요 : "))
#     if again == 0:
#         print("Good bye")
#         break
#     elif again==1:
#         os.system("clear")
#         continue

"""
1. 한 자리수 두개를 랜덤으로 받아주세요.(a,b)
2. 사용자에게 'a+b='이라고 물어보고, 입력받는다.
3. 만약 계산을 맞추면 맞았습니다. 틀렸습니다.
4. life, score 추가
5. 난이도 선택
    easy(한자리 수)
    normal(두자리 수)
    hard(세자리 수)
6. 계속하시겠습니까?
7. 뺄셈 문제도 일정확률 등장
"""

import random
import time
import os

score = 0
life = 5

while True:
    while True:
        print("="*20)
        print("1. Easy")
        print("2. Normal")
        print("3. Hard")
        print("="*20)

        level = int(input("Choice Level : "))

        if level == 1:
            r1=1
            r2=9
        elif level == 2:
            r1=10
            r2=99
        elif level==3:
            r1=100
            r2=999
        else:
            print("Error!")
            continue
        break

    while True:

        # 게임 상황판
        print("="*20)
        print("♥"*life+"♡"*(5-life))
        print("Your Score : ",score)
        print("="*20)

        # 게임오버 판단
        if life <= 0:
            print("Game Over")
            break

        # 랜덤 변수 생성
        a = random.randint(r1,r2)
        b = random.randint(r1,r2)
        op = random.randint(1,2) # 1 > +, 2 > -
        s200 = random.randint(1,5) # 1일때 200점
        life2 = random.randint(1,7) # 1일때 2라이프

        # 점수 세팅
        if s200==1:
            print("이번 문제는 score + 200")
            점수=200
        else:
            점수=100

        # 라이프 두개
        if life2==1:
            print("이번 문제는 life -2")
            라이프=2
        else:
            라이프=1

        # 문제 출제 및 정답 세팅
        if op==1:
            user = int(input(f"{a}+{b} = "))
            answer=a+b
        elif op==2:
            if a>b:
                user = int(input(f"{a}-{b} = "))
                answer=a-b
            else:
                user = int(input(f"{b} - {a} = "))
                answer = b-a
            
        # 채점
        if user == answer:
            score+=점수
            print("맞았습니다.")
        else:
            life -=라이프
            print("틀렸습니다.")

    again = int(input("Continue ? yes(1), no(0) : "))
    if again ==0:
        print("Program Exit!")
    break

