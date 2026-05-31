import streamlit as st
import pandas as pd
import re
from datetime import date
import database
from prediction import predict_health
def generate_remark(glucose, haemoglobin, cholesterol):
    return f"Glucose: {glucose}, Haemoglobin: {haemoglobin}, Cholesterol: {cholesterol}"

database.create_table()

st.title("Health Prediction App")

st.subheader("Patient Information")

name = st.text_input("Full Name")

dob = st.date_input("Date of Birth")

email = st.text_input("Email Address")

glucose = st.number_input("Glucose", min_value=0.0)

haemoglobin = st.number_input("Haemoglobin", min_value=0.0)

cholesterol = st.number_input("Cholesterol", min_value=0.0)

if st.button("Submit"):

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(email_pattern, email):
        st.error("Invalid Email Address")

    elif dob > date.today():
        st.error("Future Date Not Allowed")

    else:

        prediction = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        remark = generate_remark(
            glucose,
            haemoglobin,
            cholesterol
        )

        database.add_patient(
            (
                name,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remark
            )
        )

        st.success("Patient Saved Successfully")

        st.write("Prediction:", prediction)

        st.write("AI Remark:")

        st.info(remark)

# ----------------------------
# Display Saved Records
# ----------------------------

st.subheader("Patient Records")

records = database.get_patients()

df = pd.DataFrame(
    records,
    columns=[
        "ID",
        "Name",
        "DOB",
        "Email",
        "Glucose",
        "Haemoglobin",
        "Cholesterol",
        "Remarks"
    ]
)

st.dataframe(df)

# ----------------------------
# Delete Patient
# ----------------------------

st.subheader("Delete Patient")

delete_id = st.number_input(
    "Enter Patient ID to Delete",
    min_value=1,
    step=1
)

if st.button("Delete Patient"):

    database.delete_patient(delete_id)

    st.success(
        f"Patient ID {delete_id} deleted successfully"
    )

    st.rerun()
