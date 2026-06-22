import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import random


favorite_bands = ['잔나비', '드래곤포니', '리도어', '실리카겔', '신인류', '이승윤', '한로로', '오월오일']
recommended_band = random.choice(favorite_bands)

st.title('🎸 국내 락 페스티벌 가이드')
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Introduce", "Comparison", "Preparation"])

#---------------------------------------------------------------------------------------
with tab1:
    st.header('오늘의 추천 밴드')
    st.success(
        icon="✅",
        body=f"오늘의 랜덤 추천 밴드는 **{recommended_band}**입니다!")
    
    st.caption("💡 새로고침(F5)을 누를 때마다 오늘의 추천 밴드가 무작위로 변경됩니다.")
    st.divider()

    st.header('당신은 어떤 스타일의 페스티벌 관객인가요?')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success('**🔥 스탠딩/슬램파**\n\n무대와 가까운 거리에서 현장 분위기를 느끼며 슬램하고 뛰노는 열정파')
    with col2:
        st.info('**🌿 돗자리/힐링파**\n\n뒤쪽에 돗자리를 펴고 맥주를 마시며 여유롭게 음악을 감상하는 힐링파')
    with col3:
        st.warning('**🌭 F&B 미식파**\n\n락페는 먹으러 오는 것! 푸드코트를 섭렵하는 먹방파')
    st.divider()

    st.subheader('웹사이트 안내')
    st.markdown(
        """
        **국내 락 페스티벌 가이드**에 오신 것을 환영합니다. \n
        이 서비스는 국내에 존재하는 대표적인 메이저 락 페스티벌 5개의 핵심 정보들을 비교/점검할 수 있도록 제작된 가이드 웹입니다.
        
        상단의 탭을 클릭하여 자유롭게 페스티벌 가이드를 탐색해 보세요!
        
        *   **Home**: 메인 홈 페이지입니다. 오늘의 추천 밴드를 뽑고, 본인의 관람 성향을 알아볼 수 있습니다.\n
        *   **Introduce**: 국내 주요 페스티벌의 상세 특징, 가격 등 핵심 정보들을 알 수 있습니다.\n
        *   **Comparison**: 진행 날짜, 개최 위치와 같은 페스티벌별 주요 정보들을 표/그래프로 한 눈에 비교할 수 있습니다.\n
        *   **Preparation**: 페스티벌별 현장 스케치 영상과 함께 준비물 체크리스트를 제공합니다.
        """
    )


