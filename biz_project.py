import streamlit as st # 1. 무조건 맨 위에 써야 함 [cite: 118]
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 1. 페이지 대문 제목
st.title("🎸 내 취향 저격! 대한민국 대표 음악 페스티벌 대시보드")
st.write("수많은 페스티벌 중 가장 개성이 뚜렷한 5가지 페스티벌의 위치와 정보를 한눈에 비교합니다.")
st.divider() # 구분선

# 2. 데이터프레임 (표) 만들기
st.header("📋 1. 페스티벌 기본 정보 비교")

festival_data = pd.DataFrame({
    '페스티벌명': ['인천 펜타포트', '부산국제록페', '서울 파크뮤직', '피크 페스티벌', '더글로우'],
    '특징': ['정통 락 & 해외 라인업', ' 국내외 메이저 락 밴드', '도심 속 피크닉 감성', '한강 라이브 밴드 정수', '쾌적한 감성 밴드 중심'],
    '티켓가격(원)': [220000, 160000, 110000, 100000, 120000],
    'lat': [37.432, 35.166, 37.520, 37.567, 37.663], # 위도
    'lon': [126.631, 128.971, 127.121, 126.877, 126.746] # 경도
})

# 화면에 표 출력
st.dataframe(festival_data[['페스티벌명', '특징', '티켓가격(원)']])
st.divider()

# 3. 지도 그리기 (각자 위치가 다르다는 개성 어필!)
st.header("🗺️ 2. 전국 페스티벌 개최 위치")
st.write("각 페스티벌이 열리는 전국의 주 무대를 확인해 보세요.")
# lat과 lon 컬럼만 쏙 빼서 지도에 점 찍기
map_data = festival_data[['lat', 'lon']]
st.map(map_data)
st.divider()

# 4. Matplotlib로 티켓 가격 비교 그래프 그리기
st.header("📊 3. 페스티벌별 티켓 가격 비교")

fig, ax = plt.subplots(figsize=(7, 4))
# 막대 그래프 그리기 (x축: 페스티벌명, y축: 티켓가격)
ax.bar(festival_data['페스티벌명'], festival_data['티켓가격(원)'], color=['red', 'blue', 'green', 'orange', 'purple'])
ax.set_ylabel("가격 (원)")
ax.set_title("2026년도 페스티벌 1일권 티켓 가격 비교")
ax.grid(True, axis='y', linestyle='--')

# 💡 윈도우 환경에서 한글 깨짐 방지 팁 (필요시 사용)
plt.rcParams['font.family'] = 'Malgun Gothic'

st.pyplot(fig) # 스트림릿에 그래프 출력