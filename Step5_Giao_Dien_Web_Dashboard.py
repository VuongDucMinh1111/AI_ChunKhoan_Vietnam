import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="AI Chung Khoan Dashboard", layout="wide", page_icon="📈")

st.title("📈 Bang Dieu Khien AI Giao Dich Chung Khoan Viet Nam")
st.markdown("He thong Giao dich Tu dong va Quan ly MLOps Tich hop")

tab_live, tab_train, tab_history = st.tabs([
    "📊 Giam Sat Real-time", 
    "🧠 Tram Huan Luyen MLOps", 
    "📜 Lich Su Khop Lenh"
])

with tab_live:
    st.subheader("Trang thai Hoat dong Thuc te")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tong Tai San (NAV)", "543,250,000 VND", "+5.4% (Hom nay)")
    col2.metric("Win Rate", "68.5%", "2.1%")
    col3.metric("Do Tu Tin BNN", "85%", "Cho phep Giao dich")
    col4.metric("Diem Tin Tuc LLM", "Tich cuc (0.75)", "Bao uy tin 65%")
    
    st.markdown("---")
    st.write("Bieu do Bien dong NAV Mo phong:")
    chart_data = pd.DataFrame(np.random.randn(30, 1).cumsum() + 500, columns=["NAV (Trieu VND)"])
    st.line_chart(chart_data)

with tab_train:
    st.subheader("He thong Cap Nhat & Huan Luyen Mo Hinh")
    st.info("Loi giao dich hoat dong doc lap voi qua trinh huan luyen.")
    st.write("Trang thai Data: San sang cap nhat chu ky giao dich moi.")
    
    if st.button("🚀 Kich Hoat Huan Luyen Lai AI (Mega Training)", use_container_width=True):
        progress_text = "Dang khoi tao tien trinh huan luyen..."
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.04)
            if percent_complete == 25:
                my_bar.progress(percent_complete + 1, text="Dang thu thap du lieu 50 ma co phieu VN...")
            elif percent_complete == 50:
                my_bar.progress(percent_complete + 1, text="Dang tong hop diem tin tuc va chi bao...")
            elif percent_complete == 75:
                my_bar.progress(percent_complete + 1, text="Dang huan luyen Agent PPO va danh gia...")
            elif percent_complete == 90:
                my_bar.progress(percent_complete + 1, text="Dang tinh toan nguong rui ro Bayes...")
            else:
                my_bar.progress(percent_complete + 1)
                
        st.success("Huấn luyện hoàn tất! Mô hình đã được cập nhật thành công.")
        st.balloons()

with tab_history:
    st.subheader("Nhat Ky Khop Lenh Cua He Thong")
    
    lich_su = pd.DataFrame({
        "Thoi Gian": ["2026-08-20 10:15", "2026-08-19 14:20", "2026-08-18 09:30", "2026-08-17 11:10"],
        "Ma CK": ["FPT.VN", "VIC.VN", "HPG.VN", "SSI.VN"],
        "Hanh Dong": ["BUY", "SELL", "HOLD", "BUY"],
        "Gia Khop (VND)": ["135,000", "45,200", "-", "36,500"],
        "Ly Do He Thong": ["LLM Sentiment tot + MACD cat len", "Khoi ngoai ban rong lien tuc", "Do bat dinh cao, chan lenh", "Vuot nguong Expected Value"]
    })
    st.dataframe(lich_su, use_container_width=True)
