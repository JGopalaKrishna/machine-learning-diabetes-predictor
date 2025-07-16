import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
import base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

Home_img = get_base64_image("./img/machineLearningProjectDiabetesPrediction.png")

def show_home():
    #styles
    st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

    # Informational Content
    st.markdown(f"""
        <h2>📣 Welcome to Diabetes Prediction System!</h2>
        <img src="data:image/png;base64,{Home_img}" alt="Diabetes Prediction System">
        <p><strong>Understanding Your Health, Empowered by Diabetes Prediction System</strong></p>
        <p>Diabetes is a growing concern, and early detection can make a world of difference. At Diabetes Prediction System, we believe in empowering you with insights into your health. Our system uses advanced technology to help you understand your potential risk of developing diabetes, so you can take proactive steps towards a healthier future.</p>

        <h2>🤖 What is the Diabetes Prediction System and How Does it Work?</h2>
        <p>Think of it as your personal health assistant. It's designed to analyze important information about your health and lifestyle to give you a personalized understanding of your diabetes risk.</p>

        <h3>Here’s a simple breakdown of how it works:</h3>
        <ol>
            <li><strong>You Share Your Health Information:</strong> Input key details like:
                <ul>
                    <li>Pregnancies</li>
                    <li>Glucose</li>
                    <li>Blood Pressure</li>
                    <li>Skin Thickness</li>
                    <li>Insulin</li>
                    <li>BMI</li>
                    <li>Diabetes Pedigree Function</li>
                    <li>Age</li>
                </ul>
            </li>
            <li><strong>Smart Technology Analyzes the Data:</strong> Our machine learning model looks for patterns in your input based on real patient data.</li>
            <li><strong>You Get Your Personalized Risk Assessment:</strong> A prediction of your potential risk, helping guide you to take action.</li>
        </ol>

        <h2>🌟 Why is this Important for You?</h2>
        <ul>
            <li><strong>Early Awareness:</strong> Detecting risk early motivates healthy lifestyle changes.</li>
            <li><strong>Proactive Health Management:</strong> Enables informed discussions with your doctor.</li>
            <li><strong>User-Friendly:</strong> No technical skills required.</li>
            <li><strong>Confidential & Secure:</strong> Your data is private and protected.</li>
        </ul>

        <h2>📊 What Does Your Prediction Mean?</h2>
        <ul>
            <li><strong>Low Risk:</strong> Keep up a healthy lifestyle and get regular checkups.</li>
            <li><strong>High Risk:</strong> Consult your doctor immediately for further testing and planning.</li>
        </ul>
        <p><strong>Important Note:</strong> This is a prediction tool. It should <em>never</em> replace professional medical advice, diagnosis, or treatment. Always consult your doctor for medical concerns.</p>
    """, unsafe_allow_html=True)