def predict_health(glucose, haemoglobin, cholesterol):

    if glucose > 140 and cholesterol > 240:
        return "High Diabetes and Heart Disease Risk"

    elif glucose > 140:
        return "Possible Diabetes Risk"

    elif cholesterol > 240:
        return "High Cholesterol Risk"

    elif haemoglobin < 12:
        return "Possible Anemia Risk"