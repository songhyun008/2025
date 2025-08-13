import streamlit as st

def main():
    st.set_page_config(layout="centered") # 페이지 레이아웃 설정

    st.title("💖 MBTI 유형으로 알아보는 나와 같은 연예인!")
    st.write("당신의 MBTI 유형을 선택하고, 나와 같은 연예인을 찾아보세요!")
    st.markdown("---")

    mbti_types = [
        "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
        "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
    ]

    selected_mbti = st.selectbox("✨ 당신의 MBTI 유형은 무엇인가요?", mbti_types)

    # 연예인 데이터베이스
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

    if st.button("⭐️ 나와 같은 MBTI 연예인 찾기"):
        st.markdown("---") # 구분선 추가
        if selected_mbti in celebrity_data:
            matched_celebs = celebrity_data[selected_mbti]
            st.success(f"🎉 **{selected_mbti}** 유형의 연예인은 다음과 같습니다!")
            for celeb in matched_celebs:
                st.markdown(f"- **{celeb}**")
            st.balloons()

        else:
            st.warning("아직 해당 MBTI 유형에 대한 연예인 정보가 없습니다. ㅠㅠ 데이터를 추가해주세요!")
            st.info("다음에 더 많은 연예인 정보를 추가하여 찾아볼 수 있도록 노력하겠습니다!")

if __name__ == "__main__":
    main()
