# from bs4 import BeautifulSoup

# st = """
# <html>
#     <body>
#         <div class="hello1">안녕1</div>
#         <div id="hello2">안녕2</div>
#         <div>
#             <span class="hello1">안녕3</span>
#         </div>
#         <a href="https://www.naver.com">Naver가기</a>
#     </body>
# </html>"""

# soup = BeautifulSoup(st, "html.parser")
# print(soup.select_one("div").get("class")) # 속성값 추출

# print(soup.select(".hello1")[0].text)
# print(soup.select_one("div").text)
# soup.select > 태그클래스 인스턴스 리스트
# soup.select_one > 태그클래스 인스턴스

# import requests
# from bs4 import BeautifulSoup

# for i in range(1,251):
#     res = requests.get(f"https://comic.naver.com/webtoon/detail?titleId=728015&no={i}&weekday=wed")
#     soup = BeautifulSoup(res.text,"html.parser")


#     title = soup.select_one(".view > h3").text
#     score = soup.select_one("#topPointTotalNumber").text
#     person = soup.select_one(".pointTotalPerson > em").text
#     print("="*20)
#     print("\n",title,"\n",score,"\n",person)
#     print("="*20)

#(soup.select(".view > h3")[0].text)
#(soup.select("#topPointTotalNumber")[0].text)
#(soup.select(".pointTotalPerson > em")[0].text)

# import requests
# from bs4 import BeautifulSoup

# web = {}

# for k in ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]:
#     res = requests.get(f"https://comic.naver.com/webtoon/weekdayList?week={k}")
#     soup = BeautifulSoup(res.text, "html.parser")

#     for i in soup.select(".thumb > a"): # 네이버 전체 웹툰의 a태그
#         title = i.get("title") # a태그에 title 속성값을 title에 저장
#         num = i.get("href").split("=")[1].split("&")[0] # a태그 안에 href 속성값
#         web[title] = num

# def 제거(st):
#     for i in "\t\r\n":
#         st=st.replace(i, "")
#     return st

# for k in web:
#     res = requests.get(f"https://comic.naver.com/webtoon/list?titleId={web[k]}")
#     soup = BeautifulSoup(res.text, "html.parser")

#     작가 = 제거(soup.select_one(".wrt_nm").text)
#     장르 = soup.select_one(".genre").text
#     연령가 = soup.select_one(".age").text
#     줄거리 = soup.select_one(".detail > p").text

#     print(f"제목\t{k}")
#     print(f"작가\t{작가}")
#     print(f"장르\t{장르}")
#     print(f"연령가\t{연령가}")
#     print(줄거리)


# 함수 문자열에서 \t,\n,\r을 제거해주는 함수
# 입력값 : 문자열
# 반환값 : 문자열

"""
대상 사이트
 - https://lol.inven.co.kr/dataninfo/champion/
   캐릭터 전체가 들어있고, 캐릭터 이름과 코드를 가져와야하는 사이트이다.
   HINT > F12 하시고 캐릭터들 사진 클릭하시면서 이름과 코드가 같이 들어있는 태그를 찾으시면되요

 - https://lol.inven.co.kr/dataninfo/champion/detail.php?code=[ 특정 챔피언 코드 ]
   특정 챔피언의 정보가 들어있다. code 인자에 특정 챔피언 코드를 넣으면 챔피언 정보가 나온다.
   이 곳에서는 캐릭터의 한글이름, 영어이름, 특징, 소개를 가져와야한다.
   """

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init

init()

res = requests.get("https://lol.inven.co.kr/dataninfo/champion/")
soup = BeautifulSoup(res.text,"html.parser")

챔프 = {}

for i in soup.select(".champImage > a"):
    이름 = i.get("title")
    코드 = i.get("href")[16:]#.split("=")[1]
    챔프[이름] = 코드

for i in 챔프:
    res = requests.get(f"https://lol.inven.co.kr/dataninfo/champion/detail.php?code={챔프[i]}")
    soup = BeautifulSoup(res.text, "html.parser")

    한글이름 = soup.select_one(".korName").text
    영어이름 = soup.select_one(".engName").text
    소개 = soup.select_one(".descText").text
    특징 = soup.select_one(".png_bg").text

    print()
    print(Fore.WHITE + Back.BLUE + Style.DIM + "이름" + Style.RESET_ALL + " " + 한글이름)
    print(영어이름)
    print(Fore.WHITE + Back.BLUE + Style.DIM + "소개" + Style.RESET_ALL + " " + 소개)
    print(Fore.WHITE + Back.BLUE + Style.DIM + "특징" + Style.RESET_ALL + " " + 특징)
    print()

#     웹 크롤링 : 웹에서 데이터 가져옴~

# 1. HTML 소스 
# ==================================
# import requests 

# res = requests.get(url)
# ==================================
# res > Response Class 의 인스턴스
#  - res.text     : HTML 소스
#  - res.content  : 바이너리 값


# 2. res.text 아무의미없어요 in Python  문자덩어리
# 파싱~
# ========================================================
# from bs4 import BeautifulSoup

# soup = BeautifulSoup(res.text, "html.parser")
# ========================================================
# soup.select() > 특정 태그를 가져옴


# 3. 태그 지정하는 방법 (selector)

#  - 태그는 그대로
#  - id 속성은 #
#  - class 속성은 .
#  - 하위태그는 >


# 4. soup.select 의 반환값 : Tag class 의 인스턴스들의 리스트!

#  ★ Tag class 라면 할 수 있는 속성과 행동

#   - .text             :  텍스트 부분을 반환
#   - .get(A)           :  A 속성의 속성값을 반환
#   - .select(Selector) : 마저 자를 수 있음