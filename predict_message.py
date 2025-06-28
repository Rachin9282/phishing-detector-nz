import joblib

# Load model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# User input
text = input("Enter a message to check if it's a phishing attempt: ")

# Transform and predict
text_vector = vectorizer.transform([text])
prediction = model.predict(text_vector)

# Result
if prediction[0] == 1:
    print("🚨 Warning: This message is a PHISHING attempt.")
else:
    print("✅ This message appears to be LEGITIMATE.")
