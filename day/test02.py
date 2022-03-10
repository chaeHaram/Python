import test01

# import sys
# print(sys.path)

A = test01.Maple()
B = test01.add(60,40)
C = test01.B

print(B,C)

# import 사용하면
# 클래스, 함수, 변수
# 가져다 사용 가능!

# import random
# print(random.randint(1,10))

# import의 변형
# from 파일이름 import 클래스, 함수, 변수

from test01 import Maple

A = Maple()
# 그렇지만, Maple 하나만 가져올 때 사용

import test01 as t1
t1.Maple()
t1.add(1,10)

# mac은 pip3
# win은 pip
# pip install googletrans==4.0.0-rc1

# import googletrans
# from googletrans import Translator
 
# # print(googletrans.LANGUAGES)
 
# text1 = "Hello welcome to my website!"
 
# text2 = "안녕하세요! 환영합니다."
 
# text3 ="한글을 영어로 번역합니다"
 
# translator = Translator()
 
# print(translator.detect(text1))
# print(translator.detect(text2))
# print(translator.detect(text3))
 
# trans1 = translator.translate(text1, src='en', dest='ja')
# trans2 = translator.translate(text2, src='ko', dest='de')
# trans3 = translator.translate(text3, src='ko', dest='en')
 
# print("English to Japanese: ", trans1.text)
# print("Korean to Germany: ", trans2.text)
# print("Korean to English: ", trans3.text)
