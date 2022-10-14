## 터미널에 ##
## pip install snscrape ##
## pip install pandas 입력 및 실행 후 코드를 실행해주세요 ##

import snscrape.modules.twitter as sntwitter
import pandas as pd

#query 부분 검색어 반드시 바꿔주기
#https://twitter-michelin-guide.netlify.app/에서 그룹 검색-지역 검색 후 뜨는 검색어를 query 부분에 추가해주세요

query = "합정#몬베베가_몬베베에게_추천하는_맛집 OR #셔누_넌이미먹었겠지만또먹어야겠지 OR #민혁_너는이미북마크해놨겠지 OR #기현_너는맘마먹고다시시작하겠지 OR #채형원_너는세입도못먹겠지  OR #주헌_너는한입가득못먹겠지 OR #임창균_너는한끼뚝닭먹겠지"

tweet_list = []  #데이터 프레임을 만들기 위한 빈 리스트 지정
limit = 1000 #트위터 글을 1000개까지만 가져오도록 설정

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweet_list) == limit: #트위터 글이 1000개 이상인 경우 트위터 글을 더 이상 가져오지 않음
        break
    else:
        tweet_list.append([tweet.date, tweet.user.username, tweet.user.displayname, tweet.content, tweet.url])
        
        ## 이 코드로 읽어올 수 있는 것 ##
        # 트위터 글 날짜
        # 유저 아이디
        # 유저 닉네임
        # 트위터 글
        # 트위터 링크
        
df = pd.DataFrame(tweet_list, columns = ['Date', 'User', 'Nickname', 'Tweet', 'URL'])

print(df)

#csv로 저장
#반드시 저장명을 검색어를 바꿀때마다 변경해주세요 (변경하지 않으면 기존 파일을 덮어씁니다)
df.to_csv('합정-몬스타엑스.csv', encoding='utf-8-sig') #한글이 깨지므로 반드시 인코딩 형식 설정

#검색어를 변경한 이후 파이썬 파일을 반드시 저장한 후에 터미널에서 python tweets.py 실행해주세요



