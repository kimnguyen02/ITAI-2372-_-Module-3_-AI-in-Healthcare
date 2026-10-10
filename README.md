
# AI-Powered Symptom Checker and Triage Tool

## Project Overview

This project is a simple AI-driven healthcare application developed
for educational purposes.

The application uses Natural Language Processing (NLP) to analyze
user-entered symptom descriptions and compare them with a small
educational symptom dataset.

The system uses TF-IDF vectorization and cosine similarity to identify
the most similar symptom category and provide an educational triage
level.

## How It Works

The application follows these steps:

1. The user enters a description of their symptoms.
2. The application processes the text.
3. TF-IDF converts the symptom descriptions into numerical features.
4. Cosine similarity compares the user's input with the symptom dataset.
5. The system identifies the closest symptom category.
6. The application displays an educational triage level.
7. If the similarity is too low, the system returns an uncertain result.
8. Simplified emergency warning terms trigger an emergency warning.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- TF-IDF
- Cosine Similarity
- Natural Language Processing

## Dataset

The project uses a small, manually created educational dataset
containing symptom descriptions, categories, and triage levels.

This dataset is not intended to represent a clinical or medically
validated dataset.

## Example

Example input:

"I have a fever, cough and sore throat."

The application may return:

- Possible category: Flu-like illness
- Triage level: Routine

## Testing

The application was tested using several different symptom descriptions,
including:

- Fever, cough and sore throat
- Headache and nausea
- Runny nose and itchy eyes
- Severe chest pain and difficulty breathing
- An unrelated finger injury

The system successfully identified matching categories and returned an
uncertain result when the input did not sufficiently match the dataset.

## Ethical Considerations

### Medical Safety

This application is an educational prototype and is not a medical
diagnostic system.

It should not be used to diagnose or treat medical conditions.

### Data Quality

The application's performance depends heavily on the quality and
coverage of the symptom dataset.

### Bias

A small dataset may not represent the full diversity of real-world
healthcare situations and may produce unreliable results for symptoms
not represented in the dataset.

### Privacy

The prototype does not store or transmit user-entered symptoms.

A real healthcare application would require appropriate privacy,
security, and regulatory safeguards.

## Limitations

- Small educational dataset
- Limited symptom categories
- No clinical validation
- Simple NLP approach
- No patient medical history
- No demographic or clinical context
- Not suitable for real medical decision-making

## Disclaimer

This application is for educational purposes only and is not a
substitute for professional medical advice, diagnosis, or treatment.

If you believe you are experiencing a medical emergency, seek
immediate professional medical care.

## Future Improvements

Future versions could include:

- A larger medically validated dataset
- More advanced NLP models
- Better synonym and phrase recognition
- Clinical validation
- Improved uncertainty detection
- More comprehensive safety rules
- Secure handling of patient data
