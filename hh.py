import streamlit as st

# 페이지 설정
st.set_page_config(page_title="박해진 자기소개", layout="wide", page_icon="🚒")

# 사용자 정의 CSS로 꾸미기
st.markdown("""
<style>
/* 배경 스타일 */
body {
    background: url('https://images.unsplash.com/photo-1607990286185-2eaa1c530026?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80') no-repeat center center fixed;
    background-size: cover;
    color: #f0f0f0;
    font-family: 'Poppins', sans-serif;
    font-size: 1.2rem;
}

/* Google Fonts 연결 */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

/* 사이드바 스타일 */
.sidebar .sidebar-content {
    background-color: rgba(0, 0, 0, 0.7);
    padding: 2rem;
    border-radius: 0 10px 10px 0;
}
.stRadio > label {
    color: #ffd54f;
    font-size: 1.1rem;
}

/* 카드 스타일 */
.card {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 1.8rem;
    border-radius: 12px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.5);
    margin-bottom: 2rem;
}

/* 헤더 스타일 */
h1 {
    color: #ffd54f;
    font-weight: 600;
    font-size: 2.8rem;
}
h2 {
    color: #ffd54f;
    font-weight: 600;
    font-size: 2.2rem;
}
h3 {
    color: #ffd54f;
    font-weight: 600;
    font-size: 1.8rem;
}

/* 구분선 */
.divider {
    height: 4px;
    background: linear-gradient(to right, #ffd54f, #ff6f00);
    margin: 1.5rem 0;
}

/* 푸터 스타일 */
.footer {
    text-align: center;
    font-size: 1rem;
    color: #cccccc;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# 사이드바 네비게이션
st.sidebar.title("📑 목차")
st.sidebar.markdown("---")
page = st.sidebar.radio("페이지 선택", (
    "1. 자기소개", 
    "2. 학력 및 프로젝트", 
    "3. 경력 및 자격증", 
    "4. 강점 및 취미"
))

# 페이지별 함수 정의
def page1():
    st.title("안녕하세요, **박해진**입니다 👋")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
**🎓 재난안전소방학과 4학년 | 건양대학교**  
저는 화재 안전과 인명 보호를 위한 연구와 프로젝트에 열정을 가지고 있습니다.  
다양한 학술 및 실습 경험을 통해 문제 해결 능력과 협업 스킬을 키워왔습니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)


def page2():
    st.title("🎓 학력 및 주요 프로젝트")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
- **건양대학교 재난안전소방학과 (2020 ~ 현재)**  
- **전동 킥보드 다인 탑승 방지 시뮬레이터**: 무게·발자국 센서 기반 과탑승 감지 장치 개발  
- **PLC 7-세그먼트 디스플레이 회로**: 숫자 표시 및 오디오 출력 회로 설계  
- **심폐소생술 대회**: 금상 수상
        """)
        st.markdown('</div>', unsafe_allow_html=True)


def page3():
    st.title("💼 경력 및 자격증")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
- **소방 전기 튜터링**: 회로 가닥수 계산 및 도면 해석 교육 진행  
- **자격증**: 위험물산업기사, 소방설비(전기)기사, 전기기사  
- **추진 중**: 예다 종합설계감리사무소 입사 예정
    """)
    st.markdown('</div>', unsafe_allow_html=True)


def page4():
    st.title("🌟 강점 및 취미")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
- **문제 해결력**: 기술적 이슈 분석 및 개선  
- **협업 능력**: 다양한 팀 프로젝트 리더 경험  
- **호기심**: 양자역학·웹 개발·사회 이슈 탐구  
- **취미**: 코딩, 여행(일본·제주도), 다양한 분야의 이데올로기
            
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# 페이지 매핑 및 실행
pages = {
    "1. 자기소개": page1,
    "2. 학력 및 프로젝트": page2,
    "3. 경력 및 자격증": page3,
    "4. 강점 및 취미": page4
}

pages[page]()

# 푸터 추가
st.markdown('<div class="footer">© 2025 박해진 | 문의: hjpark4242@gmail.com</div>', unsafe_allow_html=True)











































# import streamlit as st
# # HTML 파일 읽기
# with open("h.html", "r", encoding="utf-8") as f:
#     html_code = f.read()

# # HTML 랜더링
# st.html(html_code)

# import streamlit as st
# import streamlit.components.v1 as components

# color = st.radio('색상을 선택하세요', ('red', 'green'))
# background= st.radio('색상을 선택하세요', ('rgba(0,0,10,0.3)', 'rgba(0,0,288,0.3)'))
# font= st.radio('폰트 크기를 선택하세요', ('10px', '20px'))
# html_code =f"""
# <p style= "color: {color}; 
#    font-size: {font};
#    background-color: {background};
#    margin: 20px;
#    padding: 20px;
#    text-align: center;
#    text-decoration: underline;
#    border: 3px dashed green;
#    border-radius: 120px">
#    인라인 스타일을 사용한 문단입니다. 
# </p>
# """


# # HTML 코드
# html_code7 = """
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>내 프로필</title>
#     <style>
#         body {
#             font-family: 'Arial', sans-serif;
#             line-height: 1.6;
#             margin: 0;
#             padding: 20px;
#             background-color: #fff5f5;
#         }

#         .profile-container {
#             max-width: 800px;
#             margin: 0 auto;
#             background-color: white;
#             padding: 30px;
#             border-radius: 10px;
#             box-shadow: 0 0 10px rgba(255, 0, 0, 0.1);
#         }

#         .profile-header {
#             text-align: center;
#             margin-bottom: 30px;
#         }

#         .profile-pic {
#             width: 150px;
#             height: 150px;
#             border-radius: 50%;
#             object-fit: cover;
#             border: 3px solid #e11d48;
#             float: right;  /* 오른쪽으로 이동 */
#             margin-left: 30px;  /* 텍스트와의 간격 */
#         }

#         h1 {
#             color: #b91c1c;
#             margin-top: 15px;
#         }

#         .subtitle {
#             color: #944;
#             font-style: italic;
#         }

#         .section {
#             margin-bottom: 25px;
#         }

#         .section-title {
#             font-size: 20px;
#             color: #fff;
#             background-color: rgba(255, 69, 0, 0.8);
#             text-align: center;
#             border-bottom: 5px solid #fca5a5;
#             padding: 8px;
#             border-radius: 5px;
#         }

#         .skills-list {
#             display: flex;
#             flex-wrap: wrap;
#             gap: 10px;
#             margin-top: 10px;
#         }

#         .skill-tag {
#             background-color: #ffe4e1;
#             color: #b91c1c;
#             padding: 5px 15px;
#             border-radius: 20px;
#             font-size: 14px;
#         }

#         .contact-info {
#             display: flex;
#             justify-content: center;
#             gap: 20px;
#             margin-top: 30px;
#         }

#         .contact-item {
#             display: flex;
#             align-items: center;
#             gap: 5px;
#         }

#         .contact-icon {
#             color: #e11d48;
#         }
#     </style>
# </head>
# <body>
#     <div class="profile-container">
#         <div class="profile-header">
#             <img class="profile-pic" src="https://png.pngtree.com/background/20230517/original/pngtree-very-long-hair-feline-looking-ahead-to-the-sun-picture-image_2623945.jpg" alt="프로필 사진">
#             <h1>정의영</h1>
#             <p class="subtitle">소방학과 전공 대학생</p>
#         </div>

#         <div class="section">
#             <h2 class="section-title">소개</h2>
#             <p>
#                 안녕하세요! 저는 <strong style="color: #b91c1c;">재난안전소방학과를 전공</strong>하고 있는 대학생 정의영입니다.<br>
#                 사람들의 생명과 안전을 지키는 일에 열정을 가지고 있으며, <strong>소방 공무원</strong>이 되는 것이 제 꿈입니다.<br>
#                 위기 상황에 대처하는 전문성을 키우기 위해 다양한 이론과 실무 지식을 습득 중입니다.
#             </p>
#         </div>

#         <div class="section">
#             <h2 class="section-title">보유 기술 및 관심 분야</h2>
#             <div class="skills-list">
#                 <span class="skill-tag">소방 기계 설비</span>
#                 <span class="skill-tag">위험물 안전관리</span>
#                 <span class="skill-tag">화재 예방 시스템</span>
#                 <span class="skill-tag">응급처치</span>
#                 <span class="skill-tag">CAD 도면 해석</span>
#                 <span class="skill-tag">Python</span>
#             </div>
#         </div>

#         <div class="section">
#             <h2 class="section-title">학력</h2>
#             <p>
#                 <strong>건양대학교</strong> - 재난안전소방학과 (2022 - 현재)<br>
#                 화재역학, 소방시설론, 구조 및 구급 등 다양한 전공 수업 이수 중
#             </p>
#         </div>

#         <div class="contact-info">
#             <div class="contact-item">
#                 <span class="contact-icon">📧</span>
#                 <span>firehero@email.com</span>
#             </div>
#             <div class="contact-item">
#                 <span class="contact-icon">📱</span>
#                 <span>010-1234-5678</span>
#             </div>
#         </div>
#     </div>
# </body>
# </html>
# """

# # HTML 코드 렌더링
# components.html(html_code7, height=1000)

# # HTML 파일 읽기
# with open("hh.html", "r", encoding="utf-8") as f:
#     html_code = f.read()

# # Streamlit에서 HTML 렌더링
# st.html(html_code)

