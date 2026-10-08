
import pandas as pd
import streamlit as st

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. LOAD THE DATASET

# Load the symptom dataset.
df = pd.read_csv("symptom_data.csv")

# 2. CREATE THE TF-IDF MODEL

# TF-IDF converts text into numerical values.
vectorizer = TfidfVectorizer()

# Learn the important words from the symptom descriptions.
symptom_vectors = vectorizer.fit_transform(df["symptoms"])


# 3. EMERGENCY WARNING TERMS

emergency_terms = [
    "severe chest pain",
    "chest pain",
    "severe breathing difficulty",
    "difficulty breathing",
    "cannot breathe",
    "fainting",
    "unconscious",
    "severe confusion"
]

# 4. SYMPTOM ANALYSIS FUNCTION

def analyze_symptoms(user_input):
    """
    Analyze the user's symptom description.

    The function:
    1. Checks for simplified emergency warning terms.
    2. Converts the input into TF-IDF values.
    3. Calculates cosine similarity.
    4. Finds the closest symptom category.
    5. Uses a similarity threshold for uncertain cases.
    """

    # Convert the user's input to lowercase.
    text = user_input.lower()

    # Check for emergency warning terms first.
    for term in emergency_terms:
        if term in text:
            return (
                "Emergency warning signs",
                "Emergency",
                1.0
            )

    # Convert the user's symptoms into TF-IDF values.
    user_vector = vectorizer.transform([user_input])

    # Compare the user's symptoms with the dataset.
    similarities = cosine_similarity(
        user_vector,
        symptom_vectors
    )[0]

    # Find the category with the highest similarity.
    best_match_index = similarities.argmax()

    # Get the similarity score.
    similarity_score = similarities[best_match_index]

    # Minimum similarity required for a classification.
    minimum_similarity = 0.20

    # If the similarity is too low, return an uncertain result.
    if similarity_score < minimum_similarity:
        return (
            "No reliable match",
            "Uncertain",
            similarity_score
        )

    # Get the matching category.
    best_category = df.iloc[best_match_index]["category"]

    # Get the associated triage level.
    triage_level = df.iloc[best_match_index]["triage"]

    return (
        best_category,
        triage_level,
        similarity_score
    )


# 5. STREAMLIT USER INTERFACE

st.title("AI-Powered Symptom Checker")

st.write(
    "This educational application uses basic natural language "
    "processing to compare a user's symptom description with "
    "a small symptom dataset."
)


# Healthcare disclaimer
st.warning(
    "Important: This application is an educational AI prototype "
    "and is NOT a medical diagnostic tool. It does not provide "
    "medical advice or replace evaluation by a qualified healthcare "
    "professional. If you believe you are experiencing a medical "
    "emergency, seek immediate professional medical care."
)


# Text box for the user's symptoms
user_input = st.text_area(
    "Describe your symptoms:",
    placeholder="Example: I have a fever, cough and sore throat."
)


# Analyze button
if st.button("Analyze Symptoms"):

    # Make sure the user entered something.
    if not user_input.strip():

        st.error("Please enter your symptoms first.")

    else:

        # Analyze the user's symptoms.
        category, triage, score = analyze_symptoms(user_input)

        st.subheader("Result")

        st.write("**Possible symptom category:**", category)

        st.write("**Educational triage level:**", triage)

        st.write(
            "**Similarity score:**",
            round(score, 3)
        )

        # Additional warning for uncertain results.
        if triage == "Uncertain":

            st.info(
                "The application could not find a reliable match. "
                "Please do not use this result to make medical decisions."
            )

        # Emergency warning.
        elif triage == "Emergency":

            st.error(
                "Emergency warning signs were detected. "
                "Seek immediate professional medical attention."
            )
