# 필요 라이브러리 로드
import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from konlpy.tag import Okt

# 7. 영화 리뷰수가 두번째로 많은 영화의 분석 및
# 워드 클라우드 생성 (1-6번 과정 반복)

# 1. 파일 읽어오기
df = pd.read_csv('./data/movie_aisw.csv')

# 2. 데이터 탐색(구성과 데이터 타입 확인)
print(df.info())
print(df.dtypes)

# 3. 영화 개수 확인
print(df['movie'].describe())
print(df['movie'].unique()) # 중복 없이 나온 영화 제목 : 총 6개

# 4. 영화별 평점과 리뷰 수 확인
# 영화 이름별로 그룹화 후, 리뷰 수 내림차순으로 정렬
df_groupby = df.groupby('movie').count()
df_groupby_sort = df_groupby.sort_values(by='sentence', ascending=False)
print(df_groupby_sort)

# 5. '블랙 팬서: 와칸다 포에버' 영화대한 형태소 분석(불용어 제거)
df_2 = df[df['movie'].str.contains\
 ('블랙 팬서: 와칸다 포에버')].copy()
print(df_2.count())

# 중복 제거 및 결측치 확인
print(df_2['movie'].nunique())
print(df_2.isnull().sum()) # 결측치와 중복값 없음.

# 불용어 제거 및 형태소 토큰화
okt = Okt()

# 불용어의 배열 집합
stopword = ['점', '정말', '왜', '말', '그', '없다',
 '정도', '걸', '뭐', '이건','영화', '완전',
 '좀', '있는', '거', '나','이', '볼', '입니다',
 '것', '이런', '더', '수', '때']

list = []
for sentence in df_2['sentence']:
     s_list = okt.pos(sentence)
     for word, tag in s_list:
        if word not in stopword:
            if tag in ['Noun', 'Adjective']:
                list.append((word))

counts = collections.Counter(list)
tag = counts.most_common(50)
# 빈도수가 많은 상위 50개의 단어 출력
print(tag)

# 6. '블랙 팬서: 와칸다 포에버' 영화에 대한 WordCloud 생성
font_path = 'C:/Windows/Fonts/malgun.ttf'
wc = WordCloud(font_path=font_path, background_color='black', max_font_size=50)

# 빈도수가 많은 상위 50개의 단어로 워드클라우드 생성
cloud = wc.generate_from_frequencies(dict(tag))

# 화면에 출력
plt.imshow(cloud)
plt.show()