#-------------------------------------------------------------
with tab2:
    st.header('Introduce')
    st.markdown('국내 주요 페스티벌(The Glow, 인천 펜타포트 락 페스티벌, 부산 국제 록 페스티벌, 피크 페스티벌, 파크 뮤직 페스티벌) 주요 정보 및 특징 정리')
    st.divider()

    st.subheader('1. TheGlow (더글로우)')
    col_g1, col_g2 = st.columns([2, 1])
    with col_g1:
        st.markdown('**✨ 테마**: :yellow[빛과 심플함을 주요 키워드로 꾸민 세련된 실내 대중 페스티벌]')
        st.markdown('**📍 개최 장소**: 일산 킨텍스 (KINTEX)')
        st.markdown('**📅 개최 일자**: 매년 3월 말 (봄)')
        st.markdown('**🎫 티켓 가격**: 1일권 121.000 / 2일권 193.000')
    with col_g2:
        st.warning('**🎵 대표 라인업**\n\n(2026 기준) 리도어, 이찬혁, 혁오, 드래곤포니, 놀이도감')
    st.markdown('**특징**: :yellow[날씨 걱정 없는 쾌적한 실내 공간에서 대중적인 밴드들의 공연을 즐길 수 있고, 빛을 활용한 다양한 포토존과 내부 환경을 만나볼 수 있다.]')
    st.divider()

    st.subheader('2. 인천펜타포트 락 페스티벌')
    col_p1, col_p2 = st.columns([2, 1])
    with col_p1:
        st.markdown('**✨ 테마**: :red[대한민국에서 가장 규모가 큰 록 페스티벌]')
        st.markdown('**📍 개최 장소**: 인천 송도달빛축제공원')
        st.markdown('**📅 개최 일자**: 매년 8월 (여름)')
        st.markdown('**🎫 티켓 가격**: 1일권 120.000 / 3일권 240.000')
    with col_p2:
        st.error('**🎵 대표 라인업**\n\n(2026 기준) PIXIES, 술탄오브더디스코, 실리카겔, 이승윤')
    st.markdown('**💬 특징**: :red[우리나라 락 페스티벌의 역사이자 산증인으로, 과격한 슬램과 함께 유명한 해외 밴드들의 공연을 즐길 수 있는 정통 락 축제이다.]')
    st.divider()

    st.subheader('3. 부산 국제 록 페스티벌')
    col_b1, col_b2 = st.columns([2, 1])
    with col_b1:
        st.markdown('**✨ 테마**: :blue[해외 유명 밴드들과 국내 최정상 밴드들이 모이는 대규모 페스티벌]')
        st.markdown('**📍 개최 장소**: 부산 삼락생태공원')
        st.markdown('**📅 개최 일자**: 매년 10월 (가을)')
        st.markdown('**🎫 티켓 가격**: 1일권 110.000 / 2일권 176.000 / 3일권 242.000')
    with col_b2:
        st.info('**🎵 대표 라인업**\n\n(2025 기준) 자우림, THE SMASHING PUMKINS, SUEDE, 터치드')
    st.markdown('**💬 특징**: :blue[가장 오래된 역사를 가진 가을 대표 페스티벌로, 드넓은 잔디밭 위에서 국내 최정상 밴드들과 해외 유명 밴드들의 공연을 즐길 수 있다.]')
    st.divider()

    st.subheader('4. 피크 페스티벌')
    col_pk1, col_pk2 = st.columns([2, 1])
    with col_pk1:
        st.markdown('**✨ 테마**: :orange[서울 난지 한강 잔디밭에서 즐기는 음악 축제]')
        st.markdown('**📍 개최 장소**: 서울 난지한강공원')
        st.markdown('**📅 개최 일자**: 매년 5월 (봄)')
        st.markdown('**🎫 티켓 가격**: 1일권 110.000 / 2일권 149.000')
    with col_pk2:
        st.warning('**🎵 대표 라인업**\n\n(2026 기준) SPYAIR, 극동아시아타이거즈, 리도어, 로맨틱펀치, 바이바이밴드맨')
    st.markdown('**💬 특징**: :orange[한강공원 잔디마당 위에서 싱그러운 바람과 가슴이 탁 트이는 강변 뷰를 자랑하며, 화려하고 폭발적인 밴드 라이브 공연으로 한 해 락페의 시즌 개막을 알립니다.]')
    st.divider()

    st.subheader('5. 서울 파크 뮤직 페스티벌')
    col_pm1, col_pm2 = st.columns([2, 1])
    with col_pm1:
        st.markdown('**✨ 테마**: :green[서울 정중앙에서 개최되는 피크닉이 결합된 대중음악 페스티벌]')
        st.markdown('**📍 개최 장소**: 서울 올림픽공원 잔디마당')
        st.markdown('**📅 개최 일자**: 매년 6월 (초여름)')
        st.markdown('**🎫 티켓 가격**: 1일권 119.000 / 2일권 없음')
    with col_pm2:
        st.success('**🎵 대표 라인업**\n\n(2026 기준) 잔나비, 윤마치, 토카이, 정승환, 권진아, 데이먼스 이어')
    st.markdown('**💬 특징**: :green[도심 한가운데에서 맛있는 음식과 시원한 맥주를 마시며 돗자리에 기대어 감상할 수 있는 대중적인 이지리스닝 피크닉형 페스티벌이다.]')
    st.divider()


