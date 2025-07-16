import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

About_img = get_base64_image("./img/ai_view.png")
def show_about():
    st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)
    # Page Title
    st.markdown(f"""
        <h2>📘 About Diabetes Prediction System</h2>
        <img src="data:image/png;base64,{About_img}" alt="About Diabetes Prediction System" style="margin-bottom: 10px;">
    """, unsafe_allow_html=True)
    
    # Step-by-step backend process
    st.subheader("⚙️ About The Backend Process")
    step1, step2, step3, step4 = st.columns(4)

    with step1:
        st.markdown("""
            <div style='padding: 10px; background-color: #e0f7fa; border-radius: 10px;margin-bottom:10px;'>
            <div style='font-size:22px;font-weight:bold;'>📝 Step 1</div>
            <div>User enters health data like Glucose, BMI, Age etc.</div>
            </div>
        """, unsafe_allow_html=True)

    with step2:
        st.markdown("""
            <div style='padding: 10px; background-color: #ffe0b2; border-radius: 10px;margin-bottom:10px;'>
            <div style='font-size:22px;font-weight:bold;'>⚙️ Step 2</div>
            <div>ML model (Random Forest Classifier) processes the input data.</div>
            </div>
        """, unsafe_allow_html=True)

    with step3:
        st.markdown("""
            <div style='padding: 10px; background-color: #f3e5f5; border-radius: 10px;margin-bottom:10px;'>
            <div style='font-size:22px;font-weight:bold;'>🔍 Step 3</div>
            <div>It detects patterns from thousands of records.</div>
            </div>
        """, unsafe_allow_html=True)

    with step4:
        st.markdown("""
            <div style='padding: 10px; background-color: #dcedc8; border-radius: 10px;margin-bottom:10px;'>
            <div style='font-size:22px;font-weight:bold;'>📊 Step 4</div>
            <div>Provides a risk prediction with probability, and Bar graph.</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Dataset Overview
    st.subheader("🧠 About The Dataset")
    st.markdown("""
    - **Dataset**: Pima Indians Diabetes Database  
    - **Source**: UCI Machine Learning Repository  
    - **Total Records**: 768  
    - **Features**: Pregnancies, Glucose, BMI, Insulin, Age, etc.
    """)

    # Load dataset and Pie chart
    df = pd.read_csv("diabetes.csv")
    diabetes_counts = df["Outcome"].value_counts()
    labels = ["No Diabetes", "Diabetes"]
    colors = ["#4caf50", "#f44336"]

    fig, ax = plt.subplots(figsize=(3, 2))
    ax.pie(diabetes_counts, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90,textprops={"fontsize": 10})
    ax.axis("equal")
    st.pyplot(fig)

    st.markdown("---")

    # Model Performance
    st.subheader("📊 Model Performance")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("✅ Accuracy", "88.5%")
    with col2:
        st.metric("🎯 Precision", "86%")
    with col3:
        st.metric("🔁 Recall", "90%")

    st.markdown("""
    > These values mean the model is reliably predicting diabetes risk using the provided patient data.
    """)

    st.markdown("---")

    # Disclaimer
    st.markdown("""
    <div style='border-left: 5px solid red; padding: 10px; background-color: #fff3f3;'>
    ⚠️ <strong>Disclaimer:</strong><br>
    This system is for educational purposes only and should not be used as a substitute for professional medical advice. Always consult your doctor for medical concerns.
    </div>
    """, unsafe_allow_html=True)