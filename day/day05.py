# math = int(input("수학 성적 : "))
# sci = int(input("과학 성적 : "))
# avg = (math+sci)/2

# if avg>=90:
#     print("A")
# elif avg>=80:
#     print("B")
# elif avg>=70:
#     print("C")
# else:
#     print("D")

# a = int(input("첫 번째 수 : "))
# b = int(input("두 번째 수 : "))
# op = input("연산자 입력 : ")

# if op=='+':
#     print(a,op,b,"=",a+b)
# elif op=='-':
#     print(a,op,b,"=",a-b)
# elif op=='*':
#     print(a,op,b,"=",a*b)
# elif op=='/':
#     print(a,op,b,"=",a/b)
# else:
#     print("잘못된 연산자 입력")

# mon = int(input("월 : "))

# if 3<=mon<=5:
#     print(mon,"월은 봄입니다!")
# elif 6<=mon<=8:
#     print(mon,"월은 여름입니다!")
# elif 9<=mon<=11:
#     print(mon,"월은 가을입니다!")
# elif 1<=mon<=12:
#     print(mon,"월은 겨울입니다!")
# else:
#     print("입력이 바르지 않습니다.")

# id_=input("아이디 입력 : ")
# pw_=input("비밀번호 입력 : ")

# if id_=="admin":
#     print("Hello admin")
#     pw_=input("패스워드 : ")
#     if pw_=="admin":
#         print("Login success :)")
#     else:
#         print("Login Fail")
# else:
#     print("No User")

# a = int(input("수를 입력하세요 : "))

# if a<0:
#     a=a*-1
# print("절대값은",a,"입니다.")

# i = int(input("구입할 사과의 갯수 : "))
# j = int(input("구입할 배의 갯수 : "))
# have_money = int(input("소지하고 있는 금액 : "))

# apple = 3000
# pear = 2000

# if apple*i+pear*j<=have_money:
#     print("잔돈은",have_money-(apple*i+pear*j),"입니다.")
# elif apple*i+pear*j==have_money:
#     print("잔돈은 없습니다.")
# else:
#     print("구매불가 필요한 금액은 : ",apple*i+pear*j,"입니다.")

# a = int(input("수를 입력하세요 : "))

# if a%15==0:
#     print("15의 배수입니다.")
# elif a%3==0:
#     print("3의 배수입니다.")
# elif a%5==0:
#     print("5의 배수입니다.")
# else:
#     print("3,5,15의 배수가 아닙니다.")

# print("="*20)
# print("1. 아메리카노")
# print("2. 카페라떼")
# print("="*20)
# sel = int(input("메뉴선택 : "))
# if sel==1:
#     sel="아메리카노"
# elif sel==2:
#     sel="카페라떼"
# else:
#     print("잘못된 메뉴입니다.")
# print("="*20)
# print("1. ICE")
# print("2. HOT")
# print("="*20)
# tem = int(input("온도선택 : "))
# if tem==1:
#     tem="아이스"
# elif tem==2:
#     tem="핫"
# else:
#     print("잘못된 온도입니다.")
# print(tem+sel,"선택")

# a = int(input("세자리 첫번째 수 입력 : "))
# b = int(input("세자리 두번째 수 입력 : "))

# if a%10 < b%10:
#     print("뒤집었을 때 큰 수는 ",b,"입니다.")
# elif a%10 > b%10:
#     print("뒤집었을 때 큰 수는 ",a,"입니다.")
# else:
#     if a%100//10 < b%100//10:
#         print("뒤집었을 때 큰 수는 ",b,"입니다.")
#     elif a%100//10 > b%100//10:
#         print("뒤집었을 때 큰 수는 ",a,"입니다.")
#     else:
#         if a//100 < b//100:
#             print("뒤집었을 때 큰 수는 ",b,"입니다.")
#         elif a//100 > b//100:
#             print("뒤집었을 때 큰 수는 ",a,"입니다.")
#         else:
#             print("두 수는 같은 수 입니다.")

# a = int(input("몇일 뒤 당번은? (첫날은 A가 하기로 했다.)"))

# if a%4==0:
#     print("A가 당번")
# elif a%4==1:
#     print("B가 당번")
# elif a%4==2:
#     print("C가 당번")
# elif a%4==3:
#     print("D가 당번")
# else:
#     print("잘못된 값")

# date = int(input("오늘은 금요일이다.\nN일 후에는 무슨 요일일까?\nN의 값 입력 : "))
# if date%7==0:
#     print("금요일")
# elif date%7==1:
#     print("토요일")
# elif date%7==2:
#     print("일요일")
# elif date%7==3:
#     print("월요일")
# elif date%7==4:
#     print("화요일")
# elif date%7==5:
#     print("수요일")
# elif date%7==6:
#     print("목요일")
# else:
#     print("잘못된 값")

# a = int(input("수를 입력하세요 : "))
# b = a**0.5

# if int(b)==b:
#     print(a,"는 제곱수 입니다.")
# else:
#     print(a,"는 제곱수가 아닙니다.")

# hour = int(input("현재 시간은 : "))
# min_ = int(input("현재 분은 : "))

# if min_<30:
#     hour=hour-1
#     min_=min_+30
#     print("30분 전 시간은",hour,"시",min_,"분입니다.")
# elif min_>=30:
#     min_=min_-30
#     print("30분 전 시간은",hour,"시",min_,"분입니다.")
# else:
#     print("잘못된 값입니다.")

# year = int(input("년도를 입력하세요 : "))

# if ((year%4==0) and (year%100!=0)) or (year%400 == 0):
#     print("해당 년은 윤년입니다.")
# else:
#     print("해당 년은 윤년이 아닙니다.")

# hour = int(input("현재 시간은 : "))
# min_ = int(input("현재 분은 : "))
# before = int(input("n분 전 시간을 알려줘 : "))

# if min_<before:
#     hour=hour-1
#     min_=min_+60-before
#     if hour==-1:
#         hour=23
#     print(before,"분 전 시간은",hour,"시",min_,"분입니다.")
# elif min_>=before:
#     min_=min_-before
#     print(before,"분 전 시간은",hour,"시",min_,"분입니다.")
# else:
#     print("잘못된 값입니다.")

# hour = int(input("현재 시간은 : "))
# min_ = int(input("현재 분은 : "))
# after = int(input("n분 후 시간을 알려줘 : "))

# if min_+after>=60:
#     hour=hour+1
#     min_=min_+after-60
#     if hour==24:
#         hour=0
#     print(after,"분 후 시간은",hour,"시",min_,"분입니다.")
# elif min_+after<60:
#     min_=min_+after
#     print(after,"분 후 시간은",hour,"시",min_,"분입니다.")
# else:
#     print("잘못된 값입니다.")

# a = int(input("오늘부터 3일씩 4사람이 돌아가며 청소를 하기로 했다.\n첫날은 A가 하기로 했을 때 N일째 당번은 : "))

# if a%12==1 or a%12==2 or a%12==3:ß
#     print("A가 당번")
# elif a%12==4 or a%12==5 or a%12==6:
#     print("B가 당번")
# elif a%12==7 or a%12==8 or a%12==9:
#     print("C가 당번")
# elif a%12==10 or a%12==11 or a%12==12:
#     print("D가 당번")
# else:
#     print("잘못된 값")