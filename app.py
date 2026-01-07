import streamlit as st
import pandas as pd
import joblib
import os

st.title("🎓 Student Performance Prediction App")
st.write("Decision Tree based Pass / Fail Prediction")

MODEL_PATH = "student_performance_model.joblib"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found")
else:
    model = joblib.load(MODEL_PATH)

    math = st.slider("Math Score", 0, 100, 50)
    reading = st.slider("Reading Score", 0, 100, 50)
    writing = st.slider("Writing Score", 0, 100, 50)

    if st.button("Predict"):
        input_data = pd.DataFrame(
            [[math, reading, writing]],
            columns=["math score", "reading score", "writing score"]
        )

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.success("✅ Student will PASS")
        else:
            st.error("❌ Student will FAIL")
