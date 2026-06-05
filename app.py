import streamlit as st

# 앱의 타이틀 설정
st.title("🎈 나의 첫 Streamlit 웹 앱")

# 텍스트 출력
st.write("안녕하세요! 파이썬으로 만든 웹 앱입니다.")

# 인터랙티브한 위젯 추가
name = st.text_input("당신의 이름은 무엇인가요?")
if name:
    st.write(f"반가워요, {name}님! 멋진 하루 보내세요!")