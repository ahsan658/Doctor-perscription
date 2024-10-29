import streamlit as st

# Diagnosis and prescription data (simple rules-based approach)
symptoms_diagnosis = {
    "fever": ("Common Cold", "Paracetamol"),
    "cough": ("Bronchitis", "Cough Syrup"),
    "headache": ("Migraine", "Ibuprofen"),
    "stomach ache": ("Gastritis", "Antacid"),
    "sore throat": ("Pharyngitis", "Amoxicillin")
}

def diagnose(symptom):
    # Diagnosis and medicine prescription based on symptom
    if symptom in symptoms_diagnosis:
        diagnosis, medicine = symptoms_diagnosis[symptom]
        return diagnosis, medicine
    else:
        return "Unknown condition", "Consult a healthcare provider"

# Main function
def main():
    st.title("Disease Diagnosis and Prescription App")

    # User input for symptoms
    st.header("Enter Your Symptoms")
    symptom = st.selectbox("Choose a Symptom", list(symptoms_diagnosis.keys()))
    
    if st.button("Diagnose and Prescribe"):
        diagnosis, medicine = diagnose(symptom)
        
        st.write(f"**Diagnosis**: {diagnosis}")
        st.write(f"**Prescribed Medicine**: {medicine}")
        
        # Additional advice
        if diagnosis == "Unknown condition":
            st.warning("Please consult a healthcare provider for further diagnosis.")
        else:
            st.success(f"You are prescribed **{medicine}** for {diagnosis}.")
            st.info("Please follow the dosage instructions provided by your healthcare provider.")

if __name__ == "__main__":
    main()
