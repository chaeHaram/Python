# # import googletrans
# from googletrans import Translator
#  # print(googletrans.LANGUAGES)
# text1 = input("일본어로 번역할 한국어 입력")
# translator = Translator()
# # print(translator.detect(text1))
# trans1 = translator.translate(text1, src='ko', dest='ja')
# print("Korean to Japanese: ", trans1.text)

# LANGUAGES = {
#     'af': 'afrikaans',
#     'sq': 'albanian',
#     'am': 'amharic',
#     'ar': 'arabic',
#     'hy': 'armenian',
#     'az': 'azerbaijani',
#     'eu': 'basque',
#     'be': 'belarusian',
#     'bn': 'bengali',
#     'bs': 'bosnian',
#     'bg': 'bulgarian',
#     'ca': 'catalan',
#     'ceb': 'cebuano',
#     'ny': 'chichewa',
#     'zh-cn': 'chinese (simplified)',
#     'zh-tw': 'chinese (traditional)',
#     'co': 'corsican',
#     'hr': 'croatian',
#     'cs': 'czech',
#     'da': 'danish',
#     'nl': 'dutch',
#     'en': 'english',
#     'eo': 'esperanto',
#     'et': 'estonian',
#     'tl': 'filipino',
#     'fi': 'finnish',
#     'fr': 'french',
#     'fy': 'frisian',
#     'gl': 'galician',
#     'ka': 'georgian',
#     'de': 'german',
#     'el': 'greek',
#     'gu': 'gujarati',
#     'ht': 'haitian creole',
#     'ha': 'hausa',
#     'haw': 'hawaiian',
#     'iw': 'hebrew',
#     'he': 'hebrew',
#     'hi': 'hindi',
#     'hmn': 'hmong',
#     'hu': 'hungarian',
#     'is': 'icelandic',
#     'ig': 'igbo',
#     'id': 'indonesian',
#     'ga': 'irish',
#     'it': 'italian',
#     'ja': 'japanese',
#     'jw': 'javanese',
#     'kn': 'kannada',
#     'kk': 'kazakh',
#     'km': 'khmer',
#     'ko': 'korean',
#     'ku': 'kurdish (kurmanji)',
#     'ky': 'kyrgyz',
#     'lo': 'lao',
#     'la': 'latin',
#     'lv': 'latvian',
#     'lt': 'lithuanian',
#     'lb': 'luxembourgish',
#     'mk': 'macedonian',
#     'mg': 'malagasy',
#     'ms': 'malay',
#     'ml': 'malayalam',
#     'mt': 'maltese',
#     'mi': 'maori',
#     'mr': 'marathi',
#     'mn': 'mongolian',
#     'my': 'myanmar (burmese)',
#     'ne': 'nepali',
#     'no': 'norwegian',
#     'or': 'odia',
#     'ps': 'pashto',
#     'fa': 'persian',
#     'pl': 'polish',
#     'pt': 'portuguese',
#     'pa': 'punjabi',
#     'ro': 'romanian',
#     'ru': 'russian',
#     'sm': 'samoan',
#     'gd': 'scots gaelic',
#     'sr': 'serbian',
#     'st': 'sesotho',
#     'sn': 'shona',
#     'sd': 'sindhi',
#     'si': 'sinhala',
#     'sk': 'slovak',
#     'sl': 'slovenian',
#     'so': 'somali',
#     'es': 'spanish',
#     'su': 'sundanese',
#     'sw': 'swahili',
#     'sv': 'swedish',
#     'tg': 'tajik',
#     'ta': 'tamil',
#     'te': 'telugu',
#     'th': 'thai',
#     'tr': 'turkish',
#     'uk': 'ukrainian',
#     'ur': 'urdu',
#     'ug': 'uyghur',
#     'uz': 'uzbek',
#     'vi': 'vietnamese',
#     'cy': 'welsh',
#     'xh': 'xhosa',
#     'yi': 'yiddish',
#     'yo': 'yoruba',
#     'zu': 'zulu',

# import pyautogui as pi

# for i in range(1000):
#     pi.doubleClick()
 
# print(pyautogui.position())
 
# print(pyautogui.size())
 
# print(pyautogui.onScreen(1000,2000))
 
# print(pyautogui.onScreen(1000,1000))

# 파일 열기(커서)
#f = open("test.txt","w",encoding="utf-8")
#        경로포함 파일이름, 권한
# f = open("a/b/b.txt","w")
# f = open("a/b/c/c.txt","w")
# f = open("a/b/c/d/d.txt","w")
# for i in range(1,101):
#     f.write(f"파이썬 재밌어 {i}\n")

# 파일 닫기
# f.close()


# r 파일 읽기
# 있는 파일을 읽어야함
# 경로확인 필수

# w 파일 쓰기(기존에 있던 파일은 날아감)

# a 파일 쓰기(덧붙여서)

# for i in range(2,10):
#     f = open(f"구구단/{i}단.txt","w",encoding="utf-8")
#     for j in range(1,10):
#         f.write(f"{i} x {j} = {i*j}\n")
#     f.close()

#f = open("test.txt","r",encoding="utf-8")

# print(f.read()) 파일 포인터로 부터 파일 전체 읽어옴
# print(f.readline()) 파일 포인터로 부터 한 줄 읽어옴
# print(f.realines()) 파일 포인터로 부터 한줄 한줄 읽어서 리스트로 변환

#f.close()

#import os

# print(os.listdir("구구단"))

# 구구단 폴더 안에 있는 파일을 읽기
# f=open(이름,)
# os.listdir("구구단") > 구구단 폴더안에 있는 파일 이름들의 리스트를 각각 읽어주면 된다.

import os
for i in os.listdir("구구단"):
    f = open(f"구구단/{i}","r")
    print(f.read())

# 파일종류
# 011011010110101010101010110110110101
# 텍스트 파일 : 텍스트로 해석되야하는 파일
# 바이너리 파일 : 