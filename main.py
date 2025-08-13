import streamlit as st

def main():
    # 페이지 기본 설정
    st.set_page_config(layout="centered")

    # 파스텔톤 테마 CSS 주입 (새롭게 추가된 부분)
    st.markdown(
        """
        <style>
        /* --- 전체 페이지 배경 및 기본 텍스트 색상 설정 --- */
        .stApp {
            background-color: #FFF0E5; /* AntiqueWhite - 아주 연한 따뜻한 베이지 */
            color: #555555; /* 부드러운 다크 그레이 텍스트 */
            font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif; /* 한글 폰트 적용 */
        }

        /* --- 제목 (h1, h2, h3 등) 색상 설정 --- */
        h1, h2, h3, h4, h5, h6 {
            color: #E27D60; /* 따뜻하고 부드러운 오렌지-핑크 계열 */
        }

        /* --- 버튼 색상 설정 --- */
        .stButton>button {
            background-color: #FFDAB9; /* PeachPuff - 따뜻한 피치색 버튼 배경 */
            color: #555555; /* 버튼 텍스트 색상 */
            border: 1px solid #FFC0CB; /* 연한 핑크 테두리 */
            border-radius: 8px; /* 부드러운 모서리 */
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1); /* 약간의 그림자로 입체감 추가 */
            transition: all 0.3s ease-in-out; /* 부드러운 호버 효과 */
        }
        .stButton>button:hover {
            background-color: #F0B28C; /* 호버 시 약간 어두운 피치색 */
            border-color: #EEA0B0; /* 호버 시 테두리 색상 */
            transform: translateY(-2px); /* 살짝 떠오르는 효과 */
        }

        /* --- 선택 상자 (Selectbox) 및 입력 필드 배경/테두리 색상 설정 --- */
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background-color: #FFFAF0; /* FloralWhite - 입력 필드 배경 */
            border: 1px solid #FFC0CB; /* 연한 핑크 테두리 */
            border-radius: 8px;
            color: #555555;
        }
        /* 드롭다운 메뉴 아이템 호버 시 색상 */
        .st-bb, .st-bc, .st-bd, .st-be, .st-bf, .st-bg, .st-bh, .st-bi, .st-bj, .st-bk, .st-bl, .st-bm, .st-bn, .st-bo, .st-bp, .st-bq, .st-br, .st-bs, .st-bw, .st-bx, .st-by, .st-bz, .st-ca, .st-cb, .st-cc, .st-cd, .st-ce, .st-cf, .st-cg, .st-ch, .st-ci, .st-cj, .st-ck, .st-cl, .st-cm, .st-cn, .st-co, .st-cp, .st-cq, .st-cr, .st-cs, .st-ct, .st-cu, .st-cv, .st-cw, .st-cx, .st-cy, .st-cz, .st-da, .st-db, .st-dc, .st-dd, .st-de, .st-df, .st-dg, .st-dh, .st-di, .st-dj, .st-dk, .st-dl, .st-dm, .st-dn, .st-do, .st-dp, .st-dq, .st-dr, .st-ds, .st-dt, .st-du, .st-dv, .st-dw, .st-dx, .st-dy, .st-dz, .st-ea, .st-eb, .st-ec, .st-ed, .st-ee, .st-ef, .st-eg, .st-eh, .st-ei, .st-ej, .st-ek, .st-el, .st-em, .st-en, .st-eo, .st-ep, .st-eq, .st-er, .st-es, .st-et, .st-eu, .st-ev, .st-ew, .st-ex, .st-ey, .st-ez {
            background-color: #FFEFD5 !important; /* PapayaWhip - 호버 시 배경색 */
        }

        /* --- 성공, 경고, 정보 메시지 박스 색상 설정 --- */
        .stSuccess {
            background-color: #E6FFE6; /* 연한 파스텔 그린 */
            color: #285A28; /* 어두운 녹색 텍스트 */
            border-left: 5px solid #66CC66; /* 초록색 강조 테두리 */
            border-radius: 8px;
        }
        .stWarning {
            background-color: #FFF8E6; /* 연한 파스텔 오렌지 */
            color: #7B4B00; /* 어두운 오렌지 텍스트 */
            border-left: 5px solid #FFD072; /* 주황색 강조 테두리 */
            border-radius: 8px;
        }
        .stInfo {
            background-color: #E6F3FF; /* 연한 파스텔 블루 */
            color: #2F5F8F; /* 어두운 파란색 텍스트 */
            border-left: 5px solid #72B9F4; /* 파란색 강조 테두리 */
            border-radius: 8px;
        }

        /* --- 수평선 (hr) 색상 설정 --- */
        hr {
            border-top: 1px solid #FFC0CB; /* 연한 핑크 수평선 */
        }

        /* Markdown List items */
        ul li {
            color: #696969; /* 리스트 텍스트 색상 조정 */
        }

        </style>
        """,
        unsafe_allow_html=True # HTML 렌더링을 허용합니다.
    )

    st.title("💖 MBTI 유형으로 알아보는 나와 같은 연예인 & 어울리는 동물!")
    st.write("당신의 MBTI 유형을 선택하고, 나와 같은 연예인과 어울리는 동물을 찾아보세요!")
    st.markdown("---")

    mbti_types = [
        "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
        "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
    ]

    selected_mbti = st.selectbox("✨ 당신의 MBTI 유형은 무엇인가요?", mbti_types)

    # 연예인 데이터베이스 (이전과 동일)
    celebrity_data = {
        "ISTJ": ["강동원", "송해나", "효린", "박명수", "김영철"],
        "ISFJ": ["박보검", "태연", "정국 (BTS)", "이선균", "윤종신"],
        "INFJ": ["아이유", "차은우", "강유미", "이제훈", "솔라 (마마무)"],
        "INTJ": ["손석희", "봉준호", "이수현 (악동뮤지션)", "류준열"],
        "ISTP": ["박나래", "성동일", "한혜진", "조인성"],
        "ISFP": ["백현 (EXO)", "유재석", "RM (BTS)", "수지"],
        "INFP": ["아이유", "방탄소년단 RM", "강동원 (재검사)", "제니 (블랙핑크)"],
        "INTP": ["정은지", "안테나 유희열", "진 (BTS)"],
        "ESTP": ["홍진영", "전현무", "윤하"],
        "ESFP": ["강남", "노홍철", "백종원", "윤두준"],
        "ENFP": ["세븐틴 승관", "뷔 (BTS)", "제이홉 (BTS)", "블랙핑크 로제"],
        "ENTP": ["제시", "도경수 (EXO)", "개코 (다이나믹 듀오)", "박준형 (god)"],
        "ESTJ": ["김구라", "정동원", "이민정"],
        "ESFJ": ["이승기", "지민 (BTS)", "지효 (트와이스)", "조이 (레드벨벳)"],
        "ENFJ": ["엑소 수호", "민경훈", "김태리"],
        "ENTJ": ["김희선", "지창욱"]
    }

    # MBTI별 동물 이미지 데이터베이스 (이전과 동일)
    animal_images = {
        "ISTJ": {"name": "호랑이", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Siberian_Tiger_in_Kao_Laem_ya_National_Park_%2801%29.jpg/800px-Siberian_Tiger_in_Kao_Laem_ya_National_Park_%2801%29.jpg"},
        "ISFJ": {"name": "사슴", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Red_deer_stag.jpg/800px-Red_deer_stag.jpg"},
        "INFJ": {"name": "부엉이", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Tawny_Owl_%28Strix_aluco%29_at_Zoo_Jihlava%2C_Czech_Republic.jpg/800px-Tawny_Owl_%28Strix_aluco%29_at_Zoo_Jihlava%2C_Czech_Republic.jpg"},
        "INTJ": {"name": "늑대", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Wolf_standing_in_snow.jpg/800px-Wolf_standing_in_snow.jpg"},
        "ISTP": {"name": "매", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Hawk_%28P-P%29.JPG/800px-Hawk_%28P-P%29.JPG"},
        "ISFP": {"name": "나비", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/P_aurantiaca.jpg/800px-P_aurantiaca.jpg"},
        "INFP": {"name": "고양이", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/800px-Cat03.jpg"},
        "INTP": {"name": "여우", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/RedFox06.jpg/800px-RedFox06.jpg"},
        "ESTP": {"name": "치타", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Cheetah_in_Namibia.jpg/800px-Cheetah_in_Namibia.jpg"},
        "ESFP": {"name": "돌고래", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Dolphin_cropped.jpg/800px-Dolphin_cropped.jpg"},
        "ENFP": {"name": "수달", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Sea_Otter_%28Enhydra_lutris%29_%282035887201%29.jpg/800px-Sea_Otter_%28Enhydra_lutris%29_%282035887201%29.jpg"},
        "ENTP": {"name": "원숭이", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Rhesus_Macaque_%28Macaca_mulatta%29.jpg/800px-Rhesus_Macaque_%28Macaca_mulatta%29.jpg"},
        "ESTJ": {"name": "사자", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/800px-Lion_waiting_in_Namibia.jpg"},
        "ESFJ": {"name": "강아지", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Dog.jpg/800px-Dog.jpg"},
        "ENFJ": {"name": "코끼리", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/African_Elephant_cropped.jpg/800px-African_Elephant_cropped.jpg"},
        "ENTJ": {"name": "독수리", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Eagle_at_Alaska_Raptor_Center.jpg/800px-Eagle_at_Alaska_Raptor_Center.jpg"}
    }


    if st.button("⭐️ 나와 같은 MBTI 연예인 및 동물 찾기"):
        st.markdown("---") # 구분선 추가

        # 1. MBTI별 어울리는 동물 이미지 표시
        if selected_mbti in animal_images:
            animal_info = animal_images[selected_mbti]
            st.subheader(f"✨ **{selected_mbti}** 유형과 어울리는 동물은 바로...")
            st.write(f"💖 **{animal_info['name']}** 입니다!")
            st.image(animal_info['url'], caption=f"{selected_mbti} 유형을 대표하는 {animal_info['name']}", use_column_width=True)
            st.markdown("---") # 구분선 추가
        else:
            st.warning("아직 해당 MBTI 유형에 대한 동물 정보가 없습니다. ㅠㅠ")

        # 2. 연예인 정보 표시
        if selected_mbti in celebrity_data:
            matched_celebs = celebrity_data[selected_mbti]
            st.subheader(f"🎉 **{selected_mbti}** 유형의 연예인은 다음과 같습니다!")
            for celeb in matched_celebs:
                st.markdown(f"- **{celeb}**")
            st.balloons() # 결과를 보여줄 때 풍선 효과를 띄워보세요!

        else:
            st.warning("아직 해당 MBTI 유형에 대한 연예인 정보가 없습니다. ㅠㅠ 데이터를 추가해주세요!")
            st.info("다음에 더 많은 정보를 추가하여 찾아볼 수 있도록 노력하겠습니다!")

if __name__ == "__main__":
    main()
