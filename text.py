iimport streamlit as st

def get_naeshin_university_recommendation(gpa_grade):
    """
    내신 등급(수시)에 따른 대학 추천 리스트를 반환합니다.
    (매우 단순화된 예시이며, 실제 입시는 다양한 변수를 고려해야 합니다.)
    """
    if 1.0 <= gpa_grade <= 1.5:
        return {
            "tier": "최상위권 (수시 교과/종합)",
            "universities": ["서울대학교", "연세대학교", "고려대학교"],
            "note": "매우 우수한 성적입니다. 각 대학의 학과별 특성, 수능 최저 기준, 서류 및 면접을 면밀히 살펴보세요."
        }
    elif 1.5 < gpa_grade <= 2.5:
        return {
            "tier": "상위권 (수시 교과/종합)",
            "universities": ["서강대학교", "성균관대학교", "한양대학교", "이화여자대학교", "중앙대학교", "경희대학교", "한국외국어대학교", "서울시립대학교"],
            "note": "우수한 성적입니다. 학생부 내용, 자기소개서, 면접 준비 등 종합 전형 요소를 고려하거나, 교과 전형의 수능 최저 충족 여부를 확인해 보세요."
        }
    elif 2.5 < gpa_grade <= 3.5:
        return {
            "tier": "중상위권 (수시 교과/종합)",
            "universities": ["건국대학교", "동국대학교", "홍익대학교", "숙명여자대학교", "국민대학교", "숭실대학교", "세종대학교", "단국대학교(죽전/천안)", "지방 거점 국립대학교 (예: 부산대, 경북대 등)"],
            "note": "안정적인 성적입니다. 지원하려는 학과의 경쟁률과 커리큘럼, 학생부 반영 방식을 꼼꼼히 확인하고, 학생부 종합 전형을 적극적으로 활용하는 전략도 좋습니다."
        }
    elif 3.5 < gpa_grade <= 4.5:
        return {
            "tier": "중위권 (수시 교과/종합)",
            "universities": ["명지대학교", "상명대학교", "가천대학교", "인하대학교", "아주대학교", "경기대학교", "한성대학교", "삼육대학교", "일부 지방 국립/사립대학교"],
            "note": "다양한 선택지가 있습니다. 학생부 종합 전형이나 적성고사, 논술 전형 등 다른 전형 요소를 함께 고려하고, 희망하는 학과의 경쟁률 및 입결을 확인하세요."
        }
    elif 4.5 < gpa_grade <= 9.0:
        return {
            "tier": "지원 가능 (수시 교과/종합)",
            "universities": ["전국 각지의 전문대학교 및 일부 4년제 대학교", "폭넓은 전형 선택을 통해 진학 가능"],
            "note": "성적 외에 면접, 비교과 활동, 수능 최저 등 다른 전형 요소를 활용하거나, 지역 균형 선발, 사회적 배려 대상자 전형 등 특별 전형을 알아보는 것도 방법입니다."
        }
    else:
        return {
            "tier": "정보 없음",
            "universities": [],
            "note": "올바른 내신 등급(1.0~9.0)을 입력해주세요."
        }

def get_suneung_university_recommendation(suneung_grade):
    """
    수능 등급(정시)에 따른 대학 추천 리스트를 반환합니다.
    (매우 단순화된 예시이며, 실제 입시는 다양한 변수를 고려해야 합니다.)
    """
    if 1.0 <= suneung_grade <= 1.5:
        return {
            "tier": "최상위권 (정시)",
            "universities": ["서울대학교", "연세대학교", "고려대학교", "의과대학", "치과대학", "한의과대학"],
            "note": "모든 영역에서 최상위권 성적입니다. 원하는 학과의 정시 반영 비율, 탐구 선택 과목 등을 신중하게 고려하세요."
        }
    elif 1.5 < suneung_grade <= 2.5:
        return {
            "tier": "상위권 (정시)",
            "universities": ["서강대학교", "성균관대학교", "한양대학교", "중앙대학교", "경희대학교", "이화여자대학교", "한국외국어대학교", "서울시립대학교", "KAIST, POSTECH (수시 위주지만 참고)"],
            "note": "우수한 성적입니다. 희망 대학의 수능 영역별 반영 비율, 가산점 등을 확인하고 전략적인 지원이 필요합니다."
        }
    elif 2.5 < suneung_grade <= 3.5:
        return {
            "tier": "중상위권 (정시)",
            "universities": ["건국대학교", "동국대학교", "홍익대학교", "숙명여자대학교", "국민대학교", "숭실대학교", "세종대학교", "인하대학교", "아주대학교", "지방 거점 국립대학교 (상위 학과)"],
            "note": "안정적인 성적입니다. 군별 모집과 다군 활용 전략, 백분위/표준점수 유불리를 분석하여 지원하세요."
        }
    elif 3.5 < suneung_grade <= 4.5:
        return {
            "tier": "중위권 (정시)",
            "universities": ["명지대학교", "상명대학교", "가천대학교", "경기대학교", "한성대학교", "삼육대학교", "수도권 주요 4년제 및 지방 주요 4년제 대학교"],
            "note": "다양한 선택지가 있습니다. 원하는 학과와 대학의 최근 3개년 정시 입결, 추가 합격률 등을 참고하는 것이 좋습니다."
        }
    elif 4.5 < suneung_grade <= 9.0:
        return {
            "tier": "지원 가능 (정시)",
            "universities": ["전국 각지의 전문대학교 및 일부 4년제 대학교", "폭넓은 선택을 통해 진학 가능"],
            "note": "일부 대학은 수능 위주 전형 외에도 수시 이월 인원, 지역 인재 전형 등 다양한 정시 모집 방법이 있습니다."
        }
    else:
        return {
            "tier": "정보 없음",
            "universities": [],
            "note": "올바른 수능 등급(1.0~9.0)을 입력해주세요."
        }


