import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(page_title="리스크 예측 시스템", layout="wide")

st.title("📊 리스크 예측 시스템")

st.markdown("데이터를 입력하면 리스크를 간단히 예측합니다.")

# 사이드바 입력
st.sidebar.header("입력 변수")

age = st.sidebar.slider("나이", 18, 80, 30)
income = st.sidebar.number_input("연소득", value=3000)
credit_score = st.sidebar.slider("신용 점수", 300, 900, 600)

# 예측 버튼
if st.sidebar.button("예측하기"):

    # 🔹 임시 로직 (나중에 모델로 교체 가능)
    risk_score = (
        (80 - age) * 0.2 +
        (700 - credit_score) * 0.5 +
        (5000 - income) * 0.0005
    )

    risk_score = max(0, min(100, risk_score))

    st.subheader("📌 예측 결과")

    if risk_score > 70:
        st.error(f"⚠️ 고위험 ({risk_score:.2f})")
    elif risk_score > 40:
        st.warning(f"⚡ 중위험 ({risk_score:.2f})")
    else:
        st.success(f"✅ 저위험 ({risk_score:.2f})")

    st.progress(int(risk_score))

# 데이터 업로드 기능
st.subheader("📂 데이터 업로드 (선택)")
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("업로드된 데이터:")
    st.dataframe(df.head())
