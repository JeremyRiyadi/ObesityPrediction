import streamlit as st
import requests

def run_interface() :
    st.title("Obesity Level Classifier Application")

    gender = st.radio("Select your gender", ["Male", "Female"])
    age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
    height = st.number_input("Your height (in meters)", min_value=0.3, max_value=2.5, value=1.70, step=0.01)
    weight = st.number_input("Your weight (in kg)", min_value=10.0, max_value=300.0, value=70.0, step=0.1)
    family_history = st.radio("Family history of being overweight?", ["yes", "no"])
    favc = st.radio("Do you often eat high-calorie food?", ["yes", "no"])
    fcvc = st.slider("Vegetable consumption frequency (1-3)", min_value=1.0, max_value=3.0, value=2.0, step=0.1)
    ncp = st.slider("How many main meals do you eat per day?", min_value=1.0, max_value=5.0, value=3.0, step=0.1)
    caec = st.selectbox("Do you snack between meals?", ["no", "Sometimes", "Frequently", "Always"])
    smoke = st.radio("Do you smoke?", ["yes", "no"])
    ch2o = st.slider("Water intake (1-3)", min_value=1.0, max_value=3.0, value=2.0, step=0.1)
    scc = st.radio("Do you track your calorie intake?", ["yes", "no"])
    faf = st.slider("How often do you exercise? (0-3)", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
    tue = st.slider("Time spent using electronic devices daily (0-3)", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
    calc = st.selectbox("How often do you drink alcohol?", ["no", "Sometimes", "Frequently", "Always"])
    mtrans = st.selectbox("Primary mode of transportation", ["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"])

    input = {
        'Gender': gender,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'family_history_with_overweight': family_history,
        'FAVC': favc,
        'FCVC': fcvc,
        'NCP': ncp,
        'CAEC': caec,
        'SMOKE': smoke,
        'CH2O': ch2o,
        'SCC': scc,
        'FAF': faf,
        'TUE': tue,
        'CALC': calc,
        'MTRANS': mtrans
    }

    if st.button("Make Prediction") :
        try :
            res = requests.post("http://127.0.0.1:8000/predict", json=input)
            if res.status_code == 200 :
                result = res.json()["Prediction"]
                st.success(f"Predicted Obesity Level: {result}")
            else : 
                st.error(f"Error {res.status_code}: {res.text}")
        except Exception as e :
            st.error(f"Failed to connect to API: {e}")

if __name__ == "__main__" :
    run_interface()