# Streamlit 앱 시작
st.set_page_config(
    page_title="대학 입시 추천기 (내신 & 정시)",
    page_icon="🎓",
    layout="centered"
)

st.title("📚 대학 입시 추천 프로그램")
st.markdown("---")

st.write(
    """
    **송현2777님, 안녕하세요!** 이 프로그램은 사용자의 **내신 평균 등급(수시)** 또는 
    **수능 평균 등급(정시)**을 바탕으로 참고할 만한 대학 리스트를 제공합니다. 
    **실제 대학 입시는 본인의 내신/수능 외에도 학생부 내용, 비교과 활동, 면접, 논술, 
    수능 영역별 반영 비율, 가산점 등 다양한 요소를 종합적으로 평가하므로, 
    이 결과는 참고용으로만 활용해 주세요!**
    """
)

# 사용자에게 입시 유형 선택 받기
admission_type = st.radio(
    "어떤 기준으로 추천받고 싶으신가요?",
    ("내신(수시) 기준", "수능(정시) 기준")
)

st.markdown("---")

if admission_type == "내신(수시) 기준":
    # 사용자 입력 받기 (내신)
    gpa_input = st.number_input(
        "📏 본인의 **내신 평균 등급**을 입력해 주세요 (예: 2.3):",
        min_value=1.0,
        max_value=9.0,
        value=3.0, # 초기값 설정
        step=0.1,
        format="%.1f"
    )
    if st.button("✨ 내신 기반 추천 대학 확인하기"):
        if gpa_input:
            recommendation = get_naeshin_university_recommendation(gpa_input)

            st.subheader(f"✅ 입력하신 내신 등급 **{gpa_input}등급**에 대한 추천")
            st.markdown(f"**해당 등급대:** {recommendation['tier']}")

            if recommendation['universities']:
                st.write("---")
                st.write("🎯 **추천 대학 리스트:**")
                for univ in recommendation['universities']:
                    st.write(f"- {univ}")
                st.write("---")
                st.info(f"💡 **참고:** {recommendation['note']}")
            else:
                st.warning(f"⚠️ {recommendation['note']}")
        else:
            st.error("⚠️ 내신 등급을 입력해주세요.")

else: # admission_type == "수능(정시) 기준"
    # 사용자 입력 받기 (수능)
    suneung_input = st.number_input(
        "📝 본인의 **수능 평균 등급**을 입력해 주세요 (예: 2.8):",
        min_value=1.0,
        max_value=9.0,
        value=3.0, # 초기값 설정
        step=0.1,
        format="%.1f"
    )
    if st.button("✨ 수능 기반 추천 대학 확인하기"):
        if suneung_input:
            recommendation = get_suneung_university_recommendation(suneung_input)

            st.subheader(f"✅ 입력하신 수능 등급 **{suneung_input}등급**에 대한 추천")
            st.markdown(f"**해당 등급대:** {recommendation['tier']}")

            if recommendation['universities']:
                st.write("---")
                st.write("🎯 **추천 대학 리스트:**")
                for univ in recommendation['universities']:
                    st.write(f"- {univ}")
                st.write("---")
                st.info(f"💡 **참고:** {recommendation['note']}")
            else:
                st.warning(f"⚠️ {recommendation['note']}")
        else:
            st.error("⚠️ 수능 등급을 입력해주세요.")

st.markdown("---")
st.write("본 프로그램은 교육 상담의 목적으로 제공되지 않으며, 정확한 입시 정보는 각 대학의 모집 요강을 반드시 확인해야 합니다.")
st.write("냥이 드림"
