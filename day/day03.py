#print( input("입력 : ") )

# input(문자열)
# 문자열을 화면에 출력하고
# 입력이 들어올 때까지 기다려라.
# 입력이 들어오면 해당 자료 문자열을 반환

# 정수 int
# 문자열 str
# 실수 float
# 복소수 complex

# name = input("이름 : ")
# age = input("나이 : ")
# email = input ("이메일 : ")
# print("이름 : ",name,"나이 : ",age,"이메일 : ",email)

# a = int (input("a의 값 : ") )
# b = int (input("b의 값 : ") )

# # a=int(a)
# # b=int(b)

# print("a+b = ",a+b)
# print("a-b = ",a-b)
# print("a*b = ",a*b)

# kor = int( input("국어 점수 : "))
# math = int( input ("수학 점수 : "))
# sci = int ( input ("과학 점수 : "))
# avg = float((kor+math+sci)/3)
# print("세 과목의 평균은 ",avg)

# apple = 3000
# pear = 2000

# a = int ( input ("사과 갯수 : "))
# b = int ( input ("배 갯수 : "))
# total = (apple*a)+(pear*b)
# print("총 금액 : ",total)

# hour = int(input("시간 입력 : "))
# min_ = int(input("분 입력 : "))
# sec = int(input("초 입력 : "))

# total_sec = hour*3600+min_*60+sec

# print("입력한 시간은 총 ",total_sec,"초 입니다.")

# print("==============================")
# print("삼각형의 넓이를 구해드립니다.")
# print("==============================")
# a = int(input("밑변 : "))
# b = int(input("높이 : "))

# area = a*b/2

# print("삼각형의 넓이는 ",area,"입니다.")

# print("="*30)
# print("원의 둘레, 넓이를 구해드립니다.")
# print("="*30)
# r = int(input("반지름 : "))

# round_ = float(2*3.14*r)
# area = 3.14*r*r

# print("원의 둘레는 ",round_,"입니다.")
# print("원의 넓이는 ",area,"입니다.")

# print("="*30)
# print("섭씨온도를 화씨온도로 바꿔드립니다.")
# print("="*30)

# a = float(input("섭씨온도 입력 : "))

# b = a*1.8+32

# print("섭씨온도",a,"> 화씨온도",b)

# a = int(input ("세자리 수 입력 : "))
# x = a//100
# y = a%100//10
# z = a%10
# print("일의자리는 ",z)
# print("십의자리는 ",y)
# print("백의자리는 ",x)

# birth = int(input("생년월일을 입력해주세요 (ex 19851210) > "))
# year = birth//10000
# month = birth%10000//100
# day = birth%100
# print(year,"년",month,"월",day,"일생")

total_sec = int(input("총 초를 입력하세요 : "))
hour = total_sec//3600
min_ = total_sec%3600//60
sec = total_sec%60
print(total_sec,"는",hour,"시간",min_,"분",sec,"초 입니다.")