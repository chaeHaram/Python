# 크롤링
# 네트워크란?
# client : 데이터를 요청하는 주체
# server : 데이터를 제공하는 주체
# request : 데이터를 요청하는 행위
# response : 데이터를 제공하는 행위

# requests > Client가 Web Server에 데이터를 요청하는것
# response > Web Server가 Client에게 데이터를 주는것
# 웹브라우저 > 크롬 사파리 인터넷익스프로러 파이어폭스

# pip3 install requests
# requsets.get(url)
# url로 requests를 날려준다 > response를 반환

# import requests
# res = requests.get("https://www.naver.com")
# f=open("짝퉁naver.html","w",encoding="utf-8")
# f.write(res.text)
# f.close
# print(res.text) # > html 소스

# 데이터 전송 방식(웹)
# 1) get : url을 통해서 전송!
# ? > 데이터 전송의 시작
# & > 데이터와 데이터를 연결

# 2) post : 숨겨서 전송!

# import requests
# for i in range(1,51):
#     res = requests.get(f"https://comic.naver.com/webtoon/detail?titleId=728015&no={i}&weekday=wed")
#     f=open(f"모죠/모죠{i}화.html","w",encoding="utf-8")
#     f.write(res.text)
#     f.close()

# from bs4 import BeautifulSoup
# st="""
# <html>
#     <body>
#         <div class="hello1">안녕1</div>
#         <div id="hello2">안녕2</div>
#         <div class="b">
#             <span id="hello2">안녕3</span>
#         </div>
#         <a href="https://www.naver.com">Naver로 가기</a>
#     </body>
# </html>
# """
# st는 test.html에 requests.get으로 요청해서
# res.text를 받아온 것으로 가정~

# 파싱!! : 규격에 맞춰서 해석함

# beautifulsoup(아무 의미 없는 문자열, 파서)
# from bs4 import BeautifulSoup

# soup = BeautifulSoup(st,"html.parser")
# print(soup.select("div")) # 태그 그대로
# print(soup.select("#hello2")) # id속성
# print(soup.select(".hello1")) # class속성
# print(soup.select("div#hello2")) # id속성
# print(soup.select("span#hello2")) # id속성
# print(soup.select("html>body>div>span")) # 하위태그
# print(soup.select("html>#a>.b>#hello2"))

# st를 html 규격에 맞춰서 해석할 수 있는
# soup 친구(인스턴스)를 만든다!!

# soup.select(셀렉터 표현)
# * Selector : 태그를 지칭하는 방법
# css, javascript, jQuery ..

# 1) 태그 그대로
# 2) id 속성은 #
# 3) class 속성은 .
# 4) 하위태그 >

# 1. Html 소스 가져오기
# requests Library
# =====================
# res = requests.get(*)
# =====================
# *에 request 날려주고, response 반환
# res는 특정 클래스의 인스턴스
# res.text : 이게 바로 requests 라이브러리 사용하는 목적

# 2. res.text는 python에서 웹의 언어로 해석 되지 않아요. 그냥 문자 덩어리 일뿐...
# ========================================
# soup = BeautifulSoup(문자열,"html.parser")
# ========================================
# 아무의미없는 문자열을 html 형식으로 해석할 수 있는 soup 만들어줌

# 3. Selector > tag를 지칭하는 방법 (효율적으로 정보 접근)
# - 태그 그대로, id #, class ., 하위태그 >
# ========================================
# soup.select("selector")
# ========================================

# import requests
# res = requests.get(f"https://comic.naver.com/webtoon/detail?titleId=728015&no=250&weekday=wed")
# f=open(f"모죠/모죠250화.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()

import requests
from bs4 import BeautifulSoup

for k in range(1,251):
    res = requests.get(f"https://comic.naver.com/webtoon/detail?titleId=728015&no={k}&weekday=wed")
    soup = BeautifulSoup(res.text,"html.parser")

    print(soup.select("#topPointTotalNumber > strong"))
    print(soup.select(".view > h3"))
    print(soup.select(".pointTotalPerson > em"))

import requests
res = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EC%BC%80%EB%84%A8&oquery=%EB%A1%A4+%EB%8B%A4%EC%9D%B4%EC%95%A0%EB%82%98&tqi=hjeW0dprvhGssaVoUBZssssstpV-362152")
# res.text : html소스
# res.content : 바이너리 값
f=open("kenen.png","wb")
f.write(res.content)
f.close()