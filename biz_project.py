import streamlit as st # 1. 무조건 맨 위에 써야 함 [cite: 118]
import pandas as pd
import numpy as np
from PIL import Image

# 텍스트 출력 종류별 모음 [cite: 121, 124, 127]
st.title('큰 제목 (Title)') 
st.write('# 일반 텍스트 (Markdown 가능)') 
st.markdown('**굵은 글씨**나 *기울임* 등 자유로운 꾸미기')

# 데이터 표(DataFrame) 그리기 [cite: 31, 36]
st.write('# 2. 표 그리기')
df = pd.DataFrame({
    '항목1': ['A', 'B', 'C'],
    '항목2': [10, 20, 30]
})
st.dataframe(df) # 마우스로 정렬 가능한 표가 웹에 뜸

# 막대 그래프 그리기 [cite: 42, 44]
st.write('# 3. 그래프 그리기')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data) # 변수만 넣으면 그래프가 자동 생성됨

# 이미지 넣기 (폴더에 이미지 파일이 있어야 함) [cite: 47, 50, 51]
# img = Image.open('이미지파일이름.png')
# st.image(img, width=300)