# ------------------------------------------------------------
with tab3:
    st.header('Comparison')
    st.markdown('5개의 국내 주요 페스티벌의 일정, 장소, 가격, 그리고 공간 유형별 특징을 다각도로 분석하여 비교')
    st.divider()

    st.subheader('페스티벌 기본 정보 요약')
    comparison_df = pd.DataFrame({
        '페스티벌': ['더글로우', '펜타포트', '부산 국제 록 페스티벌', '피크 페스티벌', '파크 뮤직 페스티벌'],
        '개최지': ['일산 킨텍스', '인천 송도달빛축제공원', '부산 삼락생태공원', '서울 난지한강공원', '서울 올림픽공원 일대'],
        '개최 월': [3, 8, 10, 5, 6],
        '1일권 가격': [121000, 120000, 110000, 110000, 119000]
    })
    st.dataframe(comparison_df)
    st.divider()

    st.subheader('🗺️ 전국 개최지 위치 비교')
    st.caption('확인하고 싶은 페스티벌을 선택하면 해당 위치의 지도와 상세 주소, 관련 교통편이 표시됩니다.')
    
    selected_location = st.selectbox(
        '조회할 개최지를 선택하세요:',
        ['전체 개최지 분포 보기', '더글로우 (일산 킨텍스)', '인천 펜타포트 (송도달빛축제공원)', '부산 국제 록 페스티벌 (삼락생태공원)', '피크 페스티벌 (난지한강공원)', '파크 뮤직 페스티벌 (올림픽공원)']
    )

    map_coordinates = pd.DataFrame({
        'lat': [37.668, 37.408, 35.166, 37.568, 37.521],
        'lon': [126.743, 126.634, 128.971, 126.883, 127.130]
    })

    if selected_location == '전체 개최지 분포 보기':
        st.map(map_coordinates)
    else:
        if '더글로우' in selected_location:
            filtered_df = map_coordinates.iloc[[0]]
            st.map(filtered_df)
            st.success('**📍 더글로우 개최지 정보**\n\n* **주소**: 경기도 고양시 일산서구 킨텍스로 217-60 (킨텍스 제2전시장)\n* **교통편**: 지하철 3호선 대화역 도보 15분 거리')
        elif '인천 펜타포트' in selected_location:
            filtered_df = map_coordinates.iloc[[1]]
            st.map(filtered_df)
            st.error('**📍 인천 펜타포트 개최지 정보**\n\n* **주소**: 인천광역시 연수구 센트럴로 350 (송도달빛축제공원)\n* **교통편**: 인천지하철 1호선 송도달빛축제공원역 도보 10분 거리')
        elif '부산 국제 록' in selected_location:
            filtered_df = map_coordinates.iloc[[2]]
            st.map(filtered_df)
            st.info('**📍 부산 국제 록 페스티벌 개최지 정보**\n\n* **주소**: 부산광역시 사상구 삼락동 29-46 (삼락생태공원)\n* **교통편**: 부산김해경전철 괘법르네시떼역 도보 10분 거리')
        elif '피크 페스티벌' in selected_location:
            filtered_df = map_coordinates.iloc[[3]]
            st.map(filtered_df)
            st.warning('**📍 피크 페스티벌 개최지 정보**\n\n* **주소**: 서울특별시 마포구 한강난지로 162 (난지한강공원 젊음의 광장)\n* **교통편**: 지하철 6호선 월드컵경기장역에서 대중교통 또는 도보 이동')
        elif '파크 뮤직 페스티벌' in selected_location:
            filtered_df = map_coordinates.iloc[[4]]
            st.map(filtered_df)
            st.success('**📍 서울 파크 뮤직 페스티벌 개최지 정보**\n\n* **주소**: 서울특별시 송파구 올림픽로 424 (올림픽공원 88잔디마당)\n* **교통편**: 지하철 5호선 및 9호선 올림픽공원역 도보 10분 거리')
            
    st.divider()

    st.subheader('야외 vs 실내 페스티벌 장단점 비교')
    col_type1, col_type2 = st.columns(2)
    with col_type1:
        st.info('**야외형 페스티벌 (펜타포트, 부락페, 피크페, 파뮤페)**\n\n* **장점**: 넓은 자연 경관과 잔디밭에서 느끼는 해방감 및 거대한 슬램핏 형성 가능\n* **단점**: 날씨 영향이 매우 크며 더위나 폭우 시 극심한 체력 소모 유발')
    with col_type2:
        st.warning('**실내형 페스티벌 (더글로우, 파뮤페)**\n\n* **장점**: 기후 조건에 영향받지 않는 일정한 쾌적함 및 깨끗한 음향 및 조명 설계 가능\n* **단점**: 상대적으로 한정된 공간감과 야외 피크닉 돗자리 피칭 분위기 제한')
    st.divider()

    st.subheader('📈 티켓 가격 및 개최 월 비교 분석')
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    festivals_labels = ['Glow', 'Penta', 'Busan', 'Peak', 'Park']
    ticket_prices_k = [121, 120, 110, 110, 119]
    festival_months = [3, 8, 10, 5, 6]

    axes[0].plot(festivals_labels, ticket_prices_k, 'rs-', linewidth=2, markersize=8)
    axes[0].set_title('Ticket Price (Unit: 1,000 KRW)')
    axes[0].set_ylim(100, 125)
    axes[0].grid(True)

    axes[1].bar(festivals_labels, festival_months, color='green', alpha=0.7)
    axes[1].set_title('Festival Month')
    axes[1].set_ylim(1, 12)
    axes[1].set_yticks(range(1, 13))
    axes[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)



with tab4:
    st.header('Preparation')
    st.markdown('성공적인 페스티벌 관람을 위한 카운트다운 일정표와 페스티벌별 현장 스케치 영상, 필수 체크리스트 점검')
    st.divider()

    st.subheader('⏰ 2026년도 페스티벌 실시간 카운트다운')
    today_date = date.today()
    glow_target = date(2026, 3, 21)
    peak_target = date(2026, 5, 23)
    park_target = date(2026, 6, 20)
    penta_target = date(2026, 8, 1)
    busan_target = date(2026, 10, 2)

    d_glow = (glow_target - today_date).days
    d_peak = (peak_target - today_date).days
    d_park = (park_target - today_date).days
    d_penta = (penta_target - today_date).days
    d_busan = (busan_target - today_date).days

    def format_dday(days):
        if days > 0:
            return f"D-{days}"
        elif days == 0:
            return "D-Day!"
        else:
            return f"D+{-days}"

    col_day1, col_day2, col_day3, col_day4, col_day5 = st.columns(5)
    col_day1.metric('더글로우', format_dday(d_glow))
    col_day2.metric('피크 페스티벌', format_dday(d_peak))
    col_day3.metric('파크 뮤직 페스티벌', format_dday(d_park))
    col_day4.metric('인천 펜타포트', format_dday(d_penta))
    col_day5.metric('부산 국제 록 페스티벌', format_dday(d_busan))
    st.divider()

    st.subheader('🎧 현장 프리뷰 미디어 플레이어')
    st.caption('각 페스티벌을 선택하면 해당 페스티벌 현장의 실시간 유튜브 라이브 스케치 영상을 직접 감상할 수 있습니다.')
    
    selected_media = st.selectbox(
        '감상하고 싶은 페스티벌 미디어를 선택하세요:',
        ['더글로우 (The Glow)', '인천 펜타포트 록 페스티벌', '부산 국제 록 페스티벌', '피크 페스티벌', '서울 파크 뮤직 페스티벌']
    )

    if selected_media == '더글로우 (The Glow)':
            st.markdown('**🎥 리도어 : 2026 The Glow 현장 스케치 영상**')
            st.video('https://youtu.be/vBsbWrX4nFo?si=tmeeOpn94StlgdZe')
    elif selected_media == '인천 펜타포트 록 페스티벌':
            st.markdown('**🎥 잔나비 : 비틀 파워! + 고백극장 | 2024 인천 펜타포트 락페스티벌**')
            st.video('https://youtu.be/7JYvcIn_1os?si=FP5S9X89JGb2V8c1&t=270')
    elif selected_media == '부산 국제 록 페스티벌':
            st.markdown('**🎥 이승윤 : 날아가자 Live Clip @ 2025 BUSAN INTERNATIONAL ROCK FESTIVAL**')
            st.video('https://www.youtube.com/watch?v=ZeUJljStWs0')
    elif selected_media == '피크 페스티벌':
            st.markdown('**🎥 SPYAIR : 2026 피크 페스티벌 현장 스케치 영상**')
            st.video('https://www.youtube.com/watch?v=zL-m_YXqa6g')
    elif selected_media == '서울 파크 뮤직 페스티벌':
            st.markdown('**2023 SEOUL PARK MUSIC FESTIVAL After Movie**')
            st.video('https://www.youtube.com/watch?v=U96mX4KYfVQ')

    st.divider()

    st.subheader('📝 페스티벌 필수 준비물 체크리스트')
    st.caption('가방에 넣은 물건은 박스를 체크하여 지워나가 보세요.')
    st.checkbox('**모바일 티켓 및 신분증** *(입장 시 본인 확인 필수)*', value=False)
    st.checkbox('**개인 돗자리** *(지정 피크닉 구역 휴식 및 대기 필수품)*', value=False)
    st.checkbox('**슬로건** *(아티스트 응원 물품)*', value=False)
    st.checkbox('**고용량 보조 배터리** *(휴대폰 방전 방지)*', value=False)
    st.checkbox('**선글라스, 캡모자, 선크림** *(뜨거운 자외선 및 낮시간 열사병 방지)*', value=False)
    st.checkbox('**일회용 우비 또는 초소형 3단 우산** *(갑작스러운 한여름 기습 소나기 대비)*', value=False)
    st.checkbox('**편안하고 튼튼한 운동화** *(스탠딩존 대기와 슬램 시 발 보호용)*', value=False)