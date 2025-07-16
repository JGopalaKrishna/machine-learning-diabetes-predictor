import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

def show_prediction():
    #styles
    st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

    st.markdown("""<h2>🔬 Diabetes_Prediction</h2>""", unsafe_allow_html=True)
    st.write("Enter patient data to predict the likelihood of diabetes.")

    # Input form
    pregnancies = st.number_input('Pregnancies', min_value=0)
    glucose = st.number_input('Glucose', min_value=0)
    blood_pressure = st.number_input('Blood Pressure', min_value=0)
    skin_thickness = st.number_input('Skin Thickness', min_value=0)
    insulin = st.number_input('Insulin', min_value=0)
    bmi = st.number_input('BMI', min_value=0.0)
    diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0)
    age = st.number_input('Age', min_value=1)
    st.write(".")
    # Load and prepare dataset
    @st.cache_data
    def load_data():
        df = pd.read_csv("diabetes.csv")  # Add this file to the same directory
        X = df.drop("Outcome", axis=1)
        df["Outcome"] = df["Outcome"].astype(int)
        y = df["Outcome"]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    X_train, X_test, y_train, y_test = load_data()
    y_test = y_test.astype(int)

    # 🛠️ Fix the read-only array issue
    X_train = X_train.copy()
    y_train = y_train.copy()

    # Model training
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Predict
    if st.button("Predict Diabetes"):
        user_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, diabetes_pedigree, age]])
        prediction = model.predict(user_data)
        prediction_proba = model.predict_proba(user_data)

        prob0 = prediction_proba[0][0]*100  # Probability of class 0 (no diabetes)
        prob1 = prediction_proba[0][1]*100  # Probability of class 1 (diabetes)

        if prediction[0] == 0:
            st.markdown(f"""
            <div class='positiveResult'>
                <div>✅ Low chance of Diabetes.</div>
                <div class='ResultInner_div'>
                    <div>🟢 No Diabetes: {prob0:.2f}% </div>
                    <div style='color:#fc665b;'>🔴 Risk of Diabetes : {prob1:.2f}%</div>
                </div>
            </div>
            """,unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='negativeResult'>
                <div>❌ High chance of Diabetes.</div>
                <div class='ResultInner_div'>
                    <div>🔴 Risk of Diabetes : {prob1:.2f}%</div>
                    <div style='color:#04cf15;'>🟢 Absence of Diabetes : {prob0:.2f}%</div>
                </div>
            </div>
            """,unsafe_allow_html=True)

        if prob1 > 50:
            with st.expander("📋 Recommended Health Tips"):
                st.markdown("""
                - 🍎 Eat a balanced, low-sugar diet
                - 🚶 Stay active daily (30+ mins walk)
                - 💧 Stay hydrated
                - 🧘 Manage stress with mindfulness
                - 🩺 Regular checkups with your doctor
                """)

        # Pie chart
        fig, ax = plt.subplots(figsize=(2.5,1.3))
        ax.pie([prob0, prob1],
            labels=["No Diabetes", "Diabetes"],
            colors=["green", "red"],
            autopct='%1.1f%%',
            textprops={'fontsize': 6})
        ax.axis("equal")
        ax.set_title("Prediction Probability", fontsize=6)

        plt.tight_layout()
        plt.show()
        st.pyplot(fig)

    # Model accuracy
    # accuracy = accuracy_score(y_test, model.predict(X_test))
    # st.write(f"Model Accuracy: **{accuracy*100:.2f}%**")