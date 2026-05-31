import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_remark(glucose, haemoglobin, cholesterol):

    prompt = f"""
    Analyze the following patient data:

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Generate a short professional health remark in 2-3 lines.
    """

    response = model.generate_content(prompt)

    return response.